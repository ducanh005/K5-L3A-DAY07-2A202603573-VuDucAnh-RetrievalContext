"""Multimodal and text-only retrievers over the indexed 186-page IPCC AR6 SYR corpus."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np

from src.advanced.catalog import ADV_INDEX_DIR
from src.embeddings import GeminiQueryEmbedder
from src.retrievers import Bm25Retriever

ALL_MODALITIES = frozenset({"text", "table", "chart", "diagram_map"})
VISUAL_MODALITIES = frozenset({"table", "chart", "diagram_map"})


def _resolve_allowed_modalities(modality: str | None, *, allow_visual: bool) -> frozenset[str]:
    if not allow_visual:
        if modality and modality not in ("all", "text"):
            return frozenset()
        return frozenset({"text"})
    if modality is None or modality == "all":
        return ALL_MODALITIES
    if modality == "visual":
        return VISUAL_MODALITIES
    if modality in ALL_MODALITIES:
        return frozenset({modality})
    raise ValueError(f"Unsupported modality filter: {modality!r}")


class AdvancedCorpus:
    """In-memory multimodal index combining text chunks, structured visual cards, and embeddings."""

    def __init__(self, index_dir: Path | None = None) -> None:
        base = index_dir or ADV_INDEX_DIR
        self.elements: list[dict[str, Any]] = json.loads((base / "elements.json").read_text(encoding="utf-8"))
        self.id_to_idx: dict[str, int] = {el["id"]: idx for idx, el in enumerate(self.elements)}
        self.id_to_element: dict[str, dict[str, Any]] = {el["id"]: el for el in self.elements}

        npz = np.load(base / "embeddings.npz")
        self.text_embeddings: np.ndarray = np.asarray(npz["text_embeddings"], dtype=np.float32)
        self.image_embeddings: np.ndarray = np.asarray(npz["image_embeddings"], dtype=np.float32)
        self.image_indices: np.ndarray = np.asarray(npz["image_indices"], dtype=np.int32)
        self.idx_to_img_row: dict[int, int] = {
            int(el_idx): row_idx for row_idx, el_idx in enumerate(self.image_indices.tolist())
        }

        self.bm25 = Bm25Retriever(self.elements, strategy_name="adv_bm25")


class AdvancedHybridRetriever:
    """Configurable text-only or 3-way cross-modal RRF retriever (BM25 + dense text + dense image)."""

    def __init__(
        self,
        corpus: AdvancedCorpus,
        embedder: GeminiQueryEmbedder | None,
        *,
        allow_visual: bool = True,
        use_dense_text: bool = True,
        use_dense_image: bool = True,
        candidate_k: int = 20,
        rrf_k: int = 60,
        strategy_name: str = "adv_multimodal_rrf",
    ) -> None:
        if (use_dense_text or (allow_visual and use_dense_image)) and embedder is None:
            raise ValueError("embedder is required when dense retrieval is enabled.")
        self.corpus = corpus
        self.embedder = embedder
        self.allow_visual = allow_visual
        self.use_dense_text = use_dense_text
        self.use_dense_image = allow_visual and use_dense_image
        self.candidate_k = max(5, candidate_k)
        self.rrf_k = max(1, rrf_k)
        self.strategy_name = strategy_name

    def search(
        self,
        query: str,
        *,
        modality: str | None = None,
        top_k: int = 5,
    ) -> list[dict[str, Any]]:
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query must be a non-empty string.")
        if top_k < 1:
            raise ValueError("top_k must be >= 1.")

        allowed = _resolve_allowed_modalities(modality, allow_visual=self.allow_visual)
        if not allowed:
            return []

        eligible_indices = [
            idx for idx, el in enumerate(self.corpus.elements) if el["modality"] in allowed
        ]
        if not eligible_indices:
            return []
        eligible_set = set(eligible_indices)

        # Stream 1: BM25 lexical rank
        bm25_hits = self.corpus.bm25.search(query, filters=None, top_k=len(self.corpus.elements))
        bm25_ids = [h["id"] for h in bm25_hits if self.corpus.id_to_idx[h["id"]] in eligible_set][
            : self.candidate_k
        ]

        # Embed query once for both text and image cosine matching in unified gemini-embedding-2 space.
        dense_text_ids: list[str] = []
        dense_image_ids: list[str] = []
        if self.use_dense_text or self.use_dense_image:
            assert self.embedder is not None
            q_vec = np.asarray(self.embedder.embed_query(query), dtype=np.float32)

            if self.use_dense_text:
                scores = self.corpus.text_embeddings @ q_vec
                ranked_idx = sorted(eligible_indices, key=lambda i: (-float(scores[i]), self.corpus.elements[i]["id"]))
                dense_text_ids = [self.corpus.elements[i]["id"] for i in ranked_idx[: self.candidate_k]]

            if self.use_dense_image and len(self.corpus.image_indices) > 0:
                img_scores = self.corpus.image_embeddings @ q_vec
                img_candidates = [
                    (float(img_scores[row_idx]), int(el_idx))
                    for row_idx, el_idx in enumerate(self.corpus.image_indices.tolist())
                    if el_idx in eligible_set
                ]
                img_candidates.sort(key=lambda pair: (-pair[0], self.corpus.elements[pair[1]]["id"]))
                dense_image_ids = [
                    self.corpus.elements[el_idx]["id"] for _, el_idx in img_candidates[: self.candidate_k]
                ]

        fused: dict[str, float] = defaultdict(float)
        streams: dict[str, dict[str, int]] = defaultdict(dict)
        for stream_name, ranked_ids in (
            ("bm25", bm25_ids),
            ("dense_text", dense_text_ids),
            ("dense_image", dense_image_ids),
        ):
            for rank, eid in enumerate(ranked_ids, 1):
                fused[eid] += 1.0 / (self.rrf_k + rank)
                streams[eid][stream_name] = rank

        ordered_ids = sorted(fused, key=lambda eid: (-fused[eid], eid))[:top_k]
        out: list[dict[str, Any]] = []
        for eid in ordered_ids:
            el = self.corpus.id_to_element[eid]
            out.append({
                **el,
                "score": float(fused[eid]),
                "stream_ranks": streams[eid],
                "strategy": self.strategy_name,
            })
        return out
