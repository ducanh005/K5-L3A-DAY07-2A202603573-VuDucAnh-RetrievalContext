"""Offline unit tests for Day 7 CP2 components (retriever helpers & controller logic)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.agent import GeminiController, run_agent_case  # noqa: E402
from src.retrievers import TfidfRetriever, _build_pg_filter_sql, matches_filter  # noqa: E402

SAMPLE_CHUNKS = [
    {
        "id": "c1",
        "source_id": "doc-2023",
        "source": "doc1.pdf",
        "page": 6,
        "text": "Risk measurement starts with significant AI risks.",
        "metadata": {"year": 2023, "section": "measure"},
    },
    {
        "id": "c2",
        "source_id": "doc-2024",
        "source": "doc2.pdf",
        "page": 18,
        "text": "Generative AI risk measurement requires transparency.",
        "metadata": {"year": 2024, "section": "govern"},
    },
]


class _FakeModels:
    def __init__(self, responses):
        self._iter = iter(responses)
        self.calls = []

    def generate_content(self, *, model, contents, config):
        self.calls.append((model, contents, config))
        return next(self._iter)


class _FakeClient:
    def __init__(self, responses):
        self.models = _FakeModels(responses)


def _fc_response(name: str, args: dict):
    return SimpleNamespace(
        function_calls=[SimpleNamespace(name=name, args=args)],
        usage_metadata=SimpleNamespace(
            prompt_token_count=100,
            candidates_token_count=20,
            thoughts_token_count=5,
            total_token_count=125,
        ),
    )


class CP2Tests(unittest.TestCase):
    def test_tfidf_retriever_respects_metadata_filter(self):
        ret = TfidfRetriever(SAMPLE_CHUNKS)
        hits = ret.search("risk measurement", filters={"year": 2024}, top_k=3)
        self.assertEqual([h["id"] for h in hits], ["c2"])
        self.assertEqual(hits[0]["strategy"], "tfidf")

    def test_pg_filter_sql_translates_source_id_and_rejects_unknown(self):
        clauses, params = _build_pg_filter_sql({"source_id": "nist-ai-100-1", "year": 2023})
        self.assertEqual(clauses, ["document_id = %s", "year = %s"])
        self.assertEqual(params, ["nist-ai-100-1", 2023])
        with self.assertRaises(ValueError):
            matches_filter(SAMPLE_CHUNKS[0], {"unknown_field": "x"})

    def test_gemini_controller_search_then_cited_answer(self):
        client = _FakeClient([
            _fc_response("search_documents", {"query": "risk measurement", "reason": "find measure"}),
            _fc_response(
                "submit_answer",
                {
                    "sufficient_evidence": True,
                    "answer": "Measurement starts with significant AI risks [c1].",
                    "citations": ["c1"],
                },
            ),
        ])
        ctrl = GeminiController(api_key="", client=client)
        ret = TfidfRetriever(SAMPLE_CHUNKS)
        case = {"id": "t1", "split": "dev", "question": "Where does measurement start?", "answerable": True}
        trace = run_agent_case(case, ctrl, ret, budget=1000)
        self.assertEqual(trace["status"], "answered")
        self.assertEqual(trace["citations"], ["c1"])
        self.assertEqual(trace["search_calls"], 1)
        self.assertEqual(trace["usage"]["total_tokens"], 250)
        self.assertEqual(
            client.models.calls[0][2].tool_config.function_calling_config.allowed_function_names,
            ["search_documents"],
        )

    def test_gemini_controller_intentional_abstain_clears_citations(self):
        client = _FakeClient([
            _fc_response("search_documents", {"query": "administrative fine"}),
            _fc_response(
                "submit_answer",
                {
                    "sufficient_evidence": False,
                    "answer": "No evidence found.",
                    "citations": ["c1"],
                },
            ),
        ])
        ctrl = GeminiController(api_key="", client=client)
        ret = TfidfRetriever(SAMPLE_CHUNKS)
        case = {"id": "u1", "split": "dev", "question": "What is the fine?", "answerable": False}
        trace = run_agent_case(case, ctrl, ret, budget=1000)
        self.assertEqual(trace["status"], "abstain")
        self.assertEqual(trace["citations"], [])
        self.assertEqual(trace["turns"][-1]["decision_kind"], "abstain")


if __name__ == "__main__":
    unittest.main()
