"""Offline unit and integration checks for src.advanced multimodal RAG modules."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.advanced.agent import pack_multimodal_context, run_advanced_case  # noqa: E402
from src.advanced.catalog import (  # noqa: E402
    VISUAL_REGION_SPECS,
    crop_filename,
    infer_section,
    pdf_to_printed_page,
)
from src.advanced.eval_adv import score_reviews  # noqa: E402
from src.advanced.ingest import _split_page_text  # noqa: E402
from src.advanced.retrievers import AdvancedCorpus, AdvancedHybridRetriever  # noqa: E402


class _FakeEmbedder:
    def __init__(self, vec: list[float]) -> None:
        self.vec = vec

    def embed_query(self, text: str) -> list[float]:
        return list(self.vec)


class _FakeController:
    def __init__(self, actions: list[dict], *, enable_vision_inspect: bool = True) -> None:
        self.model_name = "gemini-3.8-flash"
        self.enable_vision_inspect = enable_vision_inspect
        self.turns: list[dict] = []
        self._actions = iter(actions)

    def reset_trace(self) -> None:
        self.turns = []

    def decide(self, question: str, state: dict | None, inspected_visuals: list[dict]) -> dict:
        action = next(self._actions)
        self.turns.append({
            "turn": len(self.turns) + 1,
            "function_name": action["action"],
            "attached_visuals": [v["region_id"] for v in inspected_visuals],
            "prompt_tokens": 100,
            "candidates_tokens": 20,
            "thoughts_tokens": 5,
            "total_tokens": 125,
        })
        return action


class _FakeRetriever:
    def __init__(self, results_by_turn: list[list[dict]], *, strategy_name: str = "fake_rrf") -> None:
        self.strategy_name = strategy_name
        self._iter = iter(results_by_turn)
        self.calls: list[tuple[str, str | None, int]] = []

    def search(self, query: str, *, modality: str | None = None, top_k: int = 5) -> list[dict]:
        self.calls.append((query, modality, top_k))
        return next(self._iter)


class TestAdvancedCatalogAndIngest(unittest.TestCase):
    def test_catalog_metadata_and_page_mapping(self) -> None:
        self.assertEqual(len(VISUAL_REGION_SPECS), 37)
        region_ids = [s.region_id for s in VISUAL_REGION_SPECS]
        self.assertEqual(len(region_ids), len(set(region_ids)))
        for spec in VISUAL_REGION_SPECS:
            self.assertIn(spec.modality, {"table", "chart", "diagram_map"})
            self.assertGreaterEqual(spec.pdf_page, 1)
            self.assertLessEqual(spec.pdf_page, 186)

        self.assertEqual(pdf_to_printed_page(1), "cover")
        self.assertEqual(pdf_to_printed_page(2), "frontmatter")
        self.assertEqual(pdf_to_printed_page(3), "i")
        self.assertEqual(pdf_to_printed_page(16), "xiv")
        self.assertEqual(pdf_to_printed_page(17), "1")
        self.assertEqual(pdf_to_printed_page(63), "47")
        self.assertEqual(pdf_to_printed_page(186), "back_cover")

        self.assertEqual(infer_section(23, ""), "Summary for Policymakers")
        self.assertEqual(infer_section(63, ""), "Section 2: Current Status and Trends")
        self.assertEqual(infer_section(100, ""), "Section 3: Long-Term Futures")
        self.assertEqual(infer_section(129, ""), "Section 4: Near-Term Responses")
        self.assertEqual(infer_section(140, ""), "Annex I: Glossary")
        self.assertEqual(crop_filename("VIS:Table_2_1:p063"), "VIS_Table_2_1_p063.png")

    def test_split_page_text_preserves_words_and_overlap(self) -> None:
        para = " ".join(f"word{i}" for i in range(90))
        chunks = _split_page_text(f"{para}\n\n{para}", max_chars=260, overlap=40)
        self.assertGreaterEqual(len(chunks), 3)
        for ch in chunks:
            self.assertLessEqual(len(ch), 260)


class TestAdvancedRetrievers(unittest.TestCase):
    def _build_temp_corpus(self, tmp_dir: Path) -> AdvancedCorpus:
        elements = [
            {
                "id": "ADV_TXT:p058:c01",
                "modality": "text",
                "label": "Section 2.1 text",
                "pdf_page": 58,
                "printed_page": "42",
                "section": "Section 2",
                "bbox": [0.0, 0.0, 612.0, 792.0],
                "text": "Observed global surface temperature warming was 1.1C in 2011-2020.",
                "has_visual_embedding": False,
            },
            {
                "id": "ADV_TXT:p098:c01",
                "modality": "text",
                "label": "Section 3.3.1 text",
                "pdf_page": 98,
                "printed_page": "82",
                "section": "Section 3",
                "bbox": [0.0, 0.0, 612.0, 792.0],
                "text": "Remaining carbon budget from 2020 for 1.5C (50%) is 500 GtCO2.",
                "has_visual_embedding": False,
            },
            {
                "id": "VIS:Table_2_1:p063",
                "modality": "table",
                "label": "Table 2.1",
                "pdf_page": 63,
                "printed_page": "47",
                "section": "Section 2",
                "bbox": [45.0, 48.0, 565.0, 700.0],
                "text": "Color-coded matrix of human attribution for ice sheets and ocean warming.",
                "crop_relpath": "data/advanced/crops/VIS_Table_2_1_p063.png",
                "has_visual_embedding": True,
            },
            {
                "id": "VIS:Figure_3_4:p096",
                "modality": "chart",
                "label": "Figure 3.4",
                "pdf_page": 96,
                "printed_page": "80",
                "section": "Section 3",
                "bbox": [45.0, 50.0, 565.0, 750.0],
                "text": "Sea level rise observations and projections through 2300.",
                "crop_relpath": "data/advanced/crops/VIS_Figure_3_4_p096.png",
                "has_visual_embedding": True,
            },
        ]
        (tmp_dir / "elements.json").write_text(json.dumps(elements), encoding="utf-8")
        text_emb = np.array(
            [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.2, 0.0, 0.98, 0.0],
                [0.0, 0.1, 0.0, 0.995],
            ],
            dtype=np.float32,
        )
        img_emb = np.array(
            [
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
            ],
            dtype=np.float32,
        )
        img_idx = np.array([2, 3], dtype=np.int32)
        np.savez_compressed(
            tmp_dir / "embeddings.npz",
            text_embeddings=text_emb,
            image_embeddings=img_emb,
            image_indices=img_idx,
        )
        return AdvancedCorpus(tmp_dir)

    def test_text_only_vs_multimodal_3way_rrf(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            corpus = self._build_temp_corpus(Path(td))
            embedder = _FakeEmbedder([0.0, 0.0, 1.0, 0.0])

            txt_only = AdvancedHybridRetriever(
                corpus, embedder, allow_visual=False, use_dense_text=True, use_dense_image=False
            )
            txt_hits = txt_only.search("ice sheets attribution color matrix", top_k=5)
            self.assertTrue(all(h["modality"] == "text" for h in txt_hits))
            self.assertEqual(txt_only.search("Table 2.1", modality="table", top_k=5), [])

            mm = AdvancedHybridRetriever(
                corpus, embedder, allow_visual=True, use_dense_text=True, use_dense_image=True
            )
            mm_hits = mm.search("ice sheets attribution color matrix", top_k=2)
            self.assertEqual(mm_hits[0]["id"], "VIS:Table_2_1:p063")
            self.assertIn("bm25", mm_hits[0]["stream_ranks"])
            self.assertIn("dense_text", mm_hits[0]["stream_ranks"])
            self.assertIn("dense_image", mm_hits[0]["stream_ranks"])

            chart_hits = mm.search("sea level", modality="chart", top_k=3)
            self.assertEqual([h["id"] for h in chart_hits], ["VIS:Figure_3_4:p096"])


class TestMultimodalAgentAndScorer(unittest.TestCase):
    def test_pack_multimodal_context_dedups_and_collects_visuals(self) -> None:
        c_vis = {
            "id": "VIS:Table_2_1:p063",
            "modality": "table",
            "label": "Table 2.1",
            "printed_page": "47",
            "pdf_page": 63,
            "bbox": [45, 48, 565, 700],
            "text": "Attribution matrix " * 10,
            "_best_rank": 1,
            "_last_turn": 1,
            "score": 0.9,
        }
        c_txt = {
            "id": "ADV_TXT:p063:c01",
            "modality": "text",
            "label": "Section 2 text",
            "printed_page": "47",
            "pdf_page": 63,
            "bbox": [0, 0, 612, 792],
            "text": "Narrative explanation " * 10,
            "_best_rank": 2,
            "_last_turn": 1,
            "score": 0.7,
        }
        ctx, ids, vis_ids = pack_multimodal_context([c_txt, c_vis, {**c_txt, "_best_rank": 1}], budget=1200)
        self.assertEqual(ids.count("ADV_TXT:p063:c01"), 1)
        self.assertEqual(vis_ids, ["VIS:Table_2_1:p063"])
        self.assertIn("VIS:Table_2_1:p063", ctx)

    def test_pack_multimodal_context_caps_oversized_cards_for_multi_region_budget(self) -> None:
        big_a = {
            "id": "VIS:Figure_2_2_charts:p061",
            "modality": "chart",
            "label": "Figure 2.2 Panels a-c",
            "printed_page": "45",
            "pdf_page": 61,
            "bbox": [42, 45, 575, 582],
            "text": "Chart details " * 400,  # ~5,600 chars
            "_best_rank": 1,
            "_last_turn": 1,
            "score": 0.9,
        }
        big_b = {
            "id": "VIS:Table_Fig2_2d:p061",
            "modality": "table",
            "label": "Figure 2.2 Panel d",
            "printed_page": "45",
            "pdf_page": 61,
            "bbox": [42, 585, 575, 755],
            "text": "Regional indicator table " * 160,  # ~4,000 chars
            "_best_rank": 1,
            "_last_turn": 2,
            "score": 0.89,
        }
        ctx, ids, vis_ids = pack_multimodal_context([big_a, big_b], budget=7000)
        self.assertEqual(set(ids), {"VIS:Figure_2_2_charts:p061", "VIS:Table_Fig2_2d:p061"})
        self.assertEqual(set(vis_ids), {"VIS:Figure_2_2_charts:p061", "VIS:Table_Fig2_2d:p061"})
        self.assertLessEqual(len(ctx), 7000)

        card_with_ocr = {
            **big_a,
            "text": "Title: Fig\nSummary: Overview\nExtracted Details:\nWrong 2 dots here",
        }
        ctx_stripped, _, _ = pack_multimodal_context(
            [card_with_ocr], budget=7000, inspected_ids={"VIS:Figure_2_2_charts:p061"}
        )
        self.assertNotIn("Wrong 2 dots here", ctx_stripped)
        self.assertIn("Overview", ctx_stripped)

    def test_run_advanced_case_loads_png_and_enforces_citations(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            crop_rel = "tmp_test_crop.png"
            (root / crop_rel).write_bytes(b"\x89PNG\r\n\x1a\nfakepng")

            el_vis = {
                "id": "VIS:Table_2_1:p063",
                "modality": "table",
                "label": "Table 2.1",
                "pdf_page": 63,
                "printed_page": "47",
                "section": "Section 2",
                "bbox": [45.0, 48.0, 565.0, 700.0],
                "text": "Summary",
                "crop_relpath": crop_rel,
            }

            class _MiniCorpus:
                def __init__(self) -> None:
                    self.id_to_element = {"VIS:Table_2_1:p063": el_vis}

            corpus = _MiniCorpus()
            from unittest.mock import patch

            with patch("src.advanced.agent.REPO_ROOT", root):
                case = {
                    "id": "adv_dev_test",
                    "split": "dev",
                    "category": "table",
                    "question": "What is shown in Table 2.1?",
                    "answerable": True,
                }
                retriever = _FakeRetriever([[{**el_vis, "score": 0.85, "stream_ranks": {"dense_image": 1}}]])
                controller = _FakeController([
                    {"action": "search", "query": "Table 2.1", "modality": "table"},
                    {
                        "action": "inspect",
                        "region_id": "VIS:Table_2_1:p063",
                        "focus_question": "Read cell colors",
                    },
                    {
                        "action": "answer",
                        "sufficient": True,
                        "answer": "Greenland ice sheet is virtually certain [VIS:Table_2_1:p063].",
                        "citations": ["VIS:Table_2_1:p063"],
                    },
                ])
                trace = run_advanced_case(case, controller, retriever, corpus)
                self.assertEqual(trace["status"], "answered")
                self.assertEqual(trace["inspected_regions"], ["VIS:Table_2_1:p063"])
                self.assertEqual(trace["citations"], ["VIS:Table_2_1:p063"])
                self.assertEqual(trace["inspect_calls"], 1)

                # Grouped bracket citation format `[ID1, ID2]` is accepted
                el_txt = {
                    "id": "ADV_TXT:p063:c01",
                    "modality": "text",
                    "label": "Section 2.1",
                    "pdf_page": 63,
                    "printed_page": "47",
                    "section": "Section 2",
                    "bbox": [0.0, 0.0, 612.0, 792.0],
                    "text": "Cryosphere narrative.",
                    "crop_relpath": None,
                }
                corpus.id_to_element["ADV_TXT:p063:c01"] = el_txt
                grouped_controller = _FakeController([
                    {"action": "search", "query": "Table 2.1", "modality": "all"},
                    {
                        "action": "inspect",
                        "region_id": "VIS:Table_2_1:p063",
                        "focus_question": "Read cell colors",
                    },
                    {
                        "action": "answer",
                        "sufficient": True,
                        "answer": "Greenland ice sheet is virtually certain [VIS:Table_2_1:p063, ADV_TXT:p063:c01].",
                        "citations": ["VIS:Table_2_1:p063", "ADV_TXT:p063:c01"],
                    },
                ])
                grouped_retriever = _FakeRetriever([[
                    {**el_vis, "score": 0.85, "stream_ranks": {"dense_image": 1}},
                    {**el_txt, "score": 0.80, "stream_ranks": {"bm25": 1}},
                ]])
                grouped_trace = run_advanced_case(case, grouped_controller, grouped_retriever, corpus)
                self.assertEqual(grouped_trace["status"], "answered")
                self.assertEqual(grouped_trace["citations"], ["VIS:Table_2_1:p063", "ADV_TXT:p063:c01"])

                # Invalid inline bracket causes deterministic abstention
                bad_controller = _FakeController([
                    {"action": "search", "query": "Table 2.1", "modality": "all"},
                    {
                        "action": "answer",
                        "sufficient": True,
                        "answer": "Answer missing bracket.",
                        "citations": ["VIS:Table_2_1:p063"],
                    },
                ])
                bad_retriever = _FakeRetriever([[{**el_vis, "score": 0.5, "stream_ranks": {"bm25": 1}}]])
                bad_trace = run_advanced_case(case, bad_controller, bad_retriever, corpus)
                self.assertEqual(bad_trace["status"], "abstain")
                self.assertEqual(bad_trace["citations"], [])

    def test_score_reviews_unrounded_90pct_and_error_guards(self) -> None:
        cases = [{"id": f"q{i}", "category": "table" if i < 5 else "unanswerable"} for i in range(10)]
        traces = [
            {"query_id": f"q{i}", "status": "answered", "error": None, "search_calls": 1, "inspect_calls": 1, "usage": {"total_tokens": 100}, "elapsed_ms": 500.0}
            for i in range(10)
        ]
        reviews = [{"query_id": f"q{i}", "passed": i < 9, "reason": "Verified against crop."} for i in range(10)]
        res = score_reviews(cases, traces, reviews)
        self.assertTrue(res["meets_90pct_bar"])
        self.assertEqual(res["pass_rate_pct"], 90.0)

        # 8/9 = 88.89% must NOT meet 90% bar
        res_fail = score_reviews(cases[:9], traces[:9], [{"query_id": f"q{i}", "passed": i < 8, "reason": "ok"} for i in range(9)])
        self.assertFalse(res_fail["meets_90pct_bar"])
        self.assertEqual(res_fail["pass_rate_pct"], 88.89)

        # Provider error marked passed=True must raise ValueError
        err_traces = list(traces)
        err_traces[0] = {**traces[0], "status": "error", "error": "TimeoutError: 504"}
        with self.assertRaises(ValueError):
            score_reviews(cases, err_traces, reviews)


if __name__ == "__main__":
    unittest.main()
