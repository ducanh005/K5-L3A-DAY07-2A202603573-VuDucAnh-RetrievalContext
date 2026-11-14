"""Document metadata, download verification, and visual region catalog for IPCC AR6 SYR (186 pages)."""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pymupdf
import requests

REPO_ROOT = Path(__file__).resolve().parents[2]
ADV_DATA_DIR = REPO_ROOT / "data" / "advanced"
ADV_RAW_DIR = ADV_DATA_DIR / "raw"
ADV_CROPS_DIR = ADV_DATA_DIR / "crops"
ADV_INDEX_DIR = ADV_DATA_DIR / "index"

DOCUMENT_ID = "ipcc-ar6-syr-2023"
DOCUMENT_TITLE = (
    "Climate Change 2023: Synthesis Report (AR6 Full Volume — SPM, Longer Report & Annexes)"
)
DOCUMENT_URL = "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
DOCUMENT_DOI = "10.59327/IPCC/AR6-9789291691647"
DOCUMENT_ISBN = "978-92-9169-164-7"
PDF_FILENAME = "IPCC_AR6_SYR_FullVolume.pdf"

VALID_MODALITIES = frozenset({"text", "table", "chart", "diagram_map"})


@dataclass(frozen=True)
class VisualRegionSpec:
    region_id: str
    label: str
    modality: str  # "table" | "chart" | "diagram_map"
    pdf_page: int
    caption_page: int
    bbox: tuple[float, float, float, float]  # x0, y0, x1, y1 in PDF points (612x792)
    section: str
    caption_hint: str


