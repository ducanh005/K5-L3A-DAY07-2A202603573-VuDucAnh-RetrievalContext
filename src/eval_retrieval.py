"""CP3/CP4 retrieval & context benchmark across lexical, dense, hybrid RRF, and rerank pipelines."""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
STARTER_DIR = REPO_ROOT / "starter"
if str(STARTER_DIR) not in sys.path:
    sys.path.insert(0, str(STARTER_DIR))

from baseline import hit, pack_context, validate  # noqa: E402
from src.config import load_settings  # noqa: E402
from src.embeddings import GeminiQueryEmbedder  # noqa: E402
from src.retrievers import (  # noqa: E402
    Bm25Retriever,
    GeminiRerankRetriever,
    HybridRrfRetriever,
    PgVectorDenseRetriever,
    TfidfRetriever,
)


def _eval_config(
    name: str,
    retriever: Any,
    questions: list[dict[str, Any]],
    *,
    top_k: int = 3,
    budget: int = 2400,
    use_filter: bool = True,
    embedder: GeminiQueryEmbedder | None = None,
    reranker: GeminiRerankRetriever | None = None,
) -> dict[str, Any]:
    start_embed_calls = embedder.stats["api_calls"] if embedder else 0
    start_embed_chars = embedder.stats["input_chars"] if embedder else 0
    start_rerank_tokens = reranker.stats["total_tokens"] if reranker else 0
    start_rerank_calls = reranker.stats["api_calls"] if reranker else 0

    traces: list[dict[str, Any]] = []
    t_all = time.perf_counter()
    for q in questions:
        flt = q.get("filter") if use_filter else None
        t0 = time.perf_counter()
        results = retriever.search(q["question"], filters=flt, top_k=top_k)
        context, ids = pack_context(results, budget=budget)
        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        marked = [{**c, "hit": hit(c, q["gold"])} for c in results]
        traces.append({
            "query_id": q["id"],
            "split": q["split"],
            "type": q.get("type"),
            "question": q["question"],
            "filter": flt,
            "config": name,
            "top_k": top_k,
            "budget_chars": budget,
            "gold": q["gold"],
            "results": marked,
            "context": context,
            "context_ids": ids,
            "context_chars": len(context),
            "elapsed_ms": round(elapsed_ms, 2),
            "hit1": bool(marked and marked[0]["hit"]),
            "hit3": any(c["hit"] for c in marked[:3]),
            "context_hit": any(c["hit"] and c["id"] in ids for c in marked),
        })
    total_seconds = time.perf_counter() - t_all
    n = len(traces)
    summary = {
        "config": name,
        "strategy": getattr(retriever, "strategy_name", name),
        "split": questions[0]["split"],
        "n": n,
        "top_k": top_k,
        "budget_chars": budget,
        "use_filter": use_filter,
        "hit1": sum(t["hit1"] for t in traces),
        "hit1_rate": round(sum(t["hit1"] for t in traces) / n, 4),
        "hit3": sum(t["hit3"] for t in traces),
        "hit3_rate": round(sum(t["hit3"] for t in traces) / n, 4),
        "context_hit": sum(t["context_hit"] for t in traces),
        "context_rate": round(sum(t["context_hit"] for t in traces) / n, 4),
        "avg_context_chars": round(statistics.mean(t["context_chars"] for t in traces), 1),
        "median_ms": round(statistics.median(t["elapsed_ms"] for t in traces), 2),
        "total_seconds": round(total_seconds, 3),
        "embed_api_calls": (embedder.stats["api_calls"] - start_embed_calls) if embedder else 0,
        "embed_input_chars": (embedder.stats["input_chars"] - start_embed_chars) if embedder else 0,
        "rerank_api_calls": (reranker.stats["api_calls"] - start_rerank_calls) if reranker else 0,
        "rerank_tokens": (reranker.stats["total_tokens"] - start_rerank_tokens) if reranker else 0,
    }
    return {"summary": summary, "traces": traces}


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark retrieval & context configs on dev or test split.")
    parser.add_argument("--split", required=True, choices=("dev", "test"))
    parser.add_argument(
        "--configs",
        nargs="+",
        default=[
            "tfidf_b800",
            "tfidf_b2400",
            "bm25_filter_b2400",
            "dense_b800",
            "dense_b2400",
            "hybrid_rrf_b2400",
            "hybrid_rerank_b2400",
        ],
    )
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    out_dir = args.output_dir or (REPO_ROOT / "results" / f"retrieval_{args.split}")
    out_dir.mkdir(parents=True, exist_ok=True)

    chunks = json.loads((REPO_ROOT / "data/chunks.json").read_text(encoding="utf-8"))
    all_qs = json.loads((REPO_ROOT / "data/questions_answerable.json").read_text(encoding="utf-8"))
    questions = [q for q in all_qs if q["split"] == args.split]
    validate(chunks, questions)

    need_api = any(c for c in args.configs if c not in ("tfidf_b800", "tfidf_b2400", "bm25_filter_b2400"))
    settings = load_settings(require_api_key=need_api, require_db=need_api)

    tfidf = TfidfRetriever(chunks)
    bm25 = Bm25Retriever(chunks)

    embedder = None
    dense = None
    hybrid = None
    reranker = None
    if need_api:
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
        hybrid = HybridRrfRetriever(dense, bm25, candidate_k=10, rrf_k=60)
        reranker = GeminiRerankRetriever(
            hybrid,
            settings.gemini_api_key,
            model_name=settings.agent_model,
            candidate_k=10,
        )

    registry: dict[str, dict[str, Any]] = {
        "tfidf_b800": {"retriever": tfidf, "budget": 800, "use_filter": False},
        "tfidf_b2400": {"retriever": tfidf, "budget": 2400, "use_filter": False},
        "bm25_filter_b2400": {"retriever": bm25, "budget": 2400, "use_filter": True},
        "dense_b800": {"retriever": dense, "budget": 800, "use_filter": True},
        "dense_b2400": {"retriever": dense, "budget": 2400, "use_filter": True},
        "hybrid_rrf_b2400": {"retriever": hybrid, "budget": 2400, "use_filter": True},
        "hybrid_rerank_b2400": {"retriever": reranker, "budget": 2400, "use_filter": True},
    }

    summaries: list[dict[str, Any]] = []
    for cfg_name in args.configs:
        if cfg_name not in registry:
            raise ValueError(f"Unknown config: {cfg_name}")
        spec = registry[cfg_name]
        res = _eval_config(
            cfg_name,
            spec["retriever"],
            questions,
            top_k=3,
            budget=spec["budget"],
            use_filter=spec["use_filter"],
            embedder=embedder,
            reranker=reranker if cfg_name == "hybrid_rerank_b2400" else None,
        )
        summaries.append(res["summary"])
        (out_dir / f"traces_{cfg_name}.json").write_text(
            json.dumps(res["traces"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        s = res["summary"]
        print(
            f"{s['config']:22s} | Hit@1={s['hit1']}/{s['n']} ({s['hit1_rate']:.3f}) | "
            f"Hit@3={s['hit3']}/{s['n']} ({s['hit3_rate']:.3f}) | "
            f"Ctx={s['context_hit']}/{s['n']} ({s['context_rate']:.3f}) | "
            f"med={s['median_ms']}ms | total={s['total_seconds']}s | rerank_tok={s['rerank_tokens']}"
        )

    (out_dir / "summary.json").write_text(
        json.dumps(summaries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
