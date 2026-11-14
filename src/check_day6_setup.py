"""CP1 setup verification: Day 6 pgvector store + Gemini embedding compatibility."""
from __future__ import annotations

import json
import math
import re
import time
from typing import Any

import psycopg
from google import genai
from google.genai import types
from psycopg.rows import dict_row

from src.config import load_settings

_VECTOR_DIM_RE = re.compile(r"vector\((\d+)\)")


def l2_normalize(vector: list[float]) -> list[float]:
    norm = math.sqrt(sum(v * v for v in vector))
    if norm <= 0.0 or not math.isfinite(norm):
        raise RuntimeError("Received zero or non-finite embedding vector.")
    return [v / norm for v in vector]


def verify_postgres(database_url: str, expected_dim: int) -> dict[str, Any]:
    with psycopg.connect(database_url, row_factory=dict_row) as conn:
        ext = conn.execute(
            "SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';"
        ).fetchone()
        if not ext:
            raise RuntimeError("pgvector extension is not installed in database.")

        tables: dict[str, Any] = {}
        for table in ("day6_chunks_a", "day6_chunks_b", "day6_chunks_c"):
            row = conn.execute(
                """
                SELECT format_type(a.atttypid, a.atttypmod) AS col_type
                FROM pg_attribute a
                JOIN pg_class c ON a.attrelid = c.oid
                JOIN pg_namespace n ON c.relnamespace = n.oid
                WHERE n.nspname = current_schema()
                  AND c.relname = %s
                  AND a.attname = 'embedding'
                  AND NOT a.attisdropped;
                """,
                (table,),
            ).fetchone()
            dim_match = _VECTOR_DIM_RE.search(str(row["col_type"])) if row else None
            dim = int(dim_match.group(1)) if dim_match else None
            count_row = conn.execute(f"SELECT COUNT(*) AS n FROM {table};").fetchone()
            count = int(count_row["n"]) if count_row else 0
            if dim != expected_dim:
                raise RuntimeError(f"Table {table} has vector({dim}), expected vector({expected_dim}).")
            tables[table] = {"dimensions": dim, "rows": count}

    return {"pgvector_version": ext["extversion"], "tables": tables}


def verify_embedding_and_smoke_search(
    database_url: str,
    api_key: str,
    embedding_model: str,
    dimensions: int,
    table: str,
) -> dict[str, Any]:
    client = genai.Client(api_key=api_key)
    t0 = time.perf_counter()
    resp = client.models.embed_content(
        model=embedding_model,
        contents="How does the NIST AI RMF define an AI system?",
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=dimensions,
        ),
    )
    embed_ms = (time.perf_counter() - t0) * 1000.0
    raw_vec = [float(x) for x in resp.embeddings[0].values]
    if len(raw_vec) != dimensions:
        raise RuntimeError(f"Expected {dimensions} dims, got {len(raw_vec)}")
    q_vec = l2_normalize(raw_vec)
    vec_literal = "[" + ",".join(repr(x) for x in q_vec) + "]"

    t1 = time.perf_counter()
    with psycopg.connect(database_url, row_factory=dict_row) as conn:
        hits = conn.execute(
            f"""
            SELECT
                chunk_id,
                document_id,
                page,
                1.0 - (embedding <=> %s::vector) AS score,
                LEFT(text, 120) AS snippet
            FROM {table}
            ORDER BY embedding <=> %s::vector ASC, chunk_id ASC
            LIMIT 3;
            """,
            (vec_literal, vec_literal),
        ).fetchall()
    search_ms = (time.perf_counter() - t1) * 1000.0

    return {
        "embedding_model": embedding_model,
        "dimensions": len(q_vec),
        "l2_norm": round(math.sqrt(sum(v * v for v in q_vec)), 6),
        "embed_ms": round(embed_ms, 2),
        "pgvector_search_ms": round(search_ms, 2),
        "top3_smoke_hits": [
            {
                "id": r["chunk_id"],
                "source_id": r["document_id"],
                "page": int(r["page"]),
                "score": round(float(r["score"]), 4),
                "snippet": r["snippet"],
            }
            for r in hits
        ],
    }


def main() -> None:
    settings = load_settings(require_api_key=True, require_db=True)
    pg_info = verify_postgres(settings.database_url, settings.embedding_dimensions)
    smoke = verify_embedding_and_smoke_search(
        settings.database_url,
        settings.gemini_api_key,
        settings.embedding_model,
        settings.embedding_dimensions,
        settings.pg_table,
    )
    output = {
        "status": "ok",
        "agent_model_configured": settings.agent_model,
        "pg_table": settings.pg_table,
        "postgres": pg_info,
        "smoke_query": smoke,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
