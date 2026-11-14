"""Print concise human-audit sheets for Agent traces against benchmark references."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Print human-readable audit view for a run's traces.")
    parser.add_argument("--traces", required=True, type=Path)
    parser.add_argument("--split", required=True, choices=("dev", "test"))
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    traces = json.loads(args.traces.read_text(encoding="utf-8"))
    cases = {
        c["id"]: c
        for c in json.loads((REPO_ROOT / "data/agent_cases.json").read_text(encoding="utf-8"))
        if c["split"] == args.split
    }
    answerable_ref = {
        q["id"]: q
        for q in json.loads((REPO_ROOT / "data/questions_answerable.json").read_text(encoding="utf-8"))
        if q["split"] == args.split
    }
    chunks = {
        c["id"]: c
        for c in json.loads((REPO_ROOT / "data/chunks.json").read_text(encoding="utf-8"))
    }

    lines: list[str] = [f"# Audit Worksheet ({args.split}) — `{args.traces}`\n"]
    for t in traces:
        qid = t["query_id"]
        c = cases[qid]
        lines.append(f"## {qid} (`answerable={c['answerable']}`, `status={t['status']}`, `searches={t['search_calls']}`)")
        lines.append(f"- **Question:** {c['question']}")
        if c["answerable"]:
            ref = answerable_ref[qid]
            lines.append(f"- **Expected Answer:** {ref['expected_answer']}")
            lines.append(f"- **Gold:** {ref['gold']}")
        else:
            lines.append(f"- **Absence Reason:** {c.get('absence_reason', '')}")
        lines.append(f"- **Agent Answer:** {t['answer']}")
        lines.append(f"- **Citations:** {t['citations']}")
        for cid in t["citations"]:
            ch = chunks.get(cid)
            snippet = ch["text"] if ch else "(MISSING FROM CHUNKS)"
            lines.append(f"  - Cited `[{cid}]` (p.{ch['page'] if ch else '?'}): {snippet}")
        if t.get("error"):
            lines.append(f"- **Error:** {t['error']}")
        lines.append("")

    report = "\n".join(lines)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report + "\n", encoding="utf-8")
        print(f"Wrote audit worksheet to {args.out}")
    else:
        print(report)


if __name__ == "__main__":
    main()
