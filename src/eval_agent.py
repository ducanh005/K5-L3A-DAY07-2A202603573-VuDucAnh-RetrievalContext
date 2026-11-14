"""Run full Agent evaluation on dev or test split and export traces + audit template."""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.agent import GeminiController, run_agent_case  # noqa: E402
from src.config import load_settings  # noqa: E402
from src.embeddings import GeminiQueryEmbedder  # noqa: E402
from src.retrievers import (  # noqa: E402
    Bm25Retriever,
    GeminiRerankRetriever,
    HybridRrfRetriever,
    PgVectorDenseRetriever,
)

CONFIG_SPECS: dict[str, dict[str, Any]] = {
    "baseline_dense_b800": {
        "retriever": "dense",
        "context_mode": "starter",
        "budget": 800,
        "top_k": 3,
        "max_searches": 4,
    },
    "dense_smart_b2400": {
        "retriever": "dense",
        "context_mode": "smart",
        "budget": 2400,
        "top_k": 3,
        "max_searches": 4,
    },
    "hybrid_smart_b2400": {
        "retriever": "hybrid",
        "context_mode": "smart",
        "budget": 2400,
        "top_k": 3,
        "max_searches": 4,
    },
    "rerank_smart_b2400": {
        "retriever": "rerank",
        "context_mode": "smart",
        "budget": 2400,
        "top_k": 3,
        "max_searches": 4,
    },
}


def build_retriever(kind: str, chunks: list[dict[str, Any]], settings: Any):
    embedder = GeminiQueryEmbedder(
        settings.gemini_api_key,
        model_name=settings.embedding_model,
        dimensions=settings.embedding_dimensions,
    )
    dense = PgVectorDenseRetriever(
        settings.database_url,
        embedder,
        table_name=settings.pg_table,
        dimensions=settings.embedding_dimensions,
    )
    if kind == "dense":
        return dense, embedder, None
    bm25 = Bm25Retriever(chunks)
    hybrid = HybridRrfRetriever(dense, bm25, candidate_k=10, rrf_k=60)
    if kind == "hybrid":
        return hybrid, embedder, None
    if kind == "rerank":
        reranker = GeminiRerankRetriever(
            hybrid,
            settings.gemini_api_key,
            model_name=settings.agent_model,
            candidate_k=10,
        )
        return reranker, embedder, reranker
    raise ValueError(f"Unknown retriever kind: {kind}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run real Gemini Agent on dev or test split.")
    parser.add_argument("--config", required=True, choices=sorted(CONFIG_SPECS))
    parser.add_argument("--split", required=True, choices=("dev", "test"))
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    spec = CONFIG_SPECS[args.config]
    out_dir = args.output_dir or (REPO_ROOT / "results" / f"agent_{args.split}_{args.config}")
    out_dir.mkdir(parents=True, exist_ok=True)

    settings = load_settings(require_api_key=True, require_db=True)
    chunks = json.loads((REPO_ROOT / "data/chunks.json").read_text(encoding="utf-8"))
    cases = [
        c for c in json.loads((REPO_ROOT / "data/agent_cases.json").read_text(encoding="utf-8"))
        if c["split"] == args.split
    ]
    retriever, embedder, reranker = build_retriever(spec["retriever"], chunks, settings)
    controller = GeminiController(settings.gemini_api_key, model_name=settings.agent_model)

    traces: list[dict[str, Any]] = []
    t0 = time.perf_counter()
    for idx, case in enumerate(cases, 1):
        trace = run_agent_case(
            case,
            controller,
            retriever,
            max_searches=spec["max_searches"],
            top_k=spec["top_k"],
            budget=spec["budget"],
            use_case_filter=True,
            context_mode=spec["context_mode"],
        )
        traces.append(trace)
        print(
            f"[{idx:02d}/{len(cases)}] {trace['query_id']:8s} | ans={str(trace['answerable']):5s} | "
            f"status={trace['status']:8s} | searches={trace['search_calls']} | "
            f"cites={len(trace['citations'])} | tok={trace['usage']['total_tokens']} | ms={trace['elapsed_ms']}"
        )
    total_sec = time.perf_counter() - t0

    (out_dir / "traces.json").write_text(
        json.dumps(traces, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    meta_summary = {
        "config": args.config,
        "split": args.split,
        "spec": spec,
        "model": settings.agent_model,
        "cases": len(traces),
        "answered": sum(1 for t in traces if t["status"] == "answered"),
        "abstain": sum(1 for t in traces if t["status"] == "abstain"),
        "errors": sum(1 for t in traces if t["status"] == "error"),
        "avg_search_calls": round(statistics.mean(t["search_calls"] for t in traces), 2),
        "total_agent_tokens": sum(t["usage"]["total_tokens"] for t in traces),
        "total_embed_calls": embedder.stats["api_calls"],
        "rerank_tokens": reranker.stats["total_tokens"] if reranker else 0,
        "total_seconds": round(total_sec, 2),
        "median_case_ms": round(statistics.median(t["elapsed_ms"] for t in traces), 2),
    }
    (out_dir / "run_summary.json").write_text(
        json.dumps(meta_summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(meta_summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