# Comprehensive visual catalog spanning all 186 pages of IPCC_AR6_SYR_FullVolume.pdf.
VISUAL_REGION_SPECS: tuple[VisualRegionSpec, ...] = (
    # --- Summary for Policymakers (pp. 17-50 -> printed 1-34) ---
    VisualRegionSpec(
        "VIS:Figure_SPM1:p023",
        "Figure SPM.1",
        "diagram_map",
        pdf_page=23,
        caption_page=23,
        bbox=(45.0, 48.0, 565.0, 745.0),
        section="Summary for Policymakers",
        caption_hint="Figure SPM.1: Observed widespread climate impacts, attribution confidence dots, and generational warming timeline (1900-2100).",
    ),
    VisualRegionSpec(
        "VIS:Table_Box_SPM1:p026",
        "Box SPM.1, Table 1",
        "table",
        pdf_page=26,
        caption_page=26,
        bbox=(65.0, 48.0, 550.0, 350.0),
        section="Summary for Policymakers",
        caption_hint="Box SPM.1, Table 1: Description and relationship of scenarios (C1-C8, SSPx-y, RCPy) across AR6 Working Group reports.",
    ),
    VisualRegionSpec(
        "VIS:Figure_SPM2:p030",
        "Figure SPM.2",
        "diagram_map",
        pdf_page=30,
        caption_page=30,
        bbox=(45.0, 45.0, 565.0, 750.0),
        section="Summary for Policymakers",
        caption_hint="Figure SPM.2: Projected regional temperature, annual mean precipitation, and soil moisture maps at 1.5°C to 4°C warming.",
    ),
    VisualRegionSpec(
        "VIS:Figure_SPM3:p032",
        "Figure SPM.3",
        "diagram_map",
        pdf_page=32,
        caption_page=32,
        bbox=(45.0, 45.0, 565.0, 755.0),
        section="Summary for Policymakers",
        caption_hint="Figure SPM.3: Projected risks of species losses, heat-humidity mortality days, and maize/fisheries yield maps across global warming levels.",
    ),
    VisualRegionSpec(
        "VIS:Figure_SPM4:p033",
        "Figure SPM.4",
        "chart",
        pdf_page=33,
        caption_page=34,
        bbox=(45.0, 120.0, 565.0, 745.0),
        section="Summary for Policymakers",
        caption_hint="Figure SPM.4: Assessed temperature change curves, burning-embers Global Reasons for Concern (AR5 vs AR6), system risks, sea level rise and adaptation risk bars.",
    ),
    VisualRegionSpec(
        "VIS:Table_SPM1:p037",
        "Table SPM.1",
        "table",
        pdf_page=37,
        caption_page=37,
        bbox=(60.0, 48.0, 555.0, 165.0),
        section="Summary for Policymakers",
        caption_hint="Table SPM.1: Greenhouse gas and CO2 emission reductions (%) from 2019 in 2030, 2035, 2040, and 2050.",
    ),
    VisualRegionSpec(
        "VIS:Figure_SPM5:p038",
        "Figure SPM.5",
        "chart",
        pdf_page=38,
        caption_page=39,
        bbox=(45.0, 52.0, 565.0, 725.0),
        section="Summary for Policymakers",
        caption_hint="Figure SPM.5: Global net GHG, CO2, CH4 emissions pathways, net-zero year bars, and Illustrative Mitigation Pathways (IMPs) by sector.",
    ),
    VisualRegionSpec(
        "VIS:Figure_SPM6:p041",
        "Figure SPM.6",
        "diagram_map",
        pdf_page=41,
        caption_page=41,
        bbox=(45.0, 52.0, 565.0, 750.0),
        section="Summary for Policymakers",
        caption_hint="Figure SPM.6: Illustrative climate-resilient development pathways (red to green trajectories, choice points, enablers and outcomes).",
    ),
    VisualRegionSpec(
        "VIS:Figure_SPM7:p043",
        "Figure SPM.7",
        "chart",
        pdf_page=43,
        caption_page=43,
        bbox=(50.0, 48.0, 565.0, 750.0),
        section="Summary for Policymakers",
        caption_hint="Figure SPM.7: Feasibility of adaptation options, synergies, near-term 2030 mitigation potential by cost bracket, and 2050 demand-side reductions.",
    ),
    VisualRegionSpec(
        "VIS:Table_SPM7_Feasibility:p043",
        "Figure SPM.7 Adaptation Feasibility Table",
        "table",
        pdf_page=43,
        caption_page=43,
        bbox=(50.0, 56.0, 412.0, 628.0),
        section="Summary for Policymakers",
        caption_hint="Figure SPM.7 Panel (a) left table: Climate responses and adaptation options assessed for feasibility up to 1.5°C, synergies with mitigation, and confidence dots.",
    ),
    # --- Section 1: Introduction ---
    VisualRegionSpec(
        "VIS:Figure_1_1:p055",
        "Figure 1.1",
        "diagram_map",
        pdf_page=55,
        caption_page=55,
        bbox=(40.0, 65.0, 570.0, 210.0),
        section="Section 1: Introduction",
        caption_hint="Figure 1.1: The Synthesis Report figures key explaining axis icons and italicized non-technical annotations.",
    ),
    # --- Section 2: Current Status and Trends ---
    VisualRegionSpec(
        "VIS:Figure_2_1:p059",
        "Figure 2.1",
        "chart",
        pdf_page=59,
        caption_page=59,
        bbox=(45.0, 45.0, 570.0, 735.0),
        section="Section 2: Current Status and Trends",
        caption_hint="Figure 2.1: Causal chain from GHG emissions (GtCO2-eq/yr) to atmospheric CO2/CH4/N2O concentrations, warming (+1.1°C), and human attribution.",
    ),
    VisualRegionSpec(
        "VIS:Figure_2_2_charts:p061",
        "Figure 2.2 Panels (a)-(c)",
        "chart",
        pdf_page=61,
        caption_page=62,
        bbox=(42.0, 45.0, 575.0, 582.0),
        section="Section 2: Current Status and Trends",
        caption_hint="Figure 2.2 (a-c): Historical cumulative CO2 (1850-2019), regional per-capita GHG vs population (2019), and 1990-2019 regional shares.",
    ),
    VisualRegionSpec(
        "VIS:Table_Fig2_2d:p061",
        "Figure 2.2 Panel (d) Table",
        "table",
        pdf_page=61,
        caption_page=62,
        bbox=(42.0, 565.0, 575.0, 750.0),
        section="Section 2: Current Status and Trends",
        caption_hint="Figure 2.2 (d): Regional indicators (2019 population, GDP per capita, GHG intensity, GHG per capita, production vs consumption CO2FFI 2018).",
    ),
    VisualRegionSpec(
        "VIS:Table_2_1:p063",
        "Table 2.1",
        "table",
        pdf_page=63,
        caption_page=63,
        bbox=(40.0, 42.0, 570.0, 610.0),
        section="Section 2: Current Status and Trends",
        caption_hint="Table 2.1: Color-coded assessment of observed changes in large-scale climate indicators and human contribution.",
    ),
    VisualRegionSpec(
        "VIS:Figure_2_3a:p064",
        "Figure 2.3 Panel (a)",
        "chart",
        pdf_page=64,
        caption_page=66,
        bbox=(35.0, 45.0, 565.0, 745.0),
        section="Section 2: Current Status and Trends",
        caption_hint="Figure 2.3 (a): Comparison of vulnerability, hazard-driven human mortality (2010-2020), and regional emissions share.",
    ),
    VisualRegionSpec(
        "VIS:Figure_2_3b:p065",
        "Figure 2.3 Panel (b)",
        "diagram_map",
        pdf_page=65,
        caption_page=66,
        bbox=(45.0, 45.0, 575.0, 745.0),
        section="Section 2: Current Status and Trends",
        caption_hint="Figure 2.3 (b): Global cartogram / map comparing regional vulnerability index (INFORM/WRI 2019) vs historical CO2 per capita.",
    ),
    VisualRegionSpec(
        "VIS:Figure_2_4:p070",
        "Figure 2.4",
        "chart",
        pdf_page=70,
        caption_page=70,
        bbox=(35.0, 50.0, 565.0, 645.0),
        section="Section 2: Current Status and Trends",
        caption_hint="Figure 2.4: Unit cost declines (LCOE $/MWh & Li-ion $/kWh) and adoption growth (GW & million EVs) for PV, wind, and EVs.",
    ),
    VisualRegionSpec(
        "VIS:Table_2_2:p074",
        "Table 2.2",
        "table",
        pdf_page=74,
        caption_page=74,
        bbox=(35.0, 240.0, 560.0, 610.0),
        section="Section 2: Current Status and Trends",
        caption_hint="Table 2.2: Projected global emissions in 2030 under implemented 2020 policies vs unconditional and conditional NDCs, plus gaps.",
    ),
    VisualRegionSpec(
        "VIS:Figure_2_5:p075",
        "Figure 2.5",
        "chart",
        pdf_page=75,
        caption_page=75,
        bbox=(45.0, 45.0, 575.0, 480.0),
        section="Section 2: Current Status and Trends",
        caption_hint="Figure 2.5: Global GHG emissions trajectories of C1-C8 modelled pathways compared against 2030 policies and NDC projections.",
    ),
    VisualRegionSpec(
        "VIS:CrossBox2_Diagram:p081",
        "Cross-Section Box.2 Figure 1",
        "diagram_map",
        pdf_page=81,
        caption_page=82,
        bbox=(45.0, 42.0, 575.0, 425.0),
        section="Section 2: Cross-Section Box 2",
        caption_hint="Cross-Section Box.2 Figure 1 (a): AR6 causal loop linking socio-economics, CO2 emissions, SSP temperature pathways, and RFC1 burning embers.",
    ),
    VisualRegionSpec(
        "VIS:Table_CrossBox2_Risk:p081",
        "Cross-Section Box.2 Table & Risk Venn",
        "table",
        pdf_page=81,
        caption_page=82,
        bbox=(45.0, 420.0, 575.0, 748.0),
        section="Section 2: Cross-Section Box 2",
        caption_hint="Cross-Section Box.2 Panels (b)-(c): Scenario classification table C1-C8 mapped to SSP/RCP scenarios and Risk determinants diagram.",
    ),
    # --- Section 3: Long-Term Climate and Development Futures ---
    VisualRegionSpec(
        "VIS:Figure_3_1:p086",
        "Figure 3.1",
        "diagram_map",
        pdf_page=86,
        caption_page=86,
        bbox=(35.0, 45.0, 565.0, 745.0),
        section="Section 3: Long-Term Futures",
        caption_hint="Figure 3.1: Regional changes in temperature extremes, daily precipitation, and soil moisture at 1.5°C, 2°C, 3°C, and 4°C warming.",
    ),
    VisualRegionSpec(
        "VIS:Figure_3_2:p089",
        "Figure 3.2",
        "diagram_map",
        pdf_page=89,
        caption_page=90,
        bbox=(45.0, 45.0, 575.0, 745.0),
        section="Section 3: Long-Term Futures",
        caption_hint="Figure 3.2: Projected climate risks across species, hyperthermic mortality days, and maize/fisheries yields (full-page maps).",
    ),
    VisualRegionSpec(
        "VIS:Figure_3_3_rfc:p091",
        "Figure 3.3 Panels (a)-(b)",
        "diagram_map",
        pdf_page=91,
        caption_page=93,
        bbox=(45.0, 45.0, 575.0, 745.0),
        section="Section 3: Long-Term Futures",
        caption_hint="Figure 3.3 (a-b): Synthetic burning-embers diagrams comparing AR5 vs AR6 Global RFCs and terrestrial/ocean/coastal systems.",
    ),
    VisualRegionSpec(
        "VIS:Figure_3_3_reg:p092",
        "Figure 3.3 Panels (c)-(d)",
        "diagram_map",
        pdf_page=92,
        caption_page=93,
        bbox=(35.0, 45.0, 565.0, 745.0),
        section="Section 3: Long-Term Futures",
        caption_hint="Figure 3.3 (c-d): Sectoral burning embers by adaptation level (health, food security, coastal geographies) and regional key risks.",
    ),
    VisualRegionSpec(
        "VIS:Figure_3_4:p096",
        "Figure 3.4",
        "chart",
        pdf_page=96,
        caption_page=97,
        bbox=(35.0, 45.0, 565.0, 745.0),
        section="Section 3: Long-Term Futures",
        caption_hint="Figure 3.4: Observed and projected global mean sea level rise (1900-2100/2300) and regional amplification of 1-in-100-year coastal events.",
    ),
    VisualRegionSpec(
        "VIS:Figure_3_5:p099",
        "Figure 3.5",
        "chart",
        pdf_page=99,
        caption_page=99,
        bbox=(45.0, 45.0, 575.0, 520.0),
        section="Section 3: Long-Term Futures",
        caption_hint="Figure 3.5: Cumulative past, committed fossil infrastructure, and remaining carbon budgets for 1.5°C and 2°C.",
    ),
    VisualRegionSpec(
        "VIS:Table_3_1:p100",
        "Table 3.1",
        "table",
        pdf_page=100,
        caption_page=100,
        bbox=(35.0, 40.0, 568.0, 675.0),
        section="Section 3: Long-Term Futures",
        caption_hint="Table 3.1: Key characteristics of modelled global emissions pathways (C1-C6, GHG reductions, net zero timings, cumulative CO2, temperatures, likelihoods).",
    ),
    VisualRegionSpec(
        "VIS:Figure_3_6:p102",
        "Figure 3.6",
        "chart",
        pdf_page=102,
        caption_page=102,
        bbox=(35.0, 45.0, 565.0, 510.0),
        section="Section 3: Long-Term Futures",
        caption_hint="Figure 3.6: Global GHG, CO2 and CH4 pathways (IMP-Ren, IMP-LD, IMP-SP, IMP-Neg, IMP-GS), net-zero timings and warming categories.",
    ),
    # --- Section 4: Near-Term Responses in a Changing Climate ---
    VisualRegionSpec(
        "VIS:Figure_4_1:p110",
        "Figure 4.1",
        "chart",
        pdf_page=110,
        caption_page=111,
        bbox=(35.0, 42.0, 568.0, 748.0),
        section="Section 4: Near-Term Responses",
        caption_hint="Figure 4.1: Sectoral CO2 emissions trajectories in 1.5°C pathways (electricity, transport, buildings, industry, AFOLU).",
    ),
    VisualRegionSpec(
        "VIS:Figure_4_2:p113",
        "Figure 4.2",
        "diagram_map",
        pdf_page=113,
        caption_page=113,
        bbox=(45.0, 48.0, 570.0, 750.0),
        section="Section 4: Near-Term Responses",
        caption_hint="Figure 4.2: Illustrative climate-resilient development pathways diagram (Section 4 context).",
    ),
    VisualRegionSpec(
        "VIS:Figure_4_3:p116",
        "Figure 4.3",
        "diagram_map",
        pdf_page=116,
        caption_page=117,
        bbox=(35.0, 42.0, 565.0, 748.0),
        section="Section 4: Near-Term Responses",
        caption_hint="Figure 4.3: Regional coastal flood exposure increase (2020-2040), extreme sea-level dot map, and cascading smallholder risk network diagram.",
    ),
    VisualRegionSpec(
        "VIS:Figure_4_4:p119",
        "Figure 4.4",
        "chart",
        pdf_page=119,
        caption_page=120,
        bbox=(45.0, 45.0, 570.0, 750.0),
        section="Section 4: Near-Term Responses",
        caption_hint="Figure 4.4: Climate response & adaptation feasibility matrix, 2030 mitigation cost/potential bars, and 2050 demand-side savings.",
    ),
    VisualRegionSpec(
        "VIS:Figure_4_5:p125",
        "Figure 4.5",
        "diagram_map",
        pdf_page=125,
        caption_page=125,
        bbox=(45.0, 45.0, 570.0, 645.0),
        section="Section 4: Near-Term Responses",
        caption_hint="Figure 4.5: Synergies (blue) and trade-offs (orange/striped) matrix across 16 SDGs and adaptation/mitigation sectors.",
    ),
    VisualRegionSpec(
        "VIS:Figure_4_6:p129",
        "Figure 4.6",
        "chart",
        pdf_page=129,
        caption_page=129,
        bbox=(45.0, 45.0, 570.0, 495.0),
        section="Section 4: Near-Term Responses",
        caption_hint="Figure 4.6: Average mitigation investment flows (2017-2020) vs needs to 2030 (USD billions/yr) and lower/upper multiplication factors table.",
    ),
    VisualRegionSpec(
        "VIS:Table_4_6_Multipliers:p129",
        "Figure 4.6 Multiplication Factors Table",
        "table",
        pdf_page=129,
        caption_page=129,
        bbox=(45.0, 74.0, 575.0, 472.0),
        section="Section 4: Near-Term Responses",
        caption_hint="Figure 4.6 table & bars: Mitigation investment multiplication factors (Lower range and Upper range) by sector, economy type, and region until 2030.",
    ),
)


