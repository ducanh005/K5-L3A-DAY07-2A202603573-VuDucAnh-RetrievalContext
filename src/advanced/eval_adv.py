"""Evaluation runner, audit worksheet generator, and ADVANCED.md pass/fail scorer."""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.advanced.agent import MultimodalGeminiController, run_advanced_case  # noqa: E402
from src.advanced.ingest import MM_EMBED_DIMS, MM_EMBED_MODEL  # noqa: E402
from src.advanced.retrievers import AdvancedCorpus, AdvancedHybridRetriever  # noqa: E402
from src.config import load_settings  # noqa: E402
from src.embeddings import GeminiQueryEmbedder  # noqa: E402

ADV_CONFIGS: dict[str, dict[str, Any]] = {
    "text_only_rag": {
        "allow_visual": False,
        "use_dense_text": True,
        "use_dense_image": False,
        "enable_vision_inspect": False,
        "strategy_name": "adv_text_only_rrf",
    },
    "multimodal_summary_rag": {
        "allow_visual": True,
        "use_dense_text": True,
        "use_dense_image": True,
        "enable_vision_inspect": False,
        "strategy_name": "adv_multimodal_3way_rrf",
    },
    "multimodal_vision_agent": {
        "allow_visual": True,
        "use_dense_text": True,
        "use_dense_image": True,
        "enable_vision_inspect": True,
        "strategy_name": "adv_multimodal_3way_rrf_vision",
    },
}

CATEGORIES = ("table", "diagram_map", "chart", "multi_hop", "text", "unanswerable")


