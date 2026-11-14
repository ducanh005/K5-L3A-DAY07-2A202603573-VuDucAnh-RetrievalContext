"""Build CP1 Day 7 dataset & benchmark files from Day 6 Strategy B chunks."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
STARTER_DIR = REPO_ROOT / "starter"
if str(STARTER_DIR) not in sys.path:
    sys.path.insert(0, str(STARTER_DIR))

from baseline import validate  # noqa: E402
from convert_day6 import convert_chunk, convert_question  # noqa: E402
from src.config import DAY6_ROOT  # noqa: E402

# Day 6 Strategy B normalized typography (curly apostrophe/quotes and en-dash),
# while Day 6 evidence_quote used ASCII punctuation in 4 dev items.
_QUOTE_FIXES = {
    "q05": ("system's context", "system’s context"),
    "q08": (
        '"what happened" in the system. Explainability can answer the question of "how" a decision was made in the system. Interpretability can answer the question of "why"',
        '“what happened” in the system. Explainability can answer the question of “how” a decision was made in the system. Interpretability can answer the question of “why”',
    ),
    "q12": ("will not - or cannot - be measured", "will not – or cannot – be measured"),
    "q16": ("model's outputs", "model’s outputs"),
}

FRESH_TEST_ANSWERABLE: list[dict[str, Any]] = [
    {
        "id": "t01",
        "type": "paraphrase",
        "split": "test",
        "question": "Why is using the NIST AI RMF alone insufficient for effective AI risk management, and what challenge can smaller organizations face?",
        "expected_answer": "Organizations must establish accountability mechanisms, roles and responsibilities, culture, and incentive structures backed by senior-level commitment; using the AI RMF alone does not create these incentives or cultural changes, and small to medium-sized organizations may face different challenges than large ones depending on capabilities and resources.",
        "gold": [
            {
                "source_id": "nist-ai-100-1",
                "page": 14,
                "evidence": "Organizations need to establish and maintain the appropriate accountability mechanisms, roles and responsibilities, culture, and incentive structures for risk management to be effective. Use of the AI RMF alone will not lead to these changes or provide the appropriate incentives. Effective risk management is realized through organizational commitment at senior levels and may require cultural change within an organization or industry. In addition, small to medium-sized organizations managing AI risks or implementing the AI RMF may face different challenges than large organizations, depending on their capabilities and resources.",
            }
        ],
    },
    {
        "id": "t02",
        "type": "dieu_kien_ngoai_le",
        "split": "test",
        "question": "Does the NIST AI RMF mandate a fixed template for AI RMF cross-sectoral profiles?",
        "expected_answer": "No. The NIST AI RMF does not prescribe profile templates, allowing for flexibility in implementation.",
        "gold": [
            {
                "source_id": "nist-ai-100-1",
                "page": 39,
                "evidence": "This Framework does not prescribe profile templates, allowing for flexibility in implementation.",
            }
        ],
    },
    {
        "id": "t03",
        "type": "truc_tiep",
        "split": "test",
        "question": "How do indirect prompt injection attacks differ from direct prompt injections in GAI systems, and what exploits have security researchers demonstrated?",
        "expected_answer": "Direct prompt injections input malicious prompts directly into a GAI system, whereas indirect prompt injection attacks remotely exploit LLM-integrated applications without a direct interface by injecting prompts into data likely to be retrieved; researchers have demonstrated exploiting vulnerabilities to steal proprietary data or run malicious code remotely.",
        "gold": [
            {
                "source_id": "nist-ai-600-1",
                "page": 15,
                "evidence": "In direct prompt injections, attackers might craft malicious prompts and input them directly to a GAI system, with a variety of downstream negative consequences to interconnected systems. Indirect prompt injection attacks occur when adversaries remotely (i.e., without a direct interface) exploit LLM-integrated applications by injecting prompts into data likely to be retrieved. Security researchers have already demonstrated how indirect prompt injections can exploit vulnerabilities by stealing proprietary data or running malicious code remotely on a machine.",
            }
        ],
    },
    {
        "id": "t04",
        "type": "truc_tiep",
        "split": "test",
        "question": "Under MEASURE 2.6 in NIST AI 600-1, what must be demonstrated about safety before deploying an AI system, and what do safety metrics reflect?",
        "expected_answer": "The system must be demonstrated to be safe with residual negative risk not exceeding risk tolerance and able to fail safely (especially beyond its knowledge limits); safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.",
        "gold": [
            {
                "source_id": "nist-ai-600-1",
                "page": 36,
                "evidence": "The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.",
            }
        ],
    },
    {
        "id": "t05",
        "type": "metadata_filter",
        "split": "test",
        "question": "In the 2023 AI RMF Core Framework under the Map function, what must be understood and documented under MAP 1.1?",
        "expected_answer": "Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective deployment settings for the AI system must be understood and documented.",
        "filter": {"year": 2023, "section": "map"},
        "gold": [
            {
                "source_id": "nist-ai-100-1",
                "page": 31,
                "evidence": "MAP 1.1: Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented.",
            }
        ],
    },
    {
        "id": "t06",
        "type": "metadata_filter",
        "split": "test",
        "question": "In the Generative AI Profile under the Manage function, what types of controls does MG-3.1-001 mention for applying organizational risk tolerances to third-party GAI resources?",
        "expected_answer": "Controls include acquisition and procurement processes, assessing personnel credentials and qualifications, performing background checks, filtering GAI inputs and outputs, grounding, fine tuning, and retrieval-augmented generation.",
        "filter": {"document_type": "generative_ai_profile", "section": "manage"},
        "gold": [
            {
                "source_id": "nist-ai-600-1",
                "page": 46,
                "evidence": "Apply organizational risk tolerances and controls (e.g., acquisition and procurement processes; assessing personnel credentials and qualifications, performing background checks; filtering GAI input and outputs, grounding, fine tuning, retrieval-augmented generation) to third-party GAI resources",
            }
        ],
    },
]

UNANSWERABLE_CASES: list[dict[str, Any]] = [
    {
        "id": "u_dev_01",
        "split": "dev",
        "question": "Under the NIST AI RMF 1.0 or Generative AI Profile, what exact maximum administrative fine or percentage of global annual turnover is specified as a statutory penalty for non-compliance?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "Checked all 48 physical pages of NIST.AI.100-1.pdf and 64 physical pages of NIST.AI.600-1.pdf: terms 'administrative fine', 'global turnover', 'statutory penalty', 'penalty', 'fines', 'non-compliance', and 'percentage' occur 0 times. NIST AI RMF is voluntary and defines no monetary fines.",
    },
    {
        "id": "u_dev_02",
        "split": "dev",
        "question": "What minimum benchmark accuracy percentage (such as an MMLU or SWE-bench score) does NIST AI 100-1 or NIST AI 600-1 mandate before deploying a generative AI model in production?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "Checked all physical pages of both PDFs: 'mmlu', 'swe-bench', and 'percentage' occur 0 times; all 14 mentions of 'benchmark' discuss qualitative benchmark selection, label errors, or bias evaluation (e.g., MS-2.3-001, MS-2.11-001) without any numeric accuracy cutoff.",
    },
    {
        "id": "u_test_01",
        "split": "test",
        "question": "How does NIST AI 600-1 prescribe aligning its suggested actions with EU AI Act Article 5 prohibited AI practices and ISO/IEC 42001 certification audit requirements?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "Checked all physical pages of both PDFs: 'eu ai act', 'article 5', '42001', 'prohibited ai', and 'certification audit' occur 0 times.",
    },
    {
        "id": "u_test_02",
        "split": "test",
        "question": "What specific GPU cluster power cap (in megawatts or kilowatt-hours) or cooling water budget (in liters per token) is required by NIST AI 600-1 for foundation model training?",
        "answerable": False,
        "expected_behavior": "search_and_abstain",
        "absence_reason": "Checked all physical pages of both PDFs: 'gpu', 'megawatt', and 'kilowatt' occur 0 times; 'liter' only appears in 'literacy' (p.37) and 'Literature' (p.59), and 'watt' only in an excluded bibliography citation (p.60). While MS-2.12-003 suggests measuring energy/water consumption, no numeric caps are specified.",
    },
]


def main() -> None:
    raw_chunks = json.loads((DAY6_ROOT / "results/chunks_B.json").read_text(encoding="utf-8"))
    chunks = [convert_chunk(c) for c in raw_chunks]

    raw_qs = json.loads((DAY6_ROOT / "benchmark/questions.json").read_text(encoding="utf-8"))["questions"]
    dev_answerable: list[dict[str, Any]] = []
    for raw_q in raw_qs:
        if raw_q.get("split") != "dev":
            continue
        q = convert_question(raw_q)
        if q["id"] in _QUOTE_FIXES:
            old, new = _QUOTE_FIXES[q["id"]]
            ev = q["gold"][0]["evidence"]
            assert old in ev, f"Expected snippet not found in {q['id']}"
            q["gold"][0]["evidence"] = ev.replace(old, new)
        dev_answerable.append(q)

    all_answerable = dev_answerable + FRESH_TEST_ANSWERABLE
    validate(chunks, [q for q in all_answerable if q["split"] == "dev"])
    validate(chunks, [q for q in all_answerable if q["split"] == "test"])

    agent_cases: list[dict[str, Any]] = []
    for q in all_answerable:
        item: dict[str, Any] = {
            "id": q["id"],
            "split": q["split"],
            "question": q["question"],
            "answerable": True,
            "expected_behavior": "search_and_answer",
        }
        if "filter" in q:
            item["filter"] = q["filter"]
        agent_cases.append(item)
    agent_cases.extend(UNANSWERABLE_CASES)

    data_dir = REPO_ROOT / "data"
    (data_dir / "chunks.json").write_text(
        json.dumps(chunks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (data_dir / "questions_answerable.json").write_text(
        json.dumps(all_answerable, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (data_dir / "agent_cases.json").write_text(
        json.dumps(agent_cases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    summary = {
        "chunks": len(chunks),
        "dev_answerable": sum(1 for q in all_answerable if q["split"] == "dev"),
        "dev_unanswerable": sum(1 for c in UNANSWERABLE_CASES if c["split"] == "dev"),
        "test_answerable": sum(1 for q in all_answerable if q["split"] == "test"),
        "test_unanswerable": sum(1 for c in UNANSWERABLE_CASES if c["split"] == "test"),
        "total_cases": len(agent_cases),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