def pdf_to_printed_page(pdf_page: int) -> str:
    """Map 1-based PDF page number (1..186) to printed page label in IPCC AR6 SYR."""
    if pdf_page == 1:
        return "cover"
    if pdf_page == 186:
        return "back_cover"
    if 2 <= pdf_page <= 16:
        roman_val = pdf_page - 2
        if roman_val <= 0:
            return "frontmatter"
        return _to_roman(roman_val).lower()
    return str(pdf_page - 16)


def _to_roman(num: int) -> str:
    vals = [
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    out: list[str] = []
    for v, sym in vals:
        while num >= v:
            out.append(sym)
            num -= v
    return "".join(out)


def infer_section(pdf_page: int, page_text: str) -> str:
    """Assign high-level report section based on page range and headings."""
    if pdf_page <= 16:
        return "Frontmatter"
    if 17 <= pdf_page <= 52:
        return "Summary for Policymakers"
    if 53 <= pdf_page <= 56:
        return "Section 1: Introduction"
    if 57 <= pdf_page <= 82:
        return "Section 2: Current Status and Trends"
    if 83 <= pdf_page <= 106:
        return "Section 3: Long-Term Futures"
    if 107 <= pdf_page <= 132:
        return "Section 4: Near-Term Responses"
    if 133 <= pdf_page <= 148:
        return "Annex I: Glossary"
    if 149 <= pdf_page <= 150:
        return "Annex II: Acronyms and Units"
    if 151 <= pdf_page <= 158:
        return "Annex III: Contributors"
    if 159 <= pdf_page <= 174:
        return "Annex IV: Expert Reviewers"
    if 175 <= pdf_page <= 178:
        return "Annex V: List of Publications"
    if 179 <= pdf_page <= 185:
        return "Index"
    return "Back Cover"


def ensure_pdf_downloaded(pdf_path: Path | None = None) -> tuple[Path, str]:
    """Download IPCC AR6 SYR Full Volume from official URL if missing and compute SHA-256."""
    target = pdf_path or (ADV_RAW_DIR / PDF_FILENAME)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        resp = requests.get(DOCUMENT_URL, timeout=120)
        resp.raise_for_status()
        target.write_bytes(resp.content)
    sha256 = hashlib.sha256(target.read_bytes()).hexdigest()
    return target, sha256


def crop_filename(region_id: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", region_id)
    return f"{safe}.png"


def render_visual_crops(
    pdf_path: Path,
    crops_dir: Path | None = None,
    *,
    dpi: int = 200,
    specs: tuple[VisualRegionSpec, ...] = VISUAL_REGION_SPECS,
) -> list[dict[str, Any]]:
    """Render crisp PNG crops for all visual regions in the PDF using deterministic coordinates."""
    out_dir = crops_dir or ADV_CROPS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    records: list[dict[str, Any]] = []
    for spec in specs:
        if spec.pdf_page < 1 or spec.pdf_page > len(doc):
            raise ValueError(f"Invalid pdf_page {spec.pdf_page} for {spec.region_id} (len={len(doc)})")
        page = doc[spec.pdf_page - 1]
        cap_page = doc[spec.caption_page - 1]
        clip = pymupdf.Rect(*spec.bbox) & page.rect
        pix = page.get_pixmap(dpi=dpi, clip=clip)
        out_path = out_dir / crop_filename(spec.region_id)
        pix.save(str(out_path))
        cap_text = _extract_caption_snippet(cap_page.get_text(), spec.label)
        records.append({
            "region_id": spec.region_id,
            "label": spec.label,
            "modality": spec.modality,
            "pdf_page": spec.pdf_page,
            "caption_page": spec.caption_page,
            "printed_page": pdf_to_printed_page(spec.pdf_page),
            "bbox": [round(float(x), 1) for x in clip],
            "section": spec.section,
            "caption_hint": spec.caption_hint,
            "extracted_caption": cap_text,
            "crop_relpath": f"data/advanced/crops/{crop_filename(spec.region_id)}",
            "image_width": pix.width,
            "image_height": pix.height,
        })
    return records


def _extract_caption_snippet(page_text: str, label: str) -> str:
    """Extract paragraph around figure/table label on caption_page."""
    norm = re.sub(r"\s+", " ", page_text).strip()
    key = label.replace(" Panels (a)-(c)", "").replace(" Panel (d) Table", "").replace(" Panel (a)", "").replace(" Panel (b)", "").replace(" Panels (a)-(b)", "").replace(" Panels (c)-(d)", "").replace(" Table & Risk Venn", "")
    idx = norm.find(key)
    if idx == -1:
        return norm[:900]
    return norm[max(0, idx - 80) : min(len(norm), idx + 1100)]