def load_benchmark(split: str) -> list[dict[str, Any]]:
    path = REPO_ROOT / "data" / "advanced" / f"benchmark_{split}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def write_audit_worksheet(
    cases: list[dict[str, Any]],
    traces: list[dict[str, Any]],
    out_path: Path,
    *,
    config_name: str,
    split: str,
) -> None:
    by_id = {c["id"]: c for c in cases}
    lines = [f"# Advanced Audit Worksheet — `{config_name}` (`{split}`, N={len(traces)})\n"]
    for t in traces:
        c = by_id[t["query_id"]]
        lines.append(
            f"## {t['query_id']} [{t['category']}] — `status={t['status']}` | "
            f"`searches={t['search_calls']}` | `inspects={t['inspect_calls']}` | `err={t['error']}`"
        )
        lines.append(f"- **Question:** {c['question']}")
        if c["answerable"]:
            lines.append(f"- **Expected Answer:** {c['expected_answer']}")
            lines.append(f"- **Gold Source:** pages `{c['gold_pages']}`, regions `{c['gold_regions']}`, note: {c['evidence_notes']}")
        else:
            lines.append(f"- **Expected Behavior:** Abstain — {c['absence_reason']}")
        lines.append(f"- **Agent Answer:** {t['answer']}")
        lines.append(f"- **Citations:** {t['citations']}")
        lines.append(f"- **Citation Details:** {json.dumps(t['citation_details'], ensure_ascii=False)}")
        lines.append(f"- **Inspected Crops:** {t['inspected_regions']}")
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def score_reviews(
    cases: list[dict[str, Any]],
    traces: list[dict[str, Any]],
    reviews: list[dict[str, Any]],
) -> dict[str, Any]:
    """Compute exact ADVANCED.md pass/fail metrics without rounding up or dropping errors."""
    case_ids = [c["id"] for c in cases]
    trace_map = {t["query_id"]: t for t in traces}
    review_map = {r["query_id"]: r for r in reviews}
    if set(case_ids) != set(trace_map) or set(case_ids) != set(review_map):
        raise ValueError(
            f"Mismatch between cases ({len(case_ids)}), traces ({len(trace_map)}), reviews ({len(review_map)})."
        )

    per_cat: dict[str, dict[str, Any]] = {
        cat: {"passed": 0, "total": 0, "rate": 0.0, "failed_ids": []} for cat in CATEGORIES
    }
    system_errors = 0
    total_passed = 0

    for c in cases:
        qid = c["id"]
        cat = c["category"]
        tr = trace_map[qid]
        rv = review_map[qid]
        passed = bool(rv["passed"])
        if tr.get("error") or tr.get("status") == "error":
            system_errors += 1
            if passed:
                raise ValueError(f"System error case {qid} cannot be marked passed=True.")
        if not str(rv.get("reason", "")).strip():
            raise ValueError(f"Missing verification reason for {qid}.")
        per_cat[cat]["total"] += 1
        if passed:
            per_cat[cat]["passed"] += 1
            total_passed += 1
        else:
            per_cat[cat]["failed_ids"].append(qid)

    for cat in CATEGORIES:
        tot = per_cat[cat]["total"]
        per_cat[cat]["rate"] = round((per_cat[cat]["passed"] / tot) * 100.0, 2) if tot else 0.0

    total = len(cases)
    overall_pct = round((total_passed / total) * 100.0, 2) if total else 0.0
    latencies = [t["elapsed_ms"] for t in traces]
    total_tokens = sum(t["usage"]["total_tokens"] for t in traces)
    return {
        "total_cases": total,
        "total_passed": total_passed,
        "pass_rate_pct": overall_pct,
        "meets_90pct_bar": (total > 0 and (total_passed * 10 >= total * 9)),
        "system_errors": system_errors,
        "by_category": per_cat,
        "avg_search_calls": round(sum(t["search_calls"] for t in traces) / total, 2),
        "avg_inspect_calls": round(sum(t["inspect_calls"] for t in traces) / total, 2),
        "total_agent_tokens": total_tokens,
        "total_seconds": round(sum(latencies) / 1000.0, 2),
        "median_case_ms": round(statistics.median(latencies), 2) if latencies else 0.0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run or score Advanced Multimodal Agentic RAG evaluation.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    run_p = sub.add_parser("run", help="Execute Advanced benchmark split.")
    run_p.add_argument("--config", required=True, choices=sorted(ADV_CONFIGS))
    run_p.add_argument("--split", required=True, choices=("dev", "test"))
    run_p.add_argument("--output-dir", type=Path, default=None)

    score_p = sub.add_parser("score", help="Score manually verified reviews against traces.")
    score_p.add_argument("--split", required=True, choices=("dev", "test"))
    score_p.add_argument("--dir", required=True, type=Path)

    args = parser.parse_args()
    if args.cmd == "score":
        cases = load_benchmark(args.split)
        traces = json.loads((args.dir / "traces.json").read_text(encoding="utf-8"))
        reviews = json.loads((args.dir / "reviews.json").read_text(encoding="utf-8"))
        summary = score_reviews(cases, traces, reviews)
        (args.dir / "score_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return

    spec = ADV_CONFIGS[args.config]
    out_dir = args.output_dir or (REPO_ROOT / "results" / f"advanced_{args.split}_{args.config}")
    out_dir.mkdir(parents=True, exist_ok=True)

    settings = load_settings(require_api_key=True, require_db=False)
    corpus = AdvancedCorpus()
    embedder = GeminiQueryEmbedder(
        settings.gemini_api_key,
        model_name=MM_EMBED_MODEL,
        dimensions=MM_EMBED_DIMS,
    )
    retriever = AdvancedHybridRetriever(
        corpus,
        embedder,
        allow_visual=spec["allow_visual"],
        use_dense_text=spec["use_dense_text"],
        use_dense_image=spec["use_dense_image"],
        strategy_name=spec["strategy_name"],
    )
    controller = MultimodalGeminiController(
        settings.gemini_api_key,
        model_name=settings.agent_model,
        enable_vision_inspect=spec["enable_vision_inspect"],
    )
    cases = load_benchmark(args.split)
    traces: list[dict[str, Any]] = []
    t0 = time.perf_counter()
    for idx, case in enumerate(cases, 1):
        tr = run_advanced_case(case, controller, retriever, corpus)
        traces.append(tr)
        print(
            f"[{idx}/{len(cases)}] {case['id']} ({case['category']}) -> "
            f"{tr['status']} | s={tr['search_calls']} i={tr['inspect_calls']} | "
            f"cits={tr['citations']} | {tr['elapsed_ms']}ms",
            flush=True,
        )

    run_summary = {
        "config": args.config,
        "split": args.split,
        "cases": len(traces),
        "answered": sum(1 for t in traces if t["status"] == "answered"),
        "abstain": sum(1 for t in traces if t["status"] == "abstain"),
        "errors": sum(1 for t in traces if t["status"] == "error"),
        "avg_search_calls": round(sum(t["search_calls"] for t in traces) / len(traces), 2),
        "avg_inspect_calls": round(sum(t["inspect_calls"] for t in traces) / len(traces), 2),
        "total_agent_tokens": sum(t["usage"]["total_tokens"] for t in traces),
        "embed_api_calls": embedder.stats["api_calls"],
        "wall_seconds": round(time.perf_counter() - t0, 2),
        "median_case_ms": round(statistics.median(t["elapsed_ms"] for t in traces), 2),
    }
    (out_dir / "traces.json").write_text(json.dumps(traces, indent=2, ensure_ascii=False), encoding="utf-8")
    (out_dir / "run_summary.json").write_text(json.dumps(run_summary, indent=2, ensure_ascii=False), encoding="utf-8")
    write_audit_worksheet(cases, traces, out_dir / "audit_worksheet.md", config_name=args.config, split=args.split)
    print(json.dumps(run_summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
