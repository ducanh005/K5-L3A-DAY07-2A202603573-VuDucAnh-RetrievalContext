"""Whole-document multimodal ingestion & indexing CLI for Advanced Day 7 track."""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
import pymupdf
from google import genai
from google.genai import types

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.advanced.catalog import (  # noqa: E402
    ADV_CROPS_DIR,
    ADV_DATA_DIR,
    ADV_INDEX_DIR,
    DOCUMENT_DOI,
    DOCUMENT_ID,
    DOCUMENT_ISBN,
    DOCUMENT_TITLE,
    DOCUMENT_URL,
    VISUAL_REGION_SPECS,
    ensure_pdf_downloaded,
    infer_section,
    pdf_to_printed_page,
    render_visual_crops,
)
from src.config import DEFAULT_AGENT_MODEL, load_settings  # noqa: E402
from src.embeddings import _extract_retry_seconds, _is_retryable_error, l2_normalize  # noqa: E402

MM_EMBED_MODEL = "gemini-embedding-2"
MM_EMBED_DIMS = 768
MANIFEST_PATH = ADV_DATA_DIR / "document_manifest.json"


def _split_page_text(text: str, *, max_chars: int = 1100, overlap: int = 120) -> list[str]:
    """Split normalized page text into overlapping chunks without breaking words."""
    clean = "\n".join(line.rstrip() for line in text.splitlines()).strip()
    if not clean:
        return []
    paragraphs = [p.strip() for p in clean.split("\n\n") if p.strip()]
    if len(paragraphs) <= 1:
        paragraphs = [line.strip() for line in clean.splitlines() if line.strip()]

    chunks: list[str] = []
    cur = ""
    for para in paragraphs:
        if len(para) > max_chars:
            if cur:
                chunks.append(cur.strip())
                cur = ""
            start = 0
            while start < len(para):
                end = min(len(para), start + max_chars)
                if end < len(para):
                    cut = para.rfind(" ", start + max_chars // 2, end)
                    if cut > start:
                        end = cut
                chunks.append(para[start:end].strip())
                if end >= len(para):
                    break
                start = max(start + 1, end - overlap)
            continue

        candidate = f"{cur}\n\n{para}" if cur else para
        if len(candidate) <= max_chars:
            cur = candidate
        else:
            chunks.append(cur.strip())
            tail = cur[-overlap:].lstrip() if overlap > 0 and len(cur) > overlap else ""
            if tail and " " in tail:
                tail = tail.split(" ", 1)[1]
            merged = f"{tail}\n\n{para}".strip() if tail else para
            cur = merged if len(merged) <= max_chars else para
    if cur.strip():
        chunks.append(cur.strip())
    return chunks


def extract_document_text_and_audit(pdf_path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Scan all 186 pages, chunk text on every non-blank page, and audit blank/special pages."""
    doc = pymupdf.open(pdf_path)
    text_elements: list[dict[str, Any]] = []
    skipped_blank_pages: list[dict[str, Any]] = []
    divider_or_cover_pages: list[dict[str, Any]] = []
    indexed_pages: list[int] = []

    for pdf_page, page in enumerate(doc, 1):
        raw_text = page.get_text().strip()
        imgs = len(page.get_images(full=True))
        draws = len(page.get_drawings())
        printed = pdf_to_printed_page(pdf_page)
        section = infer_section(pdf_page, raw_text)

        if len(raw_text) < 5 and imgs == 0 and draws <= 2:
            skipped_blank_pages.append({
                "pdf_page": pdf_page,
                "printed_page": printed,
                "section": section,
                "reason": "Blank spacer/transition page (0 extractable characters, no raster images or structural drawings).",
                "impact": "None — intentionally empty separator page before major sections.",
            })
            continue

        indexed_pages.append(pdf_page)
        if len(raw_text) < 120:
            divider_or_cover_pages.append({
                "pdf_page": pdf_page,
                "printed_page": printed,
                "section": section,
                "chars": len(raw_text),
                "note": "Cover or section-divider title page (indexed in full).",
            })

        pieces = _split_page_text(raw_text, max_chars=1100, overlap=120)
        for idx, body in enumerate(pieces, 1):
            cid = f"ADV_TXT:p{pdf_page:03d}:c{idx:02d}"
            text_elements.append({
                "id": cid,
                "modality": "text",
                "label": f"{section} (p.{printed})",
                "pdf_page": pdf_page,
                "printed_page": printed,
                "caption_page": pdf_page,
                "section": section,
                "bbox": [35.0, 35.0, 575.0, 760.0],
                "text": body,
                "source_id": DOCUMENT_ID,
            })

    audit = {
        "total_pdf_pages": len(doc),
        "indexed_pages_count": len(indexed_pages),
        "skipped_blank_pages_count": len(skipped_blank_pages),
        "skipped_blank_pages": skipped_blank_pages,
        "divider_or_cover_pages": divider_or_cover_pages,
        "total_text_chunks": len(text_elements),
    }
    return text_elements, audit


def _call_with_retry(fn: Any, *, max_retries: int = 5, base_delay: float = 2.0) -> Any:
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except Exception as exc:
            if attempt >= max_retries or not _is_retryable_error(exc):
                raise
            delay = _extract_retry_seconds(exc) or (base_delay * (2**attempt))
            time.sleep(min(delay, 30.0))
    raise RuntimeError("Unreachable retry loop exit")


def extract_visual_cards(
    visual_records: list[dict[str, Any]],
    *,
    api_key: str,
    model_name: str = DEFAULT_AGENT_MODEL,
    cache_path: Path,
    reuse_existing: bool = True,
) -> tuple[dict[str, dict[str, Any]], dict[str, int]]:
    """Use Gemini Vision on each PNG crop to generate structured, queryable visual cards."""
    existing: dict[str, dict[str, Any]] = {}
    if reuse_existing and cache_path.exists():
        existing = {row["region_id"]: row for row in json.loads(cache_path.read_text(encoding="utf-8"))}

    client = genai.Client(api_key=api_key)
    token_stats = {"vision_calls": 0, "prompt_tokens": 0, "candidates_tokens": 0, "total_tokens": 0}
    results: dict[str, dict[str, Any]] = dict(existing)

    modality_guides = {
        "table": (
            "Transcribe ALL columns, merged headers, units, footnotes, and rows as clean GitHub Markdown. "
            "If cells use color coding instead of text (like Table 2.1 or feasibility dot legends), explicitly "
            "read the Key/Legend and write the exact assessed label/confidence dots per cell."
        ),
        "chart": (
            "List every panel label (a, b, c...), axis title and unit, legend categories, bar/line numeric labels, "
            "percentage values, shaded uncertainty ranges, horizontal/vertical threshold lines, and exact trends."
        ),
        "diagram_map": (
            "Describe the full diagram/map legend (colors, dots, hatching, arrow types), every panel's geographic or "
            "sectoral pattern across warming levels/scenarios, explicit numbers printed on maps/icons, and flow relationships."
        ),
    }

    for rec in visual_records:
        rid = rec["region_id"]
        if rid in results and results[rid].get("structured_data"):
            continue
        png_bytes = (REPO_ROOT / rec["crop_relpath"]).read_bytes()
        prompt = (
            f"You are indexing `{rec['label']}` ({rec['modality']}) on PDF page {rec['pdf_page']} "
            f"(printed page {rec['printed_page']}) of IPCC AR6 Synthesis Report.\n"
            f"Caption context from report: {rec['extracted_caption']}\n\n"
            f"Instructions: {modality_guides[rec['modality']]}\n"
            "Be exhaustive and faithful ONLY to what is clearly visible in the image + caption. "
            "Return strict JSON with keys: `title`, `summary`, `structured_data`, `keywords` (list of strings)."
        )
        schema = {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "summary": {"type": "string"},
                "structured_data": {"type": "string"},
                "keywords": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["title", "summary", "structured_data", "keywords"],
        }

        def _invoke():
            return client.models.generate_content(
                model=model_name,
                contents=[
                    types.Content(
                        role="user",
                        parts=[
                            types.Part.from_text(text=prompt),
                            types.Part.from_bytes(data=png_bytes, mime_type="image/png"),
                        ],
                    )
                ],
                config=types.GenerateContentConfig(
                    temperature=0.0,
                    response_mime_type="application/json",
                    response_json_schema=schema,
                    thinking_config=types.ThinkingConfig(thinking_budget=0),
                ),
            )

        resp = _call_with_retry(_invoke)
        parsed = json.loads(resp.text or "{}")
        results[rid] = {"region_id": rid, **parsed}
        usage = getattr(resp, "usage_metadata", None)
        token_stats["vision_calls"] += 1
        if usage:
            token_stats["prompt_tokens"] += int(getattr(usage, "prompt_token_count", 0) or 0)
            token_stats["candidates_tokens"] += int(getattr(usage, "candidates_token_count", 0) or 0)
            token_stats["total_tokens"] += int(getattr(usage, "total_token_count", 0) or 0)

        # Checkpoint incrementally so partial progress is never lost.
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(list(results.values()), indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[vision {len(results)}/{len(visual_records)}] {rid}", flush=True)

    return results, token_stats


def embed_multimodal_corpus(
    elements: list[dict[str, Any]],
    *,
    api_key: str,
    batch_size: int = 16,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, int]]:
    """Compute unified 768-dim text and raw-image embeddings using gemini-embedding-2."""
    client = genai.Client(api_key=api_key)
    embed_stats = {"text_embed_calls": 0, "image_embed_calls": 0, "total_items_embedded": 0}
    text_vecs: list[list[float]] = []

    cfg = types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT", output_dimensionality=MM_EMBED_DIMS)
    for start in range(0, len(elements), batch_size):
        batch = elements[start : start + batch_size]
        contents = [
            types.Content(
                parts=[
                    types.Part.from_text(
                        text=f"[{el['modality'].upper()} | {el['label']} | printed p.{el['printed_page']}]\n{el['text'][:6000]}"
                    )
                ]
            )
            for el in batch
        ]
        resp = _call_with_retry(
            lambda c=contents: client.models.embed_content(model=MM_EMBED_MODEL, contents=c, config=cfg)
        )
        embed_stats["text_embed_calls"] += 1
        embed_stats["total_items_embedded"] += len(batch)
        if len(resp.embeddings) != len(batch):
            raise RuntimeError(f"Expected {len(batch)} embeddings, got {len(resp.embeddings)}.")
        for emb in resp.embeddings:
            vec = l2_normalize([float(x) for x in emb.values])
            text_vecs.append(vec)

    visual_indices = [idx for idx, el in enumerate(elements) if el["modality"] != "text"]
    image_vecs: list[list[float]] = []
    for idx in visual_indices:
        el = elements[idx]
        png_bytes = (REPO_ROOT / el["crop_relpath"]).read_bytes()
        resp = _call_with_retry(
            lambda b=png_bytes, lb=el["label"]: client.models.embed_content(
                model=MM_EMBED_MODEL,
                contents=[types.Content(parts=[types.Part.from_bytes(data=b, mime_type="image/png")])],
                config=cfg,
            )
        )
        embed_stats["image_embed_calls"] += 1
        embed_stats["total_items_embedded"] += 1
        image_vecs.append(l2_normalize([float(x) for x in resp.embeddings[0].values]))

    return (
        np.asarray(text_vecs, dtype=np.float32),
        np.asarray(image_vecs, dtype=np.float32),
        np.asarray(visual_indices, dtype=np.int32),
        embed_stats,
    )


def run_ingest(*, render_crops_only: bool = False, reuse_cards: bool = True) -> dict[str, Any]:
    """Execute end-to-end IPCC AR6 SYR ingestion, cropping, vision indexing, and embedding."""
    t0 = time.perf_counter()
    pdf_path, sha256 = ensure_pdf_downloaded()
    text_elements, audit = extract_document_text_and_audit(pdf_path)
    visual_records = render_visual_crops(pdf_path, ADV_CROPS_DIR, dpi=200, specs=VISUAL_REGION_SPECS)

    manifest_summary = {
        "document": {
            "id": DOCUMENT_ID,
            "title": DOCUMENT_TITLE,
            "official_url": DOCUMENT_URL,
            "doi": DOCUMENT_DOI,
            "isbn": DOCUMENT_ISBN,
            "pdf_sha256": sha256,
            "license_summary": "Copyright IPCC 2023 (ISBN 978-92-9169-164-7). Short extracts permitted with attribution; raw PDF downloaded from official URL rather than redistributed in git.",
        },
        "indexing_config": {
            "text_chunk_max_chars": 1100,
            "text_chunk_overlap": 120,
            "crop_dpi": 200,
            "vision_extraction_model": DEFAULT_AGENT_MODEL,
            "embedding_model": MM_EMBED_MODEL,
            "embedding_dimensions": MM_EMBED_DIMS,
        },
        "coverage_audit": audit,
        "visual_regions_count": len(visual_records),
        "visual_modality_counts": {
            m: sum(1 for r in visual_records if r["modality"] == m)
            for m in ("table", "chart", "diagram_map")
        },
        "visual_catalog": [
            {
                "region_id": r["region_id"],
                "label": r["label"],
                "modality": r["modality"],
                "pdf_page": r["pdf_page"],
                "caption_page": r["caption_page"],
                "printed_page": r["printed_page"],
                "bbox": r["bbox"],
                "section": r["section"],
                "crop_relpath": r["crop_relpath"],
                "image_size": [r["image_width"], r["image_height"]],
            }
            for r in visual_records
        ],
    }

    if render_crops_only:
        MANIFEST_PATH.write_text(json.dumps(manifest_summary, indent=2, ensure_ascii=False), encoding="utf-8")
        return manifest_summary

    settings = load_settings(require_api_key=True, require_db=False)
    ADV_INDEX_DIR.mkdir(parents=True, exist_ok=True)
    cards_path = ADV_INDEX_DIR / "visual_cards.json"
    cards, vision_stats = extract_visual_cards(
        visual_records,
        api_key=settings.gemini_api_key,
        model_name=settings.agent_model,
        cache_path=cards_path,
        reuse_existing=reuse_cards,
    )

    visual_elements: list[dict[str, Any]] = []
    for rec in visual_records:
        card = cards[rec["region_id"]]
        kw = ", ".join(card.get("keywords") or [])
        body = (
            f"Title: {card.get('title', rec['label'])}\n"
            f"Caption: {rec['extracted_caption']}\n"
            f"Summary: {card.get('summary', '')}\n"
            f"Extracted Details:\n{card.get('structured_data', '')}\n"
            f"Keywords: {kw}"
        ).strip()
        visual_elements.append({
            "id": rec["region_id"],
            "modality": rec["modality"],
            "label": rec["label"],
            "pdf_page": rec["pdf_page"],
            "printed_page": rec["printed_page"],
            "caption_page": rec["caption_page"],
            "section": rec["section"],
            "bbox": rec["bbox"],
            "crop_relpath": rec["crop_relpath"],
            "text": body,
            "source_id": DOCUMENT_ID,
        })

    all_elements = text_elements + visual_elements
    text_mat, image_mat, image_indices, embed_stats = embed_multimodal_corpus(
        all_elements,
        api_key=settings.gemini_api_key,
        batch_size=16,
    )

    (ADV_INDEX_DIR / "elements.json").write_text(
        json.dumps(all_elements, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    np.savez_compressed(
        ADV_INDEX_DIR / "embeddings.npz",
        text_embeddings=text_mat,
        image_embeddings=image_mat,
        image_indices=image_indices,
    )

    manifest_summary["ingestion_stats"] = {
        "total_indexed_elements": len(all_elements),
        "text_elements": len(text_elements),
        "visual_elements": len(visual_elements),
        "vision_extraction": vision_stats,
        "embeddings": embed_stats,
        "elapsed_seconds": round(time.perf_counter() - t0, 2),
    }
    MANIFEST_PATH.write_text(json.dumps(manifest_summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest & build multimodal index for IPCC AR6 SYR (186 pages).")
    parser.add_argument("--render-crops-only", action="store_true", help="Only download PDF, scan pages, and render PNG crops.")
    parser.add_argument("--no-reuse-cards", action="store_true", help="Re-run Gemini Vision extraction even if cached.")
    args = parser.parse_args()
    summary = run_ingest(render_crops_only=args.render_crops_only, reuse_cards=not args.no_reuse_cards)
    print(json.dumps({
        "pages": summary["coverage_audit"]["total_pdf_pages"],
        "indexed_pages": summary["coverage_audit"]["indexed_pages_count"],
        "skipped_blank": summary["coverage_audit"]["skipped_blank_pages_count"],
        "text_chunks": summary["coverage_audit"]["total_text_chunks"],
        "visual_regions": summary["visual_regions_count"],
        "modalities": summary["visual_modality_counts"],
        "stats": summary.get("ingestion_stats"),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
