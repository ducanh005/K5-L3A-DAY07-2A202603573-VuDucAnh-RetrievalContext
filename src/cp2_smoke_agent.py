"""CP2 smoke run: real Gemini 2.5 Flash agent + real Day 6 pgvector dense retriever on 4 dev cases."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.agent import GeminiController, run_agent_case  # noqa: E402
from src.config import load_settings  # noqa: E402
from src.embeddings import GeminiQueryEmbedder  # noqa: E402
from src.retrievers import PgVectorDenseRetriever  # noqa: E402


def main() -> None:
    settings = load_settings(require_api_key=True, require_db=True)
    cases = json.loads((REPO_ROOT / "data/agent_cases.json").read_text(encoding="utf-8"))
    target_ids = ("q01", "q05", "q12", "u_dev_01")
    selected = [c for c in cases if c["id"] in target_ids and c["split"] == "dev"]

    embedder = GeminiQueryEmbedder(
        settings.gemini_api_key,
        model_name=settings.embedding_model,
        dimensions=settings.embedding_dimensions,
    )
    retriever = PgVectorDenseRetriever(
        settings.database_url,
        embedder,
        table_name=settings.pg_table,
        dimensions=settings.embedding_dimensions,
    )
    controller = GeminiController(
        settings.gemini_api_key,
        model_name=settings.agent_model,
    )

    traces = []
    for case in selected:
        trace = run_agent_case(
            case,
            controller,
            retriever,
            max_searches=4,
            top_k=3,
            budget=2400,
            use_case_filter=True,
        )
        traces.append(trace)
        print(
            f"[{trace['query_id']}] status={trace['status']} searches={trace['search_calls']} "
            f"citations={trace['citations']} tokens={trace['usage']['total_tokens']} "
            f"ms={trace['elapsed_ms']}"
        )
        print(f"  answer: {trace['answer'][:220]}")
        for idx, ev in enumerate(trace["events"], 1):
            if ev.get("event") == "search":
                hits = [f"{r['id']}({r['score']:.3f})" for r in ev["results"]]
                print(f"  search#{idx}: query={ev['query']!r} filter={ev['filter']} -> hits={hits} | ctx={ev['context_ids']}")

    out_path = REPO_ROOT / "results/cp2_smoke_traces.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(traces, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nSaved full traces to {out_path}")


if __name__ == "__main__":
    main()
