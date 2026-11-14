"""Offline unit tests for Day 7 CP3 components (BM25, Hybrid RRF, Reranker)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.agent import GeminiController, pack_context_smart, run_agent_case  # noqa: E402
from src.retrievers import (  # noqa: E402
    Bm25Retriever,
    GeminiRerankRetriever,
    HybridRrfRetriever,
)

CHUNKS = [
    {
        "id": "c1",
        "source_id": "doc-a",
        "source": "a.pdf",
        "page": 1,
        "text": "MEASURE 1.1: Risks that cannot be measured are documented.",
        "metadata": {"year": 2023, "section": "measure"},
    },
    {
        "id": "c2",
        "source_id": "doc-a",
        "source": "a.pdf",
        "page": 2,
        "text": "MEASURE 1.3: External experts participate in risk assessments.",
        "metadata": {"year": 2023, "section": "measure"},
    },
    {
        "id": "c3",
        "source_id": "doc-b",
        "source": "b.pdf",
        "page": 5,
        "text": "GOVERN 1.2: Transparency policies balance proprietary models.",
        "metadata": {"year": 2024, "section": "govern"},
    },
]


class _FakeDense:
    strategy_name = "fake_dense"

    def search(self, query, *, filters=None, top_k=3):
        # Intentionally rank c2 ahead of c1 to test RRF fusion with BM25
        order = [
            {**CHUNKS[1], "score": 0.80, "strategy": self.strategy_name},
            {**CHUNKS[0], "score": 0.78, "strategy": self.strategy_name},
            {**CHUNKS[2], "score": 0.40, "strategy": self.strategy_name},
        ]
        if filters and filters.get("year") == 2023:
            order = [c for c in order if c["metadata"]["year"] == 2023]
        return order[:top_k]


class _FakeRerankClient:
    def __init__(self, ranked_ids):
        self._ranked_ids = ranked_ids
        self.models = self

    def generate_content(self, *, model, contents, config):
        import json

        return SimpleNamespace(
            text=json.dumps({"ranked_ids": self._ranked_ids}),
            usage_metadata=SimpleNamespace(
                prompt_token_count=100,
                candidates_token_count=15,
                thoughts_token_count=0,
                total_token_count=115,
            ),
        )


class CP3RetrieverTests(unittest.TestCase):
    def test_bm25_finds_exact_identifier_and_respects_filter(self):
        bm25 = Bm25Retriever(CHUNKS)
        hits = bm25.search("MEASURE 1.1 cannot be measured", filters={"year": 2023}, top_k=3)
        self.assertEqual(hits[0]["id"], "c1")
        self.assertEqual(hits[0]["strategy"], "bm25")
        self.assertTrue(all(h["metadata"]["year"] == 2023 for h in hits))

    def test_hybrid_rrf_fuses_ranks_without_raw_score_bias(self):
        bm25 = Bm25Retriever(CHUNKS)
        hybrid = HybridRrfRetriever(_FakeDense(), bm25, candidate_k=3, rrf_k=60)
        hits = hybrid.search("MEASURE 1.1 documented", filters={"year": 2023}, top_k=2)
        # c1 is #1 in BM25 and #2 in dense -> highest combined RRF
        self.assertEqual(hits[0]["id"], "c1")
        self.assertEqual(hits[0]["dense_rank"], 2)
        self.assertEqual(hits[0]["lexical_rank"], 1)

    def test_gemini_reranker_reorders_candidates_and_tracks_tokens(self):
        bm25 = Bm25Retriever(CHUNKS)
        reranker = GeminiRerankRetriever(
            bm25, api_key="", client=_FakeRerankClient(["c2", "c1"]), candidate_k=3
        )
        hits = reranker.search("MEASURE assessment", top_k=2)
        self.assertEqual([h["id"] for h in hits], ["c2", "c1"])
        self.assertEqual(reranker.stats["total_tokens"], 115)

    def test_pack_context_smart_evicts_stale_turn1_when_turn2_rank1_arrives(self):
        c_turn1_r1 = {**CHUNKS[1], "text": "A" * 100, "_best_rank": 1, "_last_turn": 1, "score": 0.9}
        c_turn1_r2 = {**CHUNKS[2], "text": "B" * 100, "_best_rank": 2, "_last_turn": 1, "score": 0.8}
        c_turn2_r1 = {**CHUNKS[0], "text": "C" * 100, "_best_rank": 1, "_last_turn": 2, "score": 0.7}
        # Budget fits ~2 chunks (~290 chars), so turn2 rank1 must beat turn1 rank2!
        ctx, ids = pack_context_smart([c_turn1_r1, c_turn1_r2, c_turn2_r1], budget=290)
        self.assertIn("c1", ids)
        self.assertIn("c2", ids)
        self.assertNotIn("c3", ids)

    def test_smart_mode_disables_search_when_remaining_searches_zero(self):
        calls = []

        class _SearchThenSubmitClient:
            def __init__(self):
                self.models = self
                self.n = 0

            def generate_content(self, *, model, contents, config):
                self.n += 1
                allowed = config.tool_config.function_calling_config.allowed_function_names
                calls.append(list(allowed))
                if self.n == 1:
                    return SimpleNamespace(
                        function_calls=[SimpleNamespace(name="search_documents", args={"query": "MEASURE 1.1"})],
                        usage_metadata=SimpleNamespace(prompt_token_count=10, candidates_token_count=5, thoughts_token_count=0, total_token_count=15),
                    )
                return SimpleNamespace(
                    function_calls=[SimpleNamespace(name="submit_answer", args={"sufficient_evidence": True, "answer": "Ok [c1]", "citations": ["c1"]})],
                    usage_metadata=SimpleNamespace(prompt_token_count=20, candidates_token_count=5, thoughts_token_count=0, total_token_count=25),
                )

        ctrl = GeminiController(api_key="", client=_SearchThenSubmitClient())
        bm25 = Bm25Retriever(CHUNKS)
        case = {"id": "s1", "split": "dev", "question": "MEASURE 1.1?", "answerable": True}
        trace = run_agent_case(case, ctrl, bm25, max_searches=1, budget=500, context_mode="smart")
        self.assertEqual(trace["status"], "answered")
        self.assertEqual(calls, [["search_documents"], ["submit_answer"]])


if __name__ == "__main__":
    unittest.main()
