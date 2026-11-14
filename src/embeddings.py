"""Gemini query embedding client compatible with Day 6 pgvector indexes."""
from __future__ import annotations

import math
import re
import time
from typing import Any

from google import genai
from google.genai import errors as genai_errors
from google.genai import types

from src.config import DEFAULT_EMBEDDING_DIMENSIONS, DEFAULT_EMBEDDING_MODEL

_RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}
_RETRY_DELAY_RE = re.compile(r"retry in (\d+(?:\.\d+)?)s", re.IGNORECASE)


def l2_normalize(vector: list[float]) -> list[float]:
    norm = math.sqrt(sum(v * v for v in vector))
    if norm <= 0.0 or not math.isfinite(norm):
        raise RuntimeError("Received zero or non-finite embedding vector from provider.")
    return [v / norm for v in vector]


def _extract_retry_seconds(exc: Exception) -> float | None:
    match = _RETRY_DELAY_RE.search(str(exc))
    return float(match.group(1)) if match else None


def _is_retryable_error(exc: Exception) -> bool:
    if isinstance(exc, genai_errors.APIError) and getattr(exc, "code", None) in _RETRYABLE_STATUS_CODES:
        return True
    msg = str(exc).upper()
    return any(tok in msg for tok in ("429", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE", "TIMEOUT"))


class GeminiQueryEmbedder:
    """Embed search queries using the exact model/dimensions/normalization of Day 6."""

    def __init__(
        self,
        api_key: str,
        *,
        model_name: str = DEFAULT_EMBEDDING_MODEL,
        dimensions: int = DEFAULT_EMBEDDING_DIMENSIONS,
        max_retries: int = 4,
        retry_base_seconds: float = 1.5,
        client: Any | None = None,
    ) -> None:
        if client is None and not api_key.strip():
            raise RuntimeError("GEMINI_API_KEY is required for GeminiQueryEmbedder.")
        self.model_name = model_name.split("/", 1)[1] if model_name.startswith("models/") else model_name
        self.dimensions = dimensions
        self.max_retries = max(0, max_retries)
        self.retry_base_seconds = max(0.1, retry_base_seconds)
        self._client = client if client is not None else genai.Client(api_key=api_key.strip())
        self.stats: dict[str, Any] = {
            "api_calls": 0,
            "query_texts": 0,
            "input_chars": 0,
            "estimated_tokens": 0,
            "elapsed_seconds": 0.0,
            "retries": 0,
        }

    def embed_query(self, query: str) -> list[float]:
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query must be a non-empty string.")
        config = types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=self.dimensions,
        )
        t0 = time.perf_counter()
        response = self._call_with_retry(query, config)
        self.stats["elapsed_seconds"] += time.perf_counter() - t0
        self.stats["api_calls"] += 1
        self.stats["query_texts"] += 1
        self.stats["input_chars"] += len(query)
        self.stats["estimated_tokens"] += max(1, math.ceil(len(query) / 4))

        embeddings = getattr(response, "embeddings", None)
        if not embeddings:
            raise RuntimeError("Gemini API returned no embeddings for query.")
        raw = [float(x) for x in (getattr(embeddings[0], "values", None) or [])]
        if len(raw) != self.dimensions:
            raise RuntimeError(f"Expected {self.dimensions}-dim query vector, got {len(raw)}.")
        return l2_normalize(raw) if self.dimensions != 3072 else raw

    def _call_with_retry(self, text: str, config: types.EmbedContentConfig) -> Any:
        for attempt in range(self.max_retries + 1):
            try:
                return self._client.models.embed_content(
                    model=self.model_name,
                    contents=text,
                    config=config,
                )
            except Exception as exc:
                if attempt >= self.max_retries or not _is_retryable_error(exc):
                    raise
                delay = _extract_retry_seconds(exc) or (self.retry_base_seconds * (2**attempt))
                self.stats["retries"] += 1
                time.sleep(min(delay, 30.0))
        raise RuntimeError("Unreachable retry loop exit.")
