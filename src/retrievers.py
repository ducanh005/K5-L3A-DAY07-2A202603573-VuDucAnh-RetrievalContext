"""Retrievers for Day 7 implementing the shared Retriever protocol."""
from __future__ import annotations

import math
import re
import unicodedata
from collections import Counter
from typing import Any

import psycopg
from psycopg.rows import dict_row

from src.embeddings import GeminiQueryEmbedder

ALLOWED_FILTER_KEYS = frozenset({"source_id", "document_id", "source", "page", "year", "document_type", "section"})
_VALID_TABLE_RE = re.compile(r"^[a-z][a-z0-9_]{0,63}$")


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", unicodedata.normalize("NFC", text).casefold())


def matches_filter(chunk: dict[str, Any], filters: dict[str, Any] | None) -> bool:
    """Check whether an in-memory chunk matches optional metadata filters."""
    if not filters:
        return True
    unknown = set(filters) - ALLOWED_FILTER_KEYS
    if unknown:
        raise ValueError(f"Unsupported metadata filter keys: {sorted(unknown)}")
    meta = chunk.get("metadata") or {}
    for key, expected in filters.items():
        if expected is None:
            continue
        if key in ("source_id", "document_id"):
            actual = chunk.get("source_id")
        elif key in ("source", "page"):
            actual = chunk.get(key)
        else:
            actual = meta.get(key)
        if isinstance(expected, (list, tuple, set)):
            if actual not in expected:
                return False
        elif actual != expected:
            return False
    return True


def _build_pg_filter_sql(filters: dict[str, Any] | None) -> tuple[list[str], list[Any]]:
    if not filters:
        return [], []
    unknown = set(filters) - ALLOWED_FILTER_KEYS
    if unknown:
        raise ValueError(f"Unsupported metadata filter keys: {sorted(unknown)}")
    clauses: list[str] = []
    params: list[Any] = []
    for key in sorted(filters):
        val = filters[key]
        if val is None:
            continue
        col = "document_id" if key == "source_id" else key
        if isinstance(val, (list, tuple, set)):
            seq = list(val)
            if not seq:
                raise ValueError(f"Filter list for '{key}' must not be empty.")
            clauses.append(f"{col} = ANY(%s)")
            params.append(seq)
        elif isinstance(val, (str, int, float, bool)):
            clauses.append(f"{col} = %s")
            params.append(val)
        else:
            raise ValueError(f"Unsupported filter value type for '{key}': {type(val).__name__}")
    return clauses, params


class TfidfRetriever:
    """Lexical TF-IDF retriever over Day 7 chunk JSON with optional metadata filtering."""

    def __init__(self, chunks: list[dict[str, Any]], *, strategy_name: str = "tfidf") -> None:
        if not chunks:
            raise ValueError("chunks must be non-empty.")
        self.chunks = chunks
        self.strategy_name = strategy_name
        counts = [Counter(tokenize(c["text"])) for c in chunks]
        df = Counter(term for row in counts for term in row)
        self.idf = {term: math.log((1 + len(chunks)) / (1 + count)) + 1 for term, count in df.items()}
        self.vectors = [self._vector(row) for row in counts]

    def _vector(self, counts: Counter[str]) -> dict[str, float]:
        vec = {term: cnt * self.idf[term] for term, cnt in counts.items() if term in self.idf}
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        return {term: v / norm for term, v in vec.items()}

    def search(
        self,
        query: str,
        *,
        filters: dict[str, Any] | None = None,
        top_k: int = 3,
    ) -> list[dict[str, Any]]:
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query must be a non-empty string.")
        if top_k < 1:
            raise ValueError("top_k must be >= 1.")
        q_vec = self._vector(Counter(tokenize(query)))
        results: list[dict[str, Any]] = []
        for chunk, doc_vec in zip(self.chunks, self.vectors):
            if not matches_filter(chunk, filters):
                continue
            score = sum(val * doc_vec.get(term, 0.0) for term, val in q_vec.items())
            if score > 0.0:
                results.append({**chunk, "score": float(score), "strategy": self.strategy_name})
        return sorted(results, key=lambda c: (-c["score"], c["id"]))[:top_k]


class PgVectorDenseRetriever:
    """Dense cosine retriever querying Day 6 PostgreSQL + pgvector table."""

    def __init__(
        self,
        database_url: str,
        embedder: GeminiQueryEmbedder,
        *,
        table_name: str = "day6_chunks_b",
        dimensions: int = 768,
        strategy_name: str = "dense_pgvector",
    ) -> None:
        if not database_url.strip():
            raise ValueError("database_url must be non-empty.")
        if not _VALID_TABLE_RE.match(table_name):
            raise ValueError(f"Invalid table_name: {table_name}")
        self.database_url = database_url.strip()
        self.embedder = embedder
        self.table_name = table_name
        self.dimensions = dimensions
        self.strategy_name = strategy_name

    def search(
        self,
        query: str,
        *,
        filters: dict[str, Any] | None = None,
        top_k: int = 3,
    ) -> list[dict[str, Any]]:
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query must be a non-empty string.")
        if top_k < 1:
            raise ValueError("top_k must be >= 1.")

        query_vec = self.embedder.embed_query(query)
        if len(query_vec) != self.dimensions:
            raise ValueError(f"Query vector dim {len(query_vec)} != {self.dimensions}.")
        vec_literal = "[" + ",".join(repr(float(x)) for x in query_vec) + "]"

        where_clauses, filter_params = _build_pg_filter_sql(filters)
        where_sql = f"WHERE {' AND '.join(where_clauses)}" if where_clauses else ""
        sql = f"""
            SELECT
                chunk_id,
                document_id,
                source,
                page,
                text,
                metadata,
                1.0 - (embedding <=> %s::vector) AS score,
                (embedding <=> %s::vector) AS distance
            FROM {self.table_name}
            {where_sql}
            ORDER BY embedding <=> %s::vector ASC, chunk_id ASC
            LIMIT %s;
        """
        params: list[Any] = [vec_literal, vec_literal, *filter_params, vec_literal, top_k]
        with psycopg.connect(self.database_url, row_factory=dict_row) as conn:
            rows = conn.execute(sql, params).fetchall()

        return [
            {
                "id": row["chunk_id"],
                "source_id": row["document_id"],
                "source": row["source"],
                "page": int(row["page"]),
                "text": row["text"],
                "metadata": dict(row["metadata"] or {}),
                "score": float(row["score"]),
                "distance": float(row["distance"]),
                "strategy": self.strategy_name,
            }
            for row in rows
        ]
