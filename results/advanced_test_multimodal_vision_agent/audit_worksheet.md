# Advanced Audit Worksheet — `multimodal_vision_agent` (`test`, N=32)

## adv_test_01 [table] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** According to Table SPM.1 (p.37 / printed p.21), for pathways that 'Limit warming to 2°C (>67%)', what are the median and [5–95 percentile] percentage reductions from 2019 emission levels in 2030, 2035, 2040, and 2050 for both GHG and CO2?
- **Expected Answer:** For 'Limit warming to 2°C (>67%)': GHG reductions = 21 [1-42]% (2030), 35 [22-55]% (2035), 46 [34-63]% (2040), and 64 [53-77]% (2050). CO2 reductions = 22 [1-44]% (2030), 37 [21-59]% (2035), 51 [36-70]% (2040), and 73 [55-90]% (2050).
- **Gold Source:** pages `[37]`, regions `['VIS:Table_SPM1:p037']`, note: Verified from VIS_Table_SPM1_p037.png (PDF p.37, printed p.21), bottom two rows.
- **Agent Answer:** According to Table SPM.1 (p. 21 / pdf p. 37), for pathways that **Limit warming to 2°C (>67%)**, the median and [5–95th percentile] percentage reductions from 2019 emission levels are as follows [VIS:Table_SPM1:p037]:

* **Greenhouse Gas (GHG) reductions:**
  * **2030:** 21% [1–42%] [VIS:Table_SPM1:p037]
  * **2035:** 35% [22–55%] [VIS:Table_SPM1:p037]
  * **2040:** 46% [34–63%] [VIS:Table_SPM1:p037]
  * **2050:** 64% [53–77%] [VIS:Table_SPM1:p037]

* **CO₂ reductions:**
  * **2030:** 22% [1–44%] [VIS:Table_SPM1:p037]
  * **2035:** 37% [21–59%] [VIS:Table_SPM1:p037]
  * **2040:** 51% [36–70%] [VIS:Table_SPM1:p037]
  * **2050:** 73% [55–90%] [VIS:Table_SPM1:p037]
- **Citations:** ['VIS:Table_SPM1:p037']
- **Citation Details:** [{"id": "VIS:Table_SPM1:p037", "modality": "table", "label": "Table SPM.1", "pdf_page": 37, "printed_page": "21", "bbox": [60.0, 48.0, 555.0, 165.0], "crop_relpath": "data/advanced/crops/VIS_Table_SPM1_p037.png"}]
- **Inspected Crops:** ['VIS:Table_SPM1:p037']

## adv_test_02 [table] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure 2.2 panel (d) (p.61 / printed p.45), compare 'Africa', 'Europe', and 'Eastern Asia' across three rows: (1) 2019 GHG emissions intensity (tCO2-eq / USD1000_PPP 2017), (2) 2018 production-based CO2FFI emissions per person, and (3) 2018 consumption-based CO2FFI emissions per person.
- **Expected Answer:** Africa: intensity = 0.78, 2018 production-based CO2FFI = 1.2, consumption-based CO2FFI = 0.84 tCO2FFI per person. Europe: intensity = 0.18, production-based = 6.5, consumption-based = 7.8 tCO2FFI per person. Eastern Asia: intensity = 0.62, production-based = 8.4, consumption-based = 6.7 tCO2FFI per person.
- **Gold Source:** pages `[61]`, regions `['VIS:Table_Fig2_2d:p061']`, note: Verified from VIS_Table_Fig2_2d_p061.png (PDF p.61, printed p.45).
- **Agent Answer:** Based on Figure 2.2 panel (d) (*Regional indicators (2019) and regional production vs consumption accounting (2018)*, p. 61 / printed p. 45) [VIS:Table_Fig2_2d:p061], the comparison between **Africa**, **Europe**, and **Eastern Asia** across the three requested indicators is as follows:

### 1. 2019 Net GHG Emissions Intensity (production basis)
*(Unit: $\text{tCO}_2\text{-eq} / \text{USD}1000_{\text{PPP}} \ 2017$)*
* **Africa:** **0.78** [VIS:Table_Fig2_2d:p061]
* **Eastern Asia:** **0.62** [VIS:Table_Fig2_2d:p061]
* **Europe:** **0.18** [VIS:Table_Fig2_2d:p061]
* *Comparison:* Africa has the highest emissions intensity among the three, followed by Eastern Asia, while Europe has the lowest emissions intensity (less than a quarter of Africa's).

---

### 2. 2018 Production-based $\text{CO}_2\text{FFI}$ Emissions per Person
*(Unit: $\text{tCO}_2\text{FFI}$ per person, based on 2018 data)*
* **Africa:** **1.2** [VIS:Table_Fig2_2d:p061]
* **Eastern Asia:** **8.4** [VIS:Table_Fig2_2d:p061]
* **Europe:** **6.5** [VIS:Table_Fig2_2d:p061]
* *Comparison:* Eastern Asia has the highest production-based emissions per person (8.4), followed by Europe (6.5), whereas Africa has substantially lower per capita emissions (1.2).

---

### 3. 2018 Consumption-based $\text{CO}_2\text{FFI}$ Emissions per Person
*(Unit: $\text{tCO}_2\text{FFI}$ per person, based on 2018 data)*
* **Africa:** **0.84** [VIS:Table_Fig2_2d:p061]
* **Eastern Asia:** **6.7** [VIS:Table_Fig2_2d:p061]
* **Europe:** **7.8** [VIS:Table_Fig2_2d:p061]
* *Comparison:* Europe has the highest consumption-based emissions per person (7.8), followed by Eastern Asia (6.7), with Africa having the lowest (0.84). 

*(Note on production vs. consumption accounting: In Europe, consumption-based per capita emissions [7.8] exceed production-based emissions [6.5], indicating net embodied carbon imports, whereas in Eastern Asia [8.4 vs. 6.7] and Africa [1.2 vs. 0.84], production-based emissions exceed consumption-based emissions, indicating net embodied carbon exports) [VIS:Table_Fig2_2d:p061].*
- **Citations:** ['VIS:Table_Fig2_2d:p061']
- **Citation Details:** [{"id": "VIS:Table_Fig2_2d:p061", "modality": "table", "label": "Figure 2.2 Panel (d) Table", "pdf_page": 61, "printed_page": "45", "bbox": [42.0, 565.0, 575.0, 750.0], "crop_relpath": "data/advanced/crops/VIS_Table_Fig2_2d_p061.png"}]
- **Inspected Crops:** ['VIS:Table_Fig2_2d:p061']

## adv_test_03 [table] — `status=answered` | `searches=1` | `inspects=2` | `err=None`
- **Question:** In Table 2.1 (p.63 / printed p.47) under 'Ocean' and 'Carbon cycle', what are the colour-key confidence/likelihood assessments and any cell text annotations for both 'Observed change assessment' and 'Human contribution assessment' on: (1) 'Ocean heat content increase since the 1970s', (2) 'Salinity changes since the mid-20th century', and (3) 'Increased amplitude of the seasonal cycle of atmospheric CO2 since the early 1960s'?
- **Expected Answer:** 1) Ocean heat content increase since the 1970s: Observed = virtually certain (dark maroon), Human = extremely likely (rust/red-orange) + 'Main driver'. 2) Salinity changes since the mid-20th century: Observed = virtually certain (dark maroon), Human = extremely likely (rust/red-orange, no extra text). 3) Increased amplitude of the seasonal cycle of atmospheric CO2 since the early 1960s: Observed = likely / high confidence (golden yellow), Human = medium confidence (pale cream) + 'Main driver'.
- **Gold Source:** pages `[63]`, regions `['VIS:Table_2_1:p063']`, note: Verified from VIS_Table_2_1_p063.png (PDF p.63, printed p.47).
- **Agent Answer:** Based on Table 2.1 (*Assessment of observed changes in large-scale indicators of mean climate across climate system components, and their attribution to human influence*, p. 63 / printed p. 47) and its colour key, the assessments and text annotations are as follows [VIS:Table_2_1:p063]:

### 1. Ocean heat content increase since the 1970s (under 'Ocean')
* **Observed change assessment:** 
  * **Colour-key confidence/likelihood:** **virtually certain** (dark maroon) [VIS:Table_2_1:p063]
  * **Text annotation:** None (blank cell) [VIS:Table_2_1:p063]
* **Human contribution assessment:** 
  * **Colour-key confidence/likelihood:** **extremely likely** (red-orange/rust) [VIS:Table_2_1:p063]
  * **Text annotation:** **"Main driver"** [VIS:Table_2_1:p063]

---

### 2. Salinity changes since the mid-20th century (under 'Ocean')
* **Observed change assessment:** 
  * **Colour-key confidence/likelihood:** **virtually certain** (dark maroon) [VIS:Table_2_1:p063]
  * **Text annotation:** None (blank cell) [VIS:Table_2_1:p063]
* **Human contribution assessment:** 
  * **Colour-key confidence/likelihood:** **extremely likely** (red-orange/rust) [VIS:Table_2_1:p063]
  * **Text annotation:** None (blank cell) [VIS:Table_2_1:p063]

---

### 3. Increased amplitude of the seasonal cycle of atmospheric CO₂ since the early 1960s (under 'Carbon cycle')
* **Observed change assessment:** 
  * **Colour-key confidence/likelihood:** **likely / high confidence** (yellow) [VIS:Table_2_1:p063]
  * **Text annotation:** None (blank cell) [VIS:Table_2_1:p063]
* **Human contribution assessment:** 
  * **Colour-key confidence/likelihood:** **medium confidence** (pale cream) [VIS:Table_2_1:p063]
  * **Text annotation:** **"Main driver"** [VIS:Table_2_1:p063]
- **Citations:** ['VIS:Table_2_1:p063']
- **Citation Details:** [{"id": "VIS:Table_2_1:p063", "modality": "table", "label": "Table 2.1", "pdf_page": 63, "printed_page": "47", "bbox": [40.0, 42.0, 570.0, 610.0], "crop_relpath": "data/advanced/crops/VIS_Table_2_1_p063.png"}]
- **Inspected Crops:** ['VIS:Table_2_1:p063']

## adv_test_04 [table] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** According to Table 3.1 (p.100 / printed p.84), compare Category C1 (including subsets C1a and C1b) versus Category C2 on: (1) the median 5-year timing, [5–95th percentile] interval, and (% net zero pathways) for reaching 'Net zero GHGs', and (2) median [5–95th percentile] 'Cumulative CO2 emissions [Gt CO2]' from '2020–2100'.
- **Expected Answer:** Net zero GHGs timing (% pathways): C1 = 2095–2100 (52%) [2050–...]; subset C1a = 2070–2075 (100%) [2050–2090]; subset C1b = ...–... (0%) [...–...]; C2 = 2070–2075 (87%) [2055–...]. Cumulative CO2 emissions 2020–2100 (GtCO2): C1 = 320 [-210–570]; C1a = 160 [-220–620]; C1b = 360 [10–540]; C2 = 400 [-90–620].
- **Gold Source:** pages `[100]`, regions `['VIS:Table_3_1:p100']`, note: Verified from VIS_Table_3_1_p100.png (PDF p.100, printed p.84).
- **Agent Answer:** According to **Table 3.1** (p. 100 / printed p. 84) of the IPCC AR6 Synthesis Report, the comparison between **Category C1** (including subsets **C1a** and **C1b**) and **Category C2** is as follows [VIS:Table_3_1:p100]:

---

### **1. Net zero GHGs: Median 5-year timing, [5–95th percentile], and (% net zero pathways)**

*(Note: In Table 3.1, round brackets denote the percentage of pathways reaching net zero GHGs; square brackets denote the 5th–95th percentile range; three dots `…` indicate that net zero is not reached for that percentile or occurs after 2100)* [VIS:Table_3_1:p100].

* **Category C1 (overall)** (*limit warming to 1.5°C (>50%) with no or limited overshoot*):
  * **Median 5-year timing:** **2095–2100** [VIS:Table_3_1:p100]
  * **(% net zero pathways):** **(52%)** [VIS:Table_3_1:p100]
  * **[5–95th percentile] interval:** **[2050–…]** [VIS:Table_3_1:p100]
* **Subset C1a** (*with net zero GHGs*):
  * **Median 5-year timing:** **2070–2075** [VIS:Table_3_1:p100]
  * **(% net zero pathways):** **(100%)** [VIS:Table_3_1:p100]
  * **[5–95th percentile] interval:** **[2050–2090]** [VIS:Table_3_1:p100]
* **Subset C1b** (*without net zero GHGs*):
  * **Median 5-year timing:** **…–…** *(not reached)* [VIS:Table_3_1:p100]
  * **(% net zero pathways):** **(0%)** [VIS:Table_3_1:p100]
  * **[5–95th percentile] interval:** **[…–…]** [VIS:Table_3_1:p100]
* **Category C2** (*return warming to 1.5°C (>50%) after a high overshoot*):
  * **Median 5-year timing:** **2070–2075** [VIS:Table_3_1:p100]
  * **(% net zero pathways):** **(87%)** [VIS:Table_3_1:p100]
  * **[5–95th percentile] interval:** **[2055–…]** [VIS:Table_3_1:p100]

---

### **2. Cumulative CO₂ emissions from 2020–2100 [Gt CO₂]: Median [5–95th percentile]**

* **Category C1 (overall):** **320 [–210 to 570] Gt CO₂** [VIS:Table_3_1:p100]
  * **Subset C1a:** **160 [–220 to 620] Gt CO₂** [VIS:Table_3_1:p100]
  * **Subset C1b:** **360 [10 to 540] Gt CO₂** [VIS:Table_3_1:p100]
* **Category C2:** **400 [–90 to 620] Gt CO₂** [VIS:Table_3_1:p100]

---

### **Summary Comparison**
* **Net zero GHG timing & share:** A higher percentage of pathways in Category C2 reach net zero GHGs (87%) compared to Category C1 overall (52%), with C2 reaching net zero GHGs earlier at the median (2070–2075 vs 2095–2100). Within C1, subset C1a explicitly consists of pathways reaching 100% net zero GHGs (median 2070–2075), while subset C1b consists of pathways where 0% reach net zero GHGs [VIS:Table_3_1:p100].
* **Cumulative CO₂ (2020–2100):** Median cumulative CO₂ emissions for Category C1 (320 Gt CO₂) are lower than for Category C2 (400 Gt CO₂). Subset C1a has the lowest median cumulative emissions (160 Gt CO₂) due to greater net-negative CO₂ deployment in the second half of the century, whereas subset C1b has a median of 360 Gt CO₂ [VIS:Table_3_1:p100].
- **Citations:** ['VIS:Table_3_1:p100']
- **Citation Details:** [{"id": "VIS:Table_3_1:p100", "modality": "table", "label": "Table 3.1", "pdf_page": 100, "printed_page": "84", "bbox": [35.0, 40.0, 568.0, 675.0], "crop_relpath": "data/advanced/crops/VIS_Table_3_1_p100.png"}]
- **Inspected Crops:** ['VIS:Table_3_1:p100']

## adv_test_05 [table] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure 4.6 (p.129 / printed p.113), looking at the 'Multiplication factors*' columns (Lower range and Upper range) across both 'By sector' and 'By region', which sector has the highest upper-range multiplication factor (state its lower and upper factors), and which three regions have the highest lower-range multiplication factors (state all their lower and upper factors)?
- **Expected Answer:** Highest sector: Agriculture, forestry and other land use (x10 lower range, x31 upper range). Highest lower-range regions: Middle East is highest (x14 lower, x28 upper), followed by Southern Asia (x7 lower, x14 upper) and Eastern Europe and West-Central Asia (x7 lower, x15 upper).
- **Gold Source:** pages `[129]`, regions `['VIS:Table_4_6_Multipliers:p129', 'VIS:Figure_4_6:p129']`, note: Verified from VIS_Table_4_6_Multipliers_p129.png (PDF p.129); raw PDF text extraction scrambles these columns.
- **Agent Answer:** Based on Figure 4.6 (p. 129 / printed p. 113) [VIS:Table_4_6_Multipliers:p129] [VIS:Figure_4_6:p129]:

### Sector with the Highest Upper-Range Multiplication Factor:
* **Agriculture, forestry and other land use** [VIS:Table_4_6_Multipliers:p129]:
  * **Lower range:** x10
  * **Upper range:** x31

---

### Three Regions with the Highest Lower-Range Multiplication Factors:
1. **Middle East** [VIS:Table_4_6_Multipliers:p129]:
   * **Lower range:** x14
   * **Upper range:** x28
2. **Eastern Europe and West-Central Asia** [VIS:Table_4_6_Multipliers:p129]:
   * **Lower range:** x7
   * **Upper range:** x15
3. **Southern Asia** [VIS:Table_4_6_Multipliers:p129]:
   * **Lower range:** x7
   * **Upper range:** x14

*(Note: Eastern Europe and West-Central Asia and Southern Asia are tied for the second-highest lower-range multiplication factor at x7, followed by South-East Asia and Pacific at x6).*
- **Citations:** ['VIS:Table_4_6_Multipliers:p129', 'VIS:Figure_4_6:p129']
- **Citation Details:** [{"id": "VIS:Table_4_6_Multipliers:p129", "modality": "table", "label": "Figure 4.6 Multiplication Factors Table", "pdf_page": 129, "printed_page": "113", "bbox": [45.0, 74.0, 575.0, 472.0], "crop_relpath": "data/advanced/crops/VIS_Table_4_6_Multipliers_p129.png"}, {"id": "VIS:Figure_4_6:p129", "modality": "chart", "label": "Figure 4.6", "pdf_page": 129, "printed_page": "113", "bbox": [45.0, 45.0, 570.0, 495.0], "crop_relpath": "data/advanced/crops/VIS_Figure_4_6_p129.png"}]
- **Inspected Crops:** ['VIS:Table_4_6_Multipliers:p129']

## adv_test_06 [table] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure SPM.7 panel (a) (p.43 / printed p.27) under 'LAND, WATER, FOOD' in the 'Climate responses and adaptation options' table, which single option receives 'High' (dark navy) in BOTH 'Potential feasibility up to 1.5°C' and 'Synergies with mitigation' (give its confidence dots), and what are the corresponding ratings and confidence dots for 'Efficient livestock systems' and 'Agroforestry'?
- **Expected Answer:** Forest-based adaptation is the only option under LAND, WATER, FOOD with High feasibility (3 dots / High confidence) and High synergies with mitigation (3 dots / High confidence). Efficient livestock systems has Low feasibility (2 dots / Medium confidence) and Medium synergies (2 dots / Medium confidence). Agroforestry has Medium feasibility (2 dots / Medium confidence) and High synergies (3 dots / High confidence).
- **Gold Source:** pages `[43]`, regions `['VIS:Table_SPM7_Feasibility:p043']`, note: Verified from VIS_Table_SPM7_Feasibility_p043.png (PDF p.43, printed p.27).
- **Agent Answer:** Based on Figure SPM.7 panel (a) (*Feasibility of climate responses and adaptation, and potential of mitigation options in the near term*, p. 43 / printed p. 27) [VIS:Table_SPM7_Feasibility:p043], under the **'LAND, WATER, FOOD'** section of the climate responses and adaptation options table:

1. **Option receiving 'High' in BOTH categories:**
   * **Forest-based adaptation** [VIS:Table_SPM7_Feasibility:p043]
     * **Potential feasibility up to 1.5°C:** High (dark navy), High confidence (•••) [VIS:Table_SPM7_Feasibility:p043]
     * **Synergies with mitigation:** High (dark navy), High confidence (•••) [VIS:Table_SPM7_Feasibility:p043]

2. **Ratings and confidence dots for 'Efficient livestock systems':**
   * **Potential feasibility up to 1.5°C:** Low (light purple), Medium confidence (••) [VIS:Table_SPM7_Feasibility:p043]
   * **Synergies with mitigation:** Medium (medium purple), Medium confidence (••) [VIS:Table_SPM7_Feasibility:p043]

3. **Ratings and confidence dots for 'Agroforestry':**
   * **Potential feasibility up to 1.5°C:** Medium (medium purple), Medium confidence (••) [VIS:Table_SPM7_Feasibility:p043]
   * **Synergies with mitigation:** High (dark navy), High confidence (•••) [VIS:Table_SPM7_Feasibility:p043]
- **Citations:** ['VIS:Table_SPM7_Feasibility:p043']
- **Citation Details:** [{"id": "VIS:Table_SPM7_Feasibility:p043", "modality": "table", "label": "Figure SPM.7 Adaptation Feasibility Table", "pdf_page": 43, "printed_page": "27", "bbox": [50.0, 56.0, 412.0, 628.0], "crop_relpath": "data/advanced/crops/VIS_Table_SPM7_Feasibility_p043.png"}]
- **Inspected Crops:** ['VIS:Table_SPM7_Feasibility:p043']

## adv_test_07 [diagram_map] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure SPM.1 panel (b) ('Attribution of observed physical climate changes to human influence', p.23 / printed p.7), list all eight physical climate change drivers grouped under their four assessed confidence/likelihood banners ('Medium confidence', 'Likely', 'Very likely', 'Virtually certain').
- **Expected Answer:** Medium confidence: Increase in agricultural & ecological drought, Increase in fire weather, Increase in compound flooding. Likely: Increase in heavy precipitation. Very likely: Glacier retreat, Global sea level rise. Virtually certain: Upper ocean acidification, Increase in hot extremes.
- **Gold Source:** pages `[23]`, regions `['VIS:Figure_SPM1:p023']`, note: Verified from VIS_Figure_SPM1_p023.png panel (b).
- **Agent Answer:** In **Figure SPM.1 panel (b)** (*'Attribution of observed physical climate changes to human influence'*, p. 23 / printed p. 7), the eight physical climate change drivers are grouped under their four assessed confidence/likelihood banners as follows [VIS:Figure_SPM1:p023]:

1. **Medium confidence:**
   - Increase in agricultural & ecological drought
   - Increase in fire weather
   - Increase in compound flooding

2. **Likely:**
   - Increase in heavy precipitation

3. **Very likely:**
   - Glacier retreat
   - Global sea level rise

4. **Virtually certain:**
   - Upper ocean acidification
   - Increase in hot extremes
- **Citations:** ['VIS:Figure_SPM1:p023']
- **Citation Details:** [{"id": "VIS:Figure_SPM1:p023", "modality": "diagram_map", "label": "Figure SPM.1", "pdf_page": 23, "printed_page": "7", "bbox": [45.0, 48.0, 565.0, 745.0], "crop_relpath": "data/advanced/crops/VIS_Figure_SPM1_p023.png"}]
- **Inspected Crops:** ['VIS:Figure_SPM1:p023']

## adv_test_08 [diagram_map] — `status=answered` | `searches=1` | `inspects=2` | `err=None`
- **Question:** In Figure 2.3a (p.64 / printed p.48), examine the five hexagons GIC, NEU, WCE, EEU, and MED across the top two global maps: (1) under 'Hot extremes', what type of observed change and confidence dots are shown for each of those five codes, and (2) under 'Heavy precipitation', which of those five codes show an 'Increase' (teal) versus 'Low agreement in the type of change' (hatched grey), and with what confidence dots?
- **Expected Answer:** 1) Hot extremes: all five regions (GIC, NEU, WCE, EEU, MED) show Increase (pink), with Medium confidence (2 dots) for GIC and High confidence (3 dots) for NEU, WCE, EEU, and MED. 2) Heavy precipitation: GIC (teal Increase, 1 solid dot / Low due to limited agreement), NEU (teal Increase, 3 dots / High), WCE (teal Increase, 2 dots / Medium), and EEU (teal Increase, 2 dots / Medium), whereas MED shows Low agreement in the type of change (light hatched grey, 1 solid dot).
- **Gold Source:** pages `[64]`, regions `['VIS:Figure_2_3a:p064']`, note: Verified at 280 DPI in scratch/zoom_check/fig2_3a_hot_precip.png (PDF p.64).
- **Agent Answer:** Based on Figure 2.3 Panel (a) (p. 64 / printed p. 48) [VIS:Figure_2_3a:p064], the assessment for the five European/Greenland hexagons (GIC, NEU, WCE, EEU, and MED) is as follows:

### (1) Hot extremes (including heatwaves)
All five regions show an **Increase** (pink fill) in observed change since the 1950s [VIS:Figure_2_3a:p064]:
* **GIC** (Greenland/Iceland): **Increase**, with **Medium confidence** (•• / two dots) in human contribution [VIS:Figure_2_3a:p064].
* **NEU** (Northern Europe): **Increase**, with **High confidence** (••• / three dots) in human contribution [VIS:Figure_2_3a:p064].
* **WCE** (Western and Central Europe): **Increase**, with **High confidence** (••• / three dots) in human contribution [VIS:Figure_2_3a:p064].
* **EEU** (Eastern Europe): **Increase**, with **High confidence** (••• / three dots) in human contribution [VIS:Figure_2_3a:p064].
* **MED** (Mediterranean): **Increase**, with **High confidence** (••• / three dots) in human contribution [VIS:Figure_2_3a:p064].

---

### (2) Heavy precipitation
The five regions are split between 'Increase' and 'Low agreement in the type of change' [VIS:Figure_2_3a:p064]:

* **Increase** (teal):
  * **GIC**: **Increase**, with **Low confidence due to limited agreement** (• / single filled dot) in human contribution [VIS:Figure_2_3a:p064].
  * **NEU**: **Increase**, with **High confidence** (••• / three dots) in human contribution [VIS:Figure_2_3a:p064].
  * **WCE**: **Increase**, with **Medium confidence** (•• / two dots) in human contribution [VIS:Figure_2_3a:p064].

* **Low agreement in the type of change** (hatched grey):
  * **EEU**: **Low agreement in the type of change** (diagonal hatching), with **no confidence dots** shown [VIS:Figure_2_3a:p064].
  * **MED**: **Low agreement in the type of change** (diagonal hatching), with **no confidence dots** shown [VIS:Figure_2_3a:p064].
- **Citations:** ['VIS:Figure_2_3a:p064']
- **Citation Details:** [{"id": "VIS:Figure_2_3a:p064", "modality": "chart", "label": "Figure 2.3 Panel (a)", "pdf_page": 64, "printed_page": "48", "bbox": [35.0, 45.0, 565.0, 745.0], "crop_relpath": "data/advanced/crops/VIS_Figure_2_3a_p064.png"}]
- **Inspected Crops:** ['VIS:Figure_2_3a:p064']

## adv_test_09 [diagram_map] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure 3.3 panel (e) (p.92 / printed p.76), examine the bottom row of five polar burning-ember diagrams (three Arctic, two Antarctic): list all five diagram titles, identify which indicator transitions into 'Very high' risk (deep purple) at the lowest warming level (below 2°C, around 1.5–2°C, with its confidence dots), and identify which indicator delays its transition into 'Very high' risk until ~3–4°C.
- **Expected Answer:** The five bottom-row indicators are: (1) Sea-ice ecosystems from sea-ice change in the Arctic, (2) Changes in fisheries catch for Pollock and Pacific Cod in the Arctic, (3) Costs and losses for key infrastructure in the Arctic, (4) Sea-ice dependent ecosystems in the Antarctic, and (5) Changes in krill fisheries in the Antarctic. 'Sea-ice ecosystems from sea-ice change in the Arctic' transitions into 'Very high' risk (deep purple) at the lowest warming (~1.5–2°C, with 2 dots / Medium confidence). 'Changes in fisheries catch for Pollock and Pacific Cod in the Arctic' delays its transition to 'Very high' risk until around 3–4°C (with 3 dots / High confidence).
- **Gold Source:** pages `[92]`, regions `['VIS:Figure_3_3_reg:p092']`, note: Verified at 280 DPI in scratch/zoom_check/fig3_3e_polar.png (PDF p.92).
- **Agent Answer:** Based on Figure 3.3 panel (e) (*Examples of key risks in different regions*, p. 92 / printed p. 76) [VIS:Figure_3_3_reg:p092]:

### 1. The Five Polar Burning-Ember Diagram Titles
From left to right across the bottom row:
* **Arctic (three diagrams):**
  1. *Sea-ice ecosystems from sea-ice change in the Arctic*
  2. *Changes in fisheries catch for Pollock and Pacific Cod in the Arctic*
  3. *Costs and losses for key infrastructure in the Arctic*
* **Antarctic (two diagrams):**
  4. *Sea-ice dependent ecosystems in the Antarctic*
  5. *Changes in krill fisheries in the Antarctic*

---

### 2. Transition into 'Very High' Risk at the Lowest Warming Level (<2°C, ~1.5–2°C)
* **Indicator:** **"Sea-ice ecosystems from sea-ice change in the Arctic"**
* **Details:** This ember transitions into the 'Very high' risk level (deep purple) below 2°C (at approximately 1.6–1.7°C), marked with **two confidence dots (●●, medium confidence)** at the transition [VIS:Figure_3_3_reg:p092].

---

### 3. Transition into 'Very High' Risk Delayed until ~3–4°C
* **Indicator:** **"Costs and losses for key infrastructure in the Arctic"**
* **Details:** Unlike the ecological indicators, this infrastructure risk transitions to 'Very high' risk (deep purple) only at higher warming levels, occurring between approximately **3.5°C and 4°C** (with one confidence dot, ●, low confidence) [VIS:Figure_3_3_reg:p092].
- **Citations:** ['VIS:Figure_3_3_reg:p092']
- **Citation Details:** [{"id": "VIS:Figure_3_3_reg:p092", "modality": "diagram_map", "label": "Figure 3.3 Panels (c)-(d)", "pdf_page": 92, "printed_page": "76", "bbox": [35.0, 45.0, 565.0, 745.0], "crop_relpath": "data/advanced/crops/VIS_Figure_3_3_reg_p092.png"}]
- **Inspected Crops:** ['VIS:Figure_3_3_reg:p092']

## adv_test_10 [diagram_map] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure 4.3 panel (a) ('Increase in the population exposed to sea level rise from 2020 to 2040' under SSP2-4.5, p.116 / printed p.100), report the 2020 baseline exposed population (in millions) and the additional population exposed from 2020 to 2040 (both in millions and percent increase) for Asia, Africa, Europe, and Small Islands.
- **Expected Answer:** Asia: 63.81 million in 2020, +16.36 million (26%) additional by 2040. Africa: 2.40 million in 2020, +2.29 million (95%) additional by 2040. Europe: 0.67 million in 2020, +0.38 million (57%) additional by 2040. Small Islands: 0.18 million in 2020, +0.10 million (57%) additional by 2040.
- **Gold Source:** pages `[116]`, regions `['VIS:Figure_4_3:p116']`, note: Verified from VIS_Figure_4_3_p116.png panel (a).
- **Agent Answer:** Based on Figure 4.3 panel (a) ("Increase in the population exposed to sea level rise from 2020 to 2040", printed p. 100 / pdf p. 116) [VIS:Figure_4_3:p116], the 2020 baseline population exposed to a 100-year coastal flooding event and the additional population exposed from 2020 to 2040 under scenario SSP2-4.5 are as follows:

- **Asia**:
  - **2020 baseline exposed population**: 63.81 million
  - **Additional population exposed (2020–2040)**: +16.36 million (a 26% increase)

- **Africa**:
  - **2020 baseline exposed population**: 2.40 million
  - **Additional population exposed (2020–2040)**: +2.29 million (a 95% increase)

- **Europe**:
  - **2020 baseline exposed population**: 0.67 million
  - **Additional population exposed (2020–2040)**: +0.38 million (a 57% increase)

- **Small Islands**:
  - **2020 baseline exposed population**: 0.18 million
  - **Additional population exposed (2020–2040)**: +0.10 million (a 57% increase)
- **Citations:** ['VIS:Figure_4_3:p116']
- **Citation Details:** [{"id": "VIS:Figure_4_3:p116", "modality": "diagram_map", "label": "Figure 4.3", "pdf_page": 116, "printed_page": "100", "bbox": [35.0, 42.0, 565.0, 748.0], "crop_relpath": "data/advanced/crops/VIS_Figure_4_3_p116.png"}]
- **Inspected Crops:** ['VIS:Figure_4_3:p116']

## adv_test_11 [diagram_map] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** According to Figure SPM.6 (p.41 / printed p.25), what three societal actor groups are depicted in the left-side interacting diagram icon, and list the conditions shown under both 'Conditions that enable individual and collective actions' and 'Conditions that constrain individual and collective actions'.
- **Expected Answer:** The three interacting actor groups are Governments, Civil society, and Private sector. Enabling conditions (7): Inclusive governance; Diverse knowledges and values; Finance and innovation; Integration across sectors and time scales; Ecosystem stewardship; Synergies between climate and development actions; Behavioural change supported by policy, infrastructure and socio-cultural factors. Constraining conditions (5): Poverty, inequity and injustice; Economic, institutional, social and capacity barriers; Siloed responses; Lack of finance, and barriers to finance and technology; Tradeoffs with SDGs.
- **Gold Source:** pages `[41]`, regions `['VIS:Figure_SPM6:p041']`, note: Verified from VIS_Figure_SPM6_p041.png (PDF p.41, printed p.25).
- **Agent Answer:** According to **Figure SPM.6** (p. 41 / printed p. 25) [VIS:Figure_SPM6:p041]:

### **Three Societal Actor Groups**
Depicted in the left-side interacting diagram icon with bidirectional arrows between them [VIS:Figure_SPM6:p041]:
1. **Governments**
2. **Civil society**
3. **Private sector**

---

### **Conditions that enable individual and collective actions**
The diagram lists the following conditions [VIS:Figure_SPM6:p041]:
* Inclusive governance
* Diverse knowledges and values
* Finance and innovation
* Integration across sectors and time scales
* Ecosystem stewardship
* Synergies between climate and development actions
* Behavioural change supported by policy, infrastructure and socio-cultural factors

---

### **Conditions that constrain individual and collective actions**
The diagram lists the following conditions [VIS:Figure_SPM6:p041]:
* Poverty, inequity and injustice
* Economic, institutional, social and capacity barriers
* Siloed responses
* Lack of finance, and barriers to finance and technology
* Tradeoffs with SDGs
- **Citations:** ['VIS:Figure_SPM6:p041']
- **Citation Details:** [{"id": "VIS:Figure_SPM6:p041", "modality": "diagram_map", "label": "Figure SPM.6", "pdf_page": 41, "printed_page": "25", "bbox": [45.0, 52.0, 565.0, 750.0], "crop_relpath": "data/advanced/crops/VIS_Figure_SPM6_p041.png"}]
- **Inspected Crops:** ['VIS:Figure_SPM6:p041']

## adv_test_12 [diagram_map] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure 4.5 (p.125 / printed p.109), using the colour key (Synergies = solid blue, Trade-offs = solid orange, Both synergies and trade-offs/mixed = blue/orange hatched, Limited/no evidence = white), examine the rows for SDG 6 (Clean Water and Sanitation) and SDG 15 (Life on Land): in which columns does each row contain solid orange 'Trade-offs', which columns are 100% solid blue 'Synergies', and which columns are completely white ('Limited evidence/no evidence/no assessment')?
- **Expected Answer:** SDG 6 (Clean Water and Sanitation): solid orange Trade-offs appear in Energy systems Mitigation (alongside blue and hatched) and Industry Mitigation (alongside blue and white); Energy systems Adaptation and Urban and infrastructure Adaptation are 100% solid blue Synergies; no column is completely white. SDG 15 (Life on Land): solid orange Trade-offs appear prominently in Industry Mitigation (between blue and white); Land system Adaptation is 100% solid blue Synergies; Urban and infrastructure Adaptation is completely white (Limited/no evidence).
- **Gold Source:** pages `[125]`, regions `['VIS:Figure_4_5:p125']`, note: Verified at 280 DPI in scratch/zoom_check/fig4_5_sdg.png (PDF p.125).
- **Agent Answer:** Based on **Figure 4.5** (*Potential synergies and trade-offs between the portfolio of climate change mitigation and adaptation options and the Sustainable Development Goals (SDGs)*, p. 125 / printed p. 109) [VIS:Figure_4_5:p125], the breakdown for each specified SDG row across the nine sectoral columns is as follows:

---

### **1. SDG 6: Clean Water and Sanitation**
* **Columns containing solid orange ('Trade-offs')**:
  * **Energy systems – Mitigation** (contains solid blue, hatched blue/orange, and a solid orange segment) [VIS:Figure_4_5:p125]
  * **Industry – Mitigation** (contains solid blue, solid orange, and white segments) [VIS:Figure_4_5:p125]
* **Columns that are 100% solid blue ('Synergies')**:
  * **Energy systems – Adaptation** [VIS:Figure_4_5:p125]
  * **Urban and infrastructure – Adaptation** [VIS:Figure_4_5:p125]
* **Columns that are completely white ('Limited evidence/no evidence/no assessment')**:
  * **None** (all nine columns contain assessed synergies, trade-offs, and/or mixed impacts) [VIS:Figure_4_5:p125]

---

### **2. SDG 15: Life on Land**
* **Columns containing solid orange ('Trade-offs')**:
  * **Industry – Mitigation** (contains a distinct solid orange segment alongside solid blue and white) [VIS:Figure_4_5:p125]
* **Columns that are 100% solid blue ('Synergies')**:
  * **Land system – Adaptation** [VIS:Figure_4_5:p125]
* **Columns that are completely white ('Limited evidence/no evidence/no assessment')**:
  * **Urban and infrastructure – Adaptation** (entire bar is an unshaded/empty white box) [VIS:Figure_4_5:p125]
- **Citations:** ['VIS:Figure_4_5:p125']
- **Citation Details:** [{"id": "VIS:Figure_4_5:p125", "modality": "diagram_map", "label": "Figure 4.5", "pdf_page": 125, "printed_page": "109", "bbox": [45.0, 45.0, 570.0, 645.0], "crop_relpath": "data/advanced/crops/VIS_Figure_4_5_p125.png"}]
- **Inspected Crops:** ['VIS:Figure_4_5:p125']

## adv_test_13 [chart] — `status=answered` | `searches=2` | `inspects=1` | `err=None`
- **Question:** In Figure 4.4 panel (b) ('Potential of demand-side mitigation options by 2050', p.119 / printed p.103), state the percentage of possible reduction shown for each of the five rows (Food, Land transport, Buildings, Industry, and Electricity), the overall annotated reduction range across the end-use sectors, and the special qualification attached to Electricity.
- **Expected Answer:** Possible reduction percentages in 2050: Food = 44%, Land transport = 67%, Buildings = 66%, Industry = 29%, and Electricity = 73% reduction (before additional electrification), with a dark grey bar noting 'Additional electrification (+60%)'. Overall annotation: 'the range of GHG emissions reduction potential is 40–70% in these end-use sectors' (grouping Food, Land transport, and Buildings).
- **Gold Source:** pages `[119, 120]`, regions `['VIS:Figure_4_4:p119']`, note: Verified from VIS_Figure_4_4_p119.png (PDF p.119) panel (b).
- **Agent Answer:** Based on Figure 4.4 panel (b) (*Potential of demand-side mitigation options by 2050*, p. 119 [VIS:Figure_4_4:p119]; see also [ADV_TXT:p120:c06]):

### 1. Percentage of Possible Reduction by Row
* **Food:** **44%** [VIS:Figure_4_4:p119]
* **Land transport:** **67%** [VIS:Figure_4_4:p119]
* **Buildings:** **66%** [VIS:Figure_4_4:p119]
* **Industry:** **29%** [VIS:Figure_4_4:p119]
* **Electricity:** **73%** reduction (before additional electrification) [VIS:Figure_4_4:p119]

---

### 2. Overall Annotated Reduction Range Across End-Use Sectors
* An annotated bracket encompassing the end-use sectors (Food, Land transport, and Buildings) indicates that **"the range of GHG emissions reduction potential is 40–70% in these end-use sectors"** [VIS:Figure_4_4:p119], [ADV_TXT:p120:c06].

---

### 3. Special Qualification Attached to Electricity
* The reduction percentage for Electricity is explicitly qualified as **"73% reduction (before additional electrification)"** [VIS:Figure_4_4:p119].
* It includes an accompanying dark grey bar representing **"Additional electrification (+60%)"** [VIS:Figure_4_4:p119], which reflects the projected increase in electricity demand above the 2050 baseline due to increasing electrification in the other sectors [ADV_TXT:p120:c06]. The green arrow shows that this projected increase in electricity demand can be avoided through demand-side mitigation options [ADV_TXT:p120:c06].
- **Citations:** ['VIS:Figure_4_4:p119', 'ADV_TXT:p120:c06']
- **Citation Details:** [{"id": "VIS:Figure_4_4:p119", "modality": "chart", "label": "Figure 4.4", "pdf_page": 119, "printed_page": "103", "bbox": [45.0, 45.0, 570.0, 750.0], "crop_relpath": "data/advanced/crops/VIS_Figure_4_4_p119.png"}, {"id": "ADV_TXT:p120:c06", "modality": "text", "label": "Section 4: Near-Term Responses (p.104)", "pdf_page": 120, "printed_page": "104", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** ['VIS:Figure_4_4:p119']

## adv_test_14 [chart] — `status=answered` | `searches=4` | `inspects=1` | `err=None`
- **Question:** In Figure 4.1 panel (a) ('Sectoral emissions in pathways that limit warming to 1.5°C', p.110 / printed p.94), approximately when do the median lines for 'Land-use change' and 'Energy supply (including electricity)' cross the '-100% (net zero)' line (marked by solid dots), and do 'Transport, industry and buildings' or 'Non-CO2 emissions' reach -100% by 2050?
- **Expected Answer:** In Figure 4.1 panel (a), 'Land-use change' (green solid circle) reaches -100% (net zero) right at 2030 (going below -125% after 2040), and 'Energy supply (including electricity)' (blue solid circle) reaches -100% (net zero) shortly after 2040 (around ~2041–2042). Neither 'Transport, industry and buildings' (around ~-70% in 2050) nor 'Non-CO2 emissions' (around ~-45% in 2050) reaches -100% (net zero) by 2050.
- **Gold Source:** pages `[110, 111]`, regions `['VIS:Figure_4_1:p110']`, note: Verified from VIS_Figure_4_1_p110.png (PDF p.110) panel (a).
- **Agent Answer:** Based on Figure 4.1 panel (a) (*Sectoral emissions in pathways that limit warming to 1.5°C*, p. 110 / printed p. 94) [VIS:Figure_4_1:p110] [ADV_TXT:p110:c01]:

1. **Crossing of the -100% (net zero) line:**
   - **Land-use change** (green line): The median line crosses the solid horizontal **-100% (net zero)** line around **2030** (approximately 2030–2031, indicated by a solid green dot on the -100% line) [VIS:Figure_4_1:p110].
   - **Energy supply (including electricity)** (blue line): The median line crosses the solid horizontal **-100% (net zero)** line around **2040** (approximately 2040–2041, indicated by a solid blue dot on the -100% line) [VIS:Figure_4_1:p110].

2. **Reaching -100% by 2050:**
   - **Neither sector reaches -100% by 2050** [VIS:Figure_4_1:p110] [ADV_TXT:p111:c01]:
     - **Transport, industry and buildings** (purple line) reaches approximately **-65% to -70%** relative to 2015 by 2050 (having crossed the -50% "halfway to net zero" line around 2040) [VIS:Figure_4_1:p110] [ADV_TXT:p110:c02].
     - **Non-CO2 emissions** (grey line) reaches approximately **-45% to -50%** by 2050 and does not reach net zero (as also noted in the figure caption, non-CO2 emissions do not typically reach zero) [VIS:Figure_4_1:p110] [ADV_TXT:p111:c01].
- **Citations:** ['VIS:Figure_4_1:p110', 'ADV_TXT:p110:c01', 'ADV_TXT:p111:c01', 'ADV_TXT:p110:c02']
- **Citation Details:** [{"id": "VIS:Figure_4_1:p110", "modality": "chart", "label": "Figure 4.1", "pdf_page": 110, "printed_page": "94", "bbox": [35.0, 42.0, 568.0, 748.0], "crop_relpath": "data/advanced/crops/VIS_Figure_4_1_p110.png"}, {"id": "ADV_TXT:p110:c01", "modality": "text", "label": "Section 4: Near-Term Responses (p.94)", "pdf_page": 110, "printed_page": "94", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p111:c01", "modality": "text", "label": "Section 4: Near-Term Responses (p.95)", "pdf_page": 111, "printed_page": "95", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p110:c02", "modality": "text", "label": "Section 4: Near-Term Responses (p.94)", "pdf_page": 110, "printed_page": "94", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** ['VIS:Figure_4_1:p110']

## adv_test_15 [chart] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure SPM.5 (p.38 / printed p.22), what warming outcome (median °C, range, and confidence level) is annotated on panel (a) for 'Implemented policies', and in panel (e) what do bars below the zero 'net zero' line represent across the five Illustrative Mitigation Pathways (IMPs)?
- **Expected Answer:** On panel (a), implemented policies are annotated to result in projected emissions leading to warming of 3.2°C, with a range of 2.2°C to 3.5°C (medium confidence). In panel (e), bars below the zero ('net zero') line represent carbon Sinks (net negative CO2 emissions/removals from Land-use change and forestry and/or Energy supply including electricity) balancing positive emissions Sources above zero across IMP-GS, IMP-Neg, IMP-LD, IMP-SP, and IMP-Ren at the time of net zero CO2.
- **Gold Source:** pages `[38, 39]`, regions `['VIS:Figure_SPM5:p038']`, note: Verified from VIS_Figure_SPM5_p038.png (PDF p.38, printed p.22).
- **Agent Answer:** Based on **Figure SPM.5** (p. 38 / printed p. 22) [VIS:Figure_SPM5:p038]:

1. **Warming outcome for 'Implemented policies' (Panel a):**
   - **Median:** 3.2°C
   - **Range:** 2.2°C to 3.5°C
   - **Confidence level:** *medium confidence*
   *(Annotated as: "Implemented policies result in projected emissions that lead to warming of 3.2°C, with a range of 2.2°C to 3.5°C (medium confidence)")* [VIS:Figure_SPM5:p038].

2. **Bars below the zero ('net zero') line in Panel (e):**
   - The bars below the net-zero line represent emissions **Sinks** (removals / negative emissions) at the time net zero $\text{CO}_2$ is reached [VIS:Figure_SPM5:p038].
   - Across the five Illustrative Mitigation Pathways (IMPs: IMP-GS, IMP-Neg, IMP-LD, IMP-SP, IMP-Ren), these sinks consist of striped sectoral bars for:
     - **Land-use change and forestry** (green striped) [VIS:Figure_SPM5:p038]
     - **Energy supply (including electricity)** (blue striped) [VIS:Figure_SPM5:p038].
- **Citations:** ['VIS:Figure_SPM5:p038']
- **Citation Details:** [{"id": "VIS:Figure_SPM5:p038", "modality": "chart", "label": "Figure SPM.5", "pdf_page": 38, "printed_page": "22", "bbox": [45.0, 52.0, 565.0, 725.0], "crop_relpath": "data/advanced/crops/VIS_Figure_SPM5_p038.png"}]
- **Inspected Crops:** ['VIS:Figure_SPM5:p038']

## adv_test_16 [chart] — `status=answered` | `searches=3` | `inspects=1` | `err=None`
- **Question:** In Figure 2.3b panel (b) ('Vulnerability of population & per capita emissions per country in 2019', p.65 / printed p.49), what relationship is annotated between national vulnerability (vertical axis) and per-capita CO2 emissions across 180 nations, and roughly where on the horizontal axis (in tons of CO2 per capita) do the two rightmost high-emission outlier nations sit beyond 30 tons?
- **Expected Answer:** Panel (b) explicitly annotates 'more vulnerable countries generally have lower emissions per capita' (countries with the highest vulnerability indices ~55–90 cluster near 0–5 tCO2/capita). Beyond 30 tons of CO2 per capita, the two rightmost outlier nations sit around ~38–39 tons per capita (vulnerability ~22–23) and ~70–71 tons per capita (across the broken horizontal axis past 70, vulnerability ~34–35).
- **Gold Source:** pages `[65]`, regions `['VIS:Figure_2_3b:p065']`, note: Verified from VIS_Figure_2_3b_p065.png (PDF p.65, printed p.49) panel (b).
- **Agent Answer:** Based on Figure 2.3 panel (b) (*Vulnerability of population & per capita emissions per country in 2019*, page 65 / printed page 49) [VIS:Figure_2_3b:p065]:

1. **Annotated Relationship:** 
   A callout bracket pointing to the cluster of countries with higher vulnerability and lower emissions explicitly states: 
   *"more vulnerable countries generally have lower emissions per capita"* [ADV_TXT:p065:c01] [VIS:Figure_2_3b:p065]. 
   (An accompanying box also notes that vulnerability is assessed on national data, differs between and within countries, and is exacerbated by inequity and marginalisation) [ADV_TXT:p065:c02] [VIS:Figure_2_3b:p065].

2. **Positions of the Two Rightmost Outlier Nations Beyond 30 Tons:**
   On the horizontal axis (*2019 emissions per capita of 180 nations in tons of CO2*):
   - The first outlier sits at approximately **38 tons of CO₂ per capita** (just before the 40 tick mark) [VIS:Figure_2_3b:p065].
   - Following an axis break (`//`) between 40 and 70, the second and furthest right outlier sits at approximately **70 to 71 tons of CO₂ per capita** (just at/slightly past the 70 tick mark) [VIS:Figure_2_3b:p065].
- **Citations:** ['ADV_TXT:p065:c01', 'ADV_TXT:p065:c02', 'VIS:Figure_2_3b:p065']
- **Citation Details:** [{"id": "ADV_TXT:p065:c01", "modality": "text", "label": "Section 2: Current Status and Trends (p.49)", "pdf_page": 65, "printed_page": "49", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p065:c02", "modality": "text", "label": "Section 2: Current Status and Trends (p.49)", "pdf_page": 65, "printed_page": "49", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "VIS:Figure_2_3b:p065", "modality": "diagram_map", "label": "Figure 2.3 Panel (b)", "pdf_page": 65, "printed_page": "49", "bbox": [45.0, 45.0, 575.0, 745.0], "crop_relpath": "data/advanced/crops/VIS_Figure_2_3b_p065.png"}]
- **Inspected Crops:** ['VIS:Figure_2_3b:p065']

## adv_test_17 [chart] — `status=answered` | `searches=2` | `inspects=1` | `err=None`
- **Question:** In Figure 3.4 panel (a) (p.96 / printed p.80), what statistics are called out for 2050 regarding people exposed and the frequency of historical once-per-century extreme sea level events, what upper-bound warning is annotated at the top right for 2300 under very high emissions, and approximately what spans (in meters) do the 'low emissions' and 'very high emissions' scenario range bars cover in 2300?
- **Expected Answer:** By 2050: 1 billion people exposed, and extreme sea level events that occurred once per century will become 20–30 times more frequent. Top-right annotation: 'Sea level rise greater than 15m cannot be ruled out with very high emissions' (dashed storyline extending above 15 m). In 2300 (panel a bars relative to 1900; caption notes 0.3–3.1 m and 1.7–6.8 m relative to 1995–2014 + 0.16 m), the 'low emissions scenario range' bar spans roughly ~0.5 m to ~3.3 m, while the 'very high emissions scenario range' bar spans roughly ~1.9 m to ~6.9 m.
- **Gold Source:** pages `[96, 97]`, regions `['VIS:Figure_3_4:p096']`, note: Verified from VIS_Figure_3_4_p096.png (PDF p.96) panel (a) and caption on p.97.
- **Agent Answer:** Based on Figure 3.4 panel (a) and its accompanying caption in the IPCC AR6 Synthesis Report (Section 3, p. 80 / pdf p. 96–97) [VIS:Figure_3_4:p096] [ADV_TXT:p096:c02] [ADV_TXT:p097:c02]:

1. **Statistics called out for 2050** [VIS:Figure_3_4:p096] [ADV_TXT:p096:c02]:
   - **People exposed:** **1 billion** people exposed.
   - **Frequency of extreme sea level events:** *"Extreme sea level events that occured once per century will be **20–30 times more frequent**."*

2. **Upper-bound warning annotated at the top right for 2300** [VIS:Figure_3_4:p096] [ADV_TXT:p096:c01]:
   - Annotated at the top right with an arrow extending past the y-axis break is: *"**Sea level rise greater than 15m cannot be ruled out with very high emissions**"* (representing the low-likelihood, high-impact storyline including ice sheet instability processes under the very high emissions scenario) [VIS:Figure_3_4:p096] [ADV_TXT:p093:c10].

3. **Spans of scenario range bars in 2300** [VIS:Figure_3_4:p096] [ADV_TXT:p097:c02]:
   - **'low emissions scenario range' bar:** Spans from approximately **0.3 m to 3.1 m** relative to 1900 (representing the 17th–83rd percentile range for SSP1-2.6) [VIS:Figure_3_4:p096] [ADV_TXT:p097:c02].
   - **'very high emissions scenario range' bar:** The solid range bar spans from approximately **1.7 m to 6.8 m** relative to 1900 (representing the 17th–83rd percentile range for SSP5-8.5), with the dashed low-likelihood storyline extending upwards to in excess of **15 m** [VIS:Figure_3_4:p096] [ADV_TXT:p097:c02].
- **Citations:** ['VIS:Figure_3_4:p096', 'ADV_TXT:p096:c02', 'ADV_TXT:p097:c02', 'ADV_TXT:p096:c01', 'ADV_TXT:p093:c10']
- **Citation Details:** [{"id": "VIS:Figure_3_4:p096", "modality": "chart", "label": "Figure 3.4", "pdf_page": 96, "printed_page": "80", "bbox": [35.0, 45.0, 565.0, 745.0], "crop_relpath": "data/advanced/crops/VIS_Figure_3_4_p096.png"}, {"id": "ADV_TXT:p096:c02", "modality": "text", "label": "Section 3: Long-Term Futures (p.80)", "pdf_page": 96, "printed_page": "80", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p097:c02", "modality": "text", "label": "Section 3: Long-Term Futures (p.81)", "pdf_page": 97, "printed_page": "81", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p096:c01", "modality": "text", "label": "Section 3: Long-Term Futures (p.80)", "pdf_page": 96, "printed_page": "80", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p093:c10", "modality": "text", "label": "Section 3: Long-Term Futures (p.77)", "pdf_page": 93, "printed_page": "77", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** ['VIS:Figure_3_4:p096']

## adv_test_18 [chart] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure 3.3 panels (b) and (c) (p.91 / printed p.75), state the two quantitative coral-decline annotations on the 'Warm-water corals' ember and the two annotations on 'Wildfire damage', and explain how the risk level at 100 cm of sea level rise differs between 'Urban atoll islands' and 'Resource-rich coastal cities' under 'r (No-to-moderate response)' versus 'R (Maximum potential response)' in panel (c).
- **Expected Answer:** Warm-water corals annotations: 'e.g. coral reefs decline by 70–90%' (~1.5°C High risk) and 'e.g. coral reefs decline >99%' (~2°C Very high risk). Wildfire damage annotations: 'e.g. increase in the length of fire season' (~1.5°C) and 'e.g. over 100 million additional people exposed' (~4–5°C). In panel (c) at 100 cm SLR: 'Urban atoll islands' reaches deep purple (Very high risk) under 'r' and remains high-to-very-high (dark crimson) even under 'R'; whereas 'Resource-rich coastal cities' drops from High/orange under 'r' down to entirely Moderate/low (yellow to light cream) under 'R'.
- **Gold Source:** pages `[91, 93]`, regions `['VIS:Figure_3_3_rfc:p091']`, note: Verified from VIS_Figure_3_3_rfc_p091.png and high-DPI scratch/zoom_check/fig3_3c_coastal.png.
- **Agent Answer:** Based on **Figure 3.3** panels (b) and (c) (p. 91 / printed p. 75) [VIS:Figure_3_3_rfc:p091]:

### 1. Quantitative Coral-Decline Annotations on 'Warm-water corals'
The two callout annotations on the **Warm-water corals** ember are [VIS:Figure_3_3_rfc:p091]:
* **"e.g. coral reefs decline by 70–90%"** (annotated around 1.5°C of global warming)
* **"e.g. coral reefs decline >99%"** (annotated around 2°C of global warming)

---

### 2. Annotations on 'Wildfire damage'
The two callout annotations on the **Wildfire damage** ember are [VIS:Figure_3_3_rfc:p091]:
* **"e.g. increase in the length of fire season"** (annotated around 1.5°C of global warming)
* **"e.g. over 100 million additional people exposed"** (annotated around 4°C–4.5°C of global warming)

---

### 3. Risk Levels at 100 cm of Sea Level Rise in Panel (c)
At 100 cm of global mean sea level rise, the assessed risk levels differ as follows between the two geographies [VIS:Figure_3_3_rfc:p091]:

* **Urban atoll islands**:
  * **Under $r$ (No-to-moderate response)**: Risk reaches the **Very high** level (purple) [VIS:Figure_3_3_rfc:p091].
  * **Under $R$ (Maximum potential response)**: Risk remains at the **Very high** level (purple) [VIS:Figure_3_3_rfc:p091].
  * *Comparison*: For urban atoll islands, even implementing the maximum potential adaptation response ($R$) does not prevent the risk from reaching the **Very high** category at 100 cm of sea level rise, illustrating adaptation limits [VIS:Figure_3_3_rfc:p091].

* **Resource-rich coastal cities**:
  * **Under $r$ (No-to-moderate response)**: Risk reaches the **High** level (red) [VIS:Figure_3_3_rfc:p091].
  * **Under $R$ (Maximum potential response)**: Risk is reduced to the **Moderate** level (yellow) [VIS:Figure_3_3_rfc:p091].
  * *Comparison*: For resource-rich coastal cities, implementing the maximum potential response ($R$) substantially reduces risk from **High** down to **Moderate** at 100 cm of sea level rise [VIS:Figure_3_3_rfc:p091].
- **Citations:** ['VIS:Figure_3_3_rfc:p091']
- **Citation Details:** [{"id": "VIS:Figure_3_3_rfc:p091", "modality": "diagram_map", "label": "Figure 3.3 Panels (a)-(b)", "pdf_page": 91, "printed_page": "75", "bbox": [45.0, 45.0, 575.0, 745.0], "crop_relpath": "data/advanced/crops/VIS_Figure_3_3_rfc_p091.png"}]
- **Inspected Crops:** ['VIS:Figure_3_3_rfc:p091']

## adv_test_19 [multi_hop] — `status=answered` | `searches=2` | `inspects=1` | `err=None`
- **Question:** Combine Section 2.1.1 (p.60) and Figure 2.3b panel (c) (p.65): first state the 2019 per-capita net anthropogenic GHG emissions (excluding CO2-LULUCF) of Least Developed Countries (LDCs), Small Island Developing States (SIDS), and the global average; then from the 'Small Islands' column in Figure 2.3b panel (c), give the impact direction and confidence symbol/level for: (1) Flood/storm induced damages in coastal areas, (2) Damages to infrastructure, (3) Heat, malnutrition and harm from wildfire, and (4) Mental health.
- **Expected Answer:** From Section 2.1.1 (p.60, excluding CO2-LULUCF): 2019 per-capita emissions are 1.7 tCO2-eq for LDCs and 4.6 tCO2-eq for SIDS, well below the global average of 6.9 tCO2-eq. From Figure 2.3b panel (c) 'Small Islands' column: (1) Flood/storm induced damages in coastal areas = solid red Adverse impacts, High or very high confidence (3 dots); (2) Damages to infrastructure = solid red Adverse impacts, High or very high confidence (3 dots); (3) Heat, malnutrition and harm from wildfire = solid red Adverse impacts, High or very high confidence (3 dots); (4) Mental health = solid red Adverse impacts, '–' (Evidence limited, insufficient).
- **Gold Source:** pages `[60, 65]`, regions `['VIS:Figure_2_3b:p065']`, note: Verified from PDF p.60 text and high-DPI scratch/zoom_check/fig2_3b_matrix.png (PDF p.65).
- **Agent Answer:** Based on **Section 2.1.1 (p. 60)** and **Figure 2.3b panel (c) (p. 65)** of the IPCC AR6 Synthesis Report:

### 1. 2019 Per-Capita Net Anthropogenic GHG Emissions (excluding CO₂-LULUCF)
* **Least Developed Countries (LDCs):** 1.7 $\text{tCO}_2\text{-eq}$ per capita [ADV_TXT:p060:c02]
* **Small Island Developing States (SIDS):** 4.6 $\text{tCO}_2\text{-eq}$ per capita [ADV_TXT:p060:c02]
* **Global average:** 6.9 $\text{tCO}_2\text{-eq}$ per capita [ADV_TXT:p060:c02]

---

### 2. Observed Impacts for 'Small Islands' from Figure 2.3b Panel (c)
According to the legend of Figure 2.3b panel (c):
* Solid red/brown background = **Adverse impacts** [VIS:Figure_2_3b:p065]
* $\bullet\bullet\bullet$ = **High or very high confidence** [VIS:Figure_2_3b:p065]
* $-$ = **Evidence limited, insufficient** [VIS:Figure_2_3b:p065]

For the specified categories in the **Small Islands** column:
1. **Flood/storm induced damages in coastal areas:**
   * **Impact direction:** Adverse impacts [VIS:Figure_2_3b:p065]
   * **Confidence symbol/level:** $\bullet\bullet\bullet$ (High or very high confidence) [VIS:Figure_2_3b:p065]

2. **Damages to infrastructure:**
   * **Impact direction:** Adverse impacts [VIS:Figure_2_3b:p065]
   * **Confidence symbol/level:** $\bullet\bullet\bullet$ (High or very high confidence) [VIS:Figure_2_3b:p065]

3. **Heat, malnutrition and harm from wildfire:**
   * **Impact direction:** Adverse impacts [VIS:Figure_2_3b:p065]
   * **Confidence symbol/level:** $\bullet\bullet\bullet$ (High or very high confidence) [VIS:Figure_2_3b:p065]

4. **Mental health:**
   * **Impact direction:** Adverse impacts [VIS:Figure_2_3b:p065]
   * **Confidence symbol/level:** $-$ (Evidence limited, insufficient) [VIS:Figure_2_3b:p065]
- **Citations:** ['ADV_TXT:p060:c02', 'VIS:Figure_2_3b:p065']
- **Citation Details:** [{"id": "ADV_TXT:p060:c02", "modality": "text", "label": "Section 2: Current Status and Trends (p.44)", "pdf_page": 60, "printed_page": "44", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "VIS:Figure_2_3b:p065", "modality": "diagram_map", "label": "Figure 2.3 Panel (b)", "pdf_page": 65, "printed_page": "49", "bbox": [45.0, 45.0, 575.0, 745.0], "crop_relpath": "data/advanced/crops/VIS_Figure_2_3b_p065.png"}]
- **Inspected Crops:** ['VIS:Figure_2_3b:p065']

## adv_test_20 [multi_hop] — `status=answered` | `searches=2` | `inspects=1` | `err=None`
- **Question:** Combining Section 3.2 (p.95), Figure 3.4 panel (b) (p.96), and the Figure 3.4 caption on p.97: list the typical intended lifetimes of all six coastal risk-management measures in Figure 3.4 panel (b), state the likely global mean sea level rise ranges by 2100 (relative to 1995–2014) under SSP1-1.9 and SSP5-8.5, and report beyond what rate of sea level rise ecosystem-based solutions lose effectiveness.
- **Expected Answer:** Figure 3.4 panel (b) intended lifetimes: Ecosystem-based adaptation ≈15 years, Sediment-based protection ≈15 years, Elevating houses ≈30 years, Protect levees ≈50 years, Protect barriers ≈100 years, Planned relocation ≥100 years. Likely sea level rise by 2100 relative to 1995–2014 (p.97): 0.28 to 0.55 m (SSP1-1.9) and 0.63 to 1.01 m (SSP5-8.5) (medium confidence). Section 3.2 (p.95): ecosystem-based solutions lose effectiveness at high rates of sea level rise beyond 0.5 to 1 cm yr-1 (medium confidence).
- **Gold Source:** pages `[95, 96, 97]`, regions `['VIS:Figure_3_4:p096']`, note: Verified from PDF p.95 text, VIS_Figure_3_4_p096.png panel (b), and PDF p.97 caption.
- **Agent Answer:** Based on Section 3.2, Figure 3.4 panel (b), and the Figure 3.4 caption:

### 1. Typical Intended Lifetimes of the Six Coastal Risk-Management Measures
As shown in Figure 3.4 panel (b) [VIS:Figure_3_4:p096], the typical intended operational lifetimes are:
- **Ecosystem-based adaptation:** ≈15 years
- **Sediment-based protection:** ≈15 years
- **Elevating houses:** ≈30 years
- **Protect levees:** ≈50 years
- **Protect barriers:** ≈100 years
- **Planned relocation:** ≥100 years

---

### 2. Likely Global Mean Sea Level Rise Ranges by 2100 (relative to 1995–2014)
According to the caption of Figure 3.4 [VIS:Figure_3_4:p096], [ADV_TXT:p097:c03]:
- **SSP1-1.9 (very low GHG emissions scenario):** between **0.28 to 0.55 m** *(medium confidence)*
- **SSP5-8.5 (very high GHG emissions scenario):** between **0.63 to 1.01 m** *(medium confidence)*

---

### 3. Sea Level Rise Rate Beyond Which Ecosystem-Based Solutions Lose Effectiveness
According to Section 3.2 [ADV_TXT:p095:c02], ecosystem-based solutions (such as wetlands) lose effectiveness at high rates of sea level rise beyond **0.5 to 1 cm yr⁻¹** *(medium confidence)*.
- **Citations:** ['VIS:Figure_3_4:p096', 'ADV_TXT:p097:c03', 'ADV_TXT:p095:c02']
- **Citation Details:** [{"id": "VIS:Figure_3_4:p096", "modality": "chart", "label": "Figure 3.4", "pdf_page": 96, "printed_page": "80", "bbox": [35.0, 45.0, 565.0, 745.0], "crop_relpath": "data/advanced/crops/VIS_Figure_3_4_p096.png"}, {"id": "ADV_TXT:p097:c03", "modality": "text", "label": "Section 3: Long-Term Futures (p.81)", "pdf_page": 97, "printed_page": "81", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p095:c02", "modality": "text", "label": "Section 3: Long-Term Futures (p.79)", "pdf_page": 95, "printed_page": "79", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** ['VIS:Figure_3_4:p096']

## adv_test_21 [multi_hop] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** Combine Section 3.3.2 (p.101) and Figure 4.1 panel (b) (p.110): at the time of net zero GHG emissions in pathways limiting warming to 2°C (>67%) or lower, what residual quantity of non-CO2 emissions (CH4, N2O, and F-gases, median and range in GtCO2-eq yr-1) typically remains, what must counterbalance it, and which Illustrative Mitigation Pathway in Figure 4.1 panel (b) stands out for relying on large negative emissions in both Energy supply and Land-use change at the time of net zero CO2?
- **Expected Answer:** Section 3.3.2 (p.101): residual non-CO2 emissions (CH4, N2O, and F-gases) of about 8 [5–11] GtCO2-eq yr-1 remain at the time of net zero GHG and must be counterbalanced by net negative CO2 emissions (via Carbon Dioxide Removal, CDR). In Figure 4.1 panel (b) (p.110), IMP-Neg ('High reliance on net negative emissions', high overshoot) stands out by combining deep negative hatches (Sinks) in Energy supply (including electricity) as well as Land-use change and forestry below the zero line to offset remaining sources (especially Transport/industry/buildings and Non-CO2 emissions).
- **Gold Source:** pages `[101, 110, 111]`, regions `['VIS:Figure_4_1:p110']`, note: Verified from PDF p.101 (Section 3.3.2) and VIS_Figure_4_1_p110.png panel (b).
- **Agent Answer:** Based on Section 3.3.2 (p. 101) and Figure 4.1 panel (b) (p. 110):

1. **Residual non-CO2 emissions**: At the time of net zero GHG emissions in pathways limiting warming to 2°C (>67%) or lower, residual emissions of CH4, N2O, and F-gases typically remain at about **8 [5–11] GtCO2-eq yr⁻¹** (median of 8, with a range of 5–11 GtCO2-eq yr⁻¹) [ADV_TXT:p101:c03].
2. **What must counterbalance it**: These residual emissions must be **counterbalanced by net negative CO2 emissions** [ADV_TXT:p101:c03].
3. **Illustrative Mitigation Pathway**: In Figure 4.1 panel (b), the pathway that stands out for relying on large negative emissions (sinks below zero) in both **Energy supply (including electricity)** and **Land-use change and forestry** at the time of net zero CO2 is **IMP-Neg** (High reliance on net negative emissions) [VIS:Figure_4_1:p110].
- **Citations:** ['ADV_TXT:p101:c03', 'VIS:Figure_4_1:p110']
- **Citation Details:** [{"id": "ADV_TXT:p101:c03", "modality": "text", "label": "Section 3: Long-Term Futures (p.85)", "pdf_page": 101, "printed_page": "85", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "VIS:Figure_4_1:p110", "modality": "chart", "label": "Figure 4.1", "pdf_page": 110, "printed_page": "94", "bbox": [35.0, 42.0, 568.0, 748.0], "crop_relpath": "data/advanced/crops/VIS_Figure_4_1_p110.png"}]
- **Inspected Crops:** ['VIS:Figure_4_1:p110']

## adv_test_22 [multi_hop] — `status=answered` | `searches=3` | `inspects=1` | `err=None`
- **Question:** Combine Section 4.8.1 (p.127–128) and Figure 4.6 (p.129): what structural financing challenges facing developing countries are cited in Section 4.8.1 alongside the Paris Agreement's USD 100 billion-a-year goal context, and in Figure 4.6 ('By type of economy') what are the mitigation investment multiplication factors (Lower range and Upper range) needed until 2030 for 'Developing countries' versus 'Developed countries', as well as the global ratio stated in the footnote?
- **Expected Answer:** Section 4.8.1 (p.127–128): although there is sufficient global capital and liquidity, developing countries face macroeconomic barriers including indebtedness and economic vulnerability, up-front risks deterring projects, and weaker local capital markets (alongside calls for increased public/mobilised private finance in the context of the USD 100 billion-a-year Paris Agreement goal). In Figure 4.6 (p.129), Developing countries require a multiplication factor of x4 (lower) to x7 (upper), versus Developed countries at x3 (lower) to x5 (upper). The footnote states: 'Globally, current mitigation financial flows are a factor of three to six below the average levels up to 2030.'
- **Gold Source:** pages `[127, 128, 129]`, regions `['VIS:Figure_4_6:p129', 'VIS:Table_4_6_Multipliers:p129']`, note: Verified from PDF p.127–128 text and VIS_Table_4_6_Multipliers_p129.png / VIS_Figure_4_6_p129.png.
- **Agent Answer:** Based on Section 4.8.1 and Figure 4.6 of the IPCC AR6 Synthesis Report (Longer Report):

### 1. Structural Financing Challenges in Developing Countries (Section 4.8.1)
Alongside the context of the USD 100 billion-a-year goal of the Paris Agreement, Section 4.8.1 identifies the following structural challenges and barriers facing developing countries:
- **Inequities in finance and financial terms:** Inequities in access to finance, including higher finance costs, disadvantageous terms and conditions, and economic vulnerability to climate change [ADV_TXT:p128:c03].
- **Debt burden and economic instability:** Developing regions face high debt costs, debt distress, indebtedness, and macroeconomic uncertainty [ADV_TXT:p127:c07] [ADV_TXT:p128:c04].
- **Investment risk and market constraints:** Elevated investment risks requiring public guarantees to leverage private capital at lower cost, underdeveloped local capital markets, institutional/regulatory/market access barriers, and the need to build greater trust in international cooperation processes [ADV_TXT:p127:c07] [ADV_TXT:p128:c03] [ADV_TXT:p128:c04].

---

### 2. Mitigation Investment Multiplication Factors until 2030 (Figure 4.6, 'By type of economy')
The multiplication factors indicating the required fold-increase in annual mitigation financial flows to meet average annual mitigation investment needs up to 2030 are:
- **Developing countries:**
  - **Lower range:** **x4** [VIS:Table_4_6_Multipliers:p129]
  - **Upper range:** **x7** [VIS:Table_4_6_Multipliers:p129]
- **Developed countries:**
  - **Lower range:** **x3** [VIS:Table_4_6_Multipliers:p129]
  - **Upper range:** **x5** [VIS:Table_4_6_Multipliers:p129]

---

### 3. Global Ratio Stated in the Footnote
- The footnote states: *"Multiplication factors indicate the x-fold increase between yearly mitigation flows to average yearly mitigation investment needs. Globally, current mitigation financial flows are a **factor of three to six** below the average levels up to 2030"* [VIS:Table_4_6_Multipliers:p129].
- **Citations:** ['ADV_TXT:p127:c07', 'ADV_TXT:p128:c03', 'ADV_TXT:p128:c04', 'VIS:Table_4_6_Multipliers:p129']
- **Citation Details:** [{"id": "ADV_TXT:p127:c07", "modality": "text", "label": "Section 4: Near-Term Responses (p.111)", "pdf_page": 127, "printed_page": "111", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p128:c03", "modality": "text", "label": "Section 4: Near-Term Responses (p.112)", "pdf_page": 128, "printed_page": "112", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p128:c04", "modality": "text", "label": "Section 4: Near-Term Responses (p.112)", "pdf_page": 128, "printed_page": "112", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "VIS:Table_4_6_Multipliers:p129", "modality": "table", "label": "Figure 4.6 Multiplication Factors Table", "pdf_page": 129, "printed_page": "113", "bbox": [45.0, 74.0, 575.0, 472.0], "crop_relpath": "data/advanced/crops/VIS_Table_4_6_Multipliers_p129.png"}]
- **Inspected Crops:** ['VIS:Table_4_6_Multipliers:p129']

## adv_test_23 [text] — `status=answered` | `searches=1` | `inspects=0` | `err=None`
- **Question:** According to SPM B.1.1, B.1.2, and Footnote 30 (PDF p.28 / printed p.12), state the best estimates and [very likely ranges] of global warming for 2081–2100 across all five WGI GHG emissions scenarios (SSP1-1.9 through SSP5-8.5), and within how many years discernible global surface temperature differences emerge between high and very-low emissions scenarios.
- **Expected Answer:** For 2081–2100 relative to 1850–1900 (Footnote 30): SSP1-1.9 = 1.4 [1.0 to 1.8]°C; SSP1-2.6 = 1.8 [1.3 to 2.4]°C; SSP2-4.5 = 2.7 [2.1 to 3.5]°C; SSP3-7.0 = 3.6 [2.8 to 4.6]°C; SSP5-8.5 = 4.4 [3.3 to 5.7]°C. Under B.1.2, discernible differences in trends of global surface temperature between contrasting scenarios emerge from natural variability within around 20 years (around two decades).
- **Gold Source:** pages `[28]`, regions `[]`, note: Verified verbatim in PDF p.28 (printed p.12), B.1.1, B.1.2, Footnote 30.
- **Agent Answer:** According to **SPM B.1.1** and **Footnote 30**, the best estimates and [very likely ranges] of global warming for 2081–2100 across all five WGI GHG emissions scenarios are [ADV_TXT:p028:c02] [ADV_TXT:p028:c05]:
- **SSP1-1.9:** 1.4 [1.0 to 1.8]°C
- **SSP1-2.6:** 1.8 [1.3 to 2.4]°C
- **SSP2-4.5:** 2.7 [2.1 to 3.5]°C
- **SSP3-7.0:** 3.6 [2.8 to 4.6]°C
- **SSP5-8.5:** 4.4 [3.3 to 5.7]°C

According to **SPM B.1.2**, discernible differences in trends of global surface temperature between contrasting GHG emissions scenarios (SSP1-1.9 and SSP1-2.6 vs. SSP3-7.0 and SSP5-8.5) would begin to emerge from natural variability **within around 20 years** [ADV_TXT:p028:c03].
- **Citations:** ['ADV_TXT:p028:c02', 'ADV_TXT:p028:c03', 'ADV_TXT:p028:c05']
- **Citation Details:** [{"id": "ADV_TXT:p028:c02", "modality": "text", "label": "Summary for Policymakers (p.12)", "pdf_page": 28, "printed_page": "12", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p028:c03", "modality": "text", "label": "Summary for Policymakers (p.12)", "pdf_page": 28, "printed_page": "12", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p028:c05", "modality": "text", "label": "Summary for Policymakers (p.12)", "pdf_page": 28, "printed_page": "12", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_test_24 [text] — `status=answered` | `searches=3` | `inspects=0` | `err=None`
- **Question:** According to Section 2.1.1 (PDF p.58 / printed p.42), what were the observed 2011–2020 global surface temperature increases (best estimate and range) relative to 1850–1900 overall, over land, and over the ocean, and what were the assessed 1850–1900 to 2010–2019 temperature contributions from total human influence, well-mixed GHGs, other human drivers (principally aerosols), and natural (solar and volcanic) drivers?
- **Expected Answer:** In 2011–2020 relative to 1850–1900: overall global surface temperature rose ~1.1°C (1.09 [0.95 to 1.20]°C), with larger warming over land (1.59 [1.34 to 1.83]°C) than over the ocean (0.88 [0.68 to 1.01]°C). From 1850–1900 to 2010–2019: likely total human-caused increase = 0.8°C to 1.3°C (best estimate 1.07°C); well-mixed GHGs contributed +1.0°C to +2.0°C; other human drivers (principally aerosols) contributed cooling of 0.0°C to 0.8°C; natural (solar and volcanic) drivers changed temperature by ±0.1°C.
- **Gold Source:** pages `[58]`, regions `[]`, note: Verified verbatim in PDF p.58 (printed p.42), Section 2.1.1.
- **Agent Answer:** According to Section 2.1.1 (PDF p. 58 / printed p. 42) of the IPCC AR6 Synthesis Report:

### Observed 2011–2020 Global Surface Temperature Increases (relative to 1850–1900):
* **Overall:** 1.09 [0.95 to 1.20] °C (around 1.1 °C) [ADV_TXT:p058:c02]
* **Over land:** 1.59 [1.34 to 1.83] °C [ADV_TXT:p058:c02]
* **Over the ocean:** 0.88 [0.68 to 1.01] °C [ADV_TXT:p058:c02]

---

### Assessed 1850–1900 to 2010–2019 Temperature Contributions:
* **Total human influence (total human-caused warming):** Best estimate of 1.07 °C, with a likely range of 0.8 °C to 1.3 °C [ADV_TXT:p058:c03].
* **Well-mixed GHGs:** Likely contributed a warming of 1.0 °C to 2.0 °C [ADV_TXT:p058:c03].
* **Other human drivers (principally aerosols):** Likely contributed a cooling of 0.0 °C to 0.8 °C [ADV_TXT:p058:c03].
* **Natural (solar and volcanic) drivers:** Changed global surface temperature by ±0.1 °C [ADV_TXT:p058:c03].
- **Citations:** ['ADV_TXT:p058:c02', 'ADV_TXT:p058:c03']
- **Citation Details:** [{"id": "ADV_TXT:p058:c02", "modality": "text", "label": "Section 2: Current Status and Trends (p.42)", "pdf_page": 58, "printed_page": "42", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p058:c03", "modality": "text", "label": "Section 2: Current Status and Trends (p.42)", "pdf_page": 58, "printed_page": "42", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_test_25 [text] — `status=answered` | `searches=2` | `inspects=0` | `err=None`
- **Question:** According to Section 4.2 and Footnote 148 (PDF p.111 / printed p.95), what is the projected globally discounted value of stranded fossil fuel infrastructure from 2015 to 2050 when limiting global warming to 2°C or below, and what quantitative benchmarks does Footnote 148 use to illustrate interventions without which fossil fuels count as 'unabated'?
- **Expected Answer:** Limiting global warming to 2°C or below could strand considerable fossil fuel infrastructure with a globally discounted value projected around USD 1 to 4 trillion from 2015 to 2050 (medium confidence). Footnote 148 defines 'unabated fossil fuels' as fossil fuels produced and used without interventions that substantially reduce life-cycle GHG emissions, giving the benchmark examples of capturing 90% or more CO2 from power plants, or 50 to 80% of fugitive methane emissions from energy supply.
- **Gold Source:** pages `[111]`, regions `[]`, note: Verified verbatim in PDF p.111 (printed p.95), Section 4.2 & Footnote 148.
- **Agent Answer:** According to Section 4.2 and Footnote 148 (PDF p. 111 / printed p. 95) of the IPCC AR6 Synthesis Report:

- **Projected Globally Discounted Value of Stranded Infrastructure:** 
  Limiting global warming to 2°C or below is projected to result in a globally discounted value of stranded fossil fuel infrastructure of around **USD 1 to 4 trillion** from 2015 to 2050 (*medium confidence*) [ADV_TXT:p111:c07].

- **Quantitative Benchmarks for 'Unabated' Fossil Fuels in Footnote 148:**
  Footnote 148 defines "unabated fossil fuels" as those produced and used without interventions that substantially reduce life-cycle greenhouse gas emissions, illustrating these interventions with the following quantitative benchmarks [ADV_TXT:p111:c05], [ADV_TXT:p111:c06]:
  1. Capturing **90% or more** $\text{CO}_2$ from power plants [ADV_TXT:p111:c06].
  2. Capturing **50 to 80%** of fugitive methane emissions from energy supply [ADV_TXT:p111:c06].
- **Citations:** ['ADV_TXT:p111:c05', 'ADV_TXT:p111:c06', 'ADV_TXT:p111:c07']
- **Citation Details:** [{"id": "ADV_TXT:p111:c05", "modality": "text", "label": "Section 4: Near-Term Responses (p.95)", "pdf_page": 111, "printed_page": "95", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p111:c06", "modality": "text", "label": "Section 4: Near-Term Responses (p.95)", "pdf_page": 111, "printed_page": "95", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p111:c07", "modality": "text", "label": "Section 4: Near-Term Responses (p.95)", "pdf_page": 111, "printed_page": "95", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_test_26 [text] — `status=answered` | `searches=1` | `inspects=0` | `err=None`
- **Question:** According to Section 2.3.2 and Footnote 100 (PDF p.77 / printed p.61), how does the report distinguish 'hard adaptation limit' from 'soft adaptation limit', which ecosystems are reported as already having reached hard adaptation limits, and which human groups/regions are reported as having reached soft limits?
- **Expected Answer:** Footnote 100: 'Hard adaptation limit' means no adaptive actions are possible to avoid intolerable risks; 'Soft adaptation limit' means options are currently not available to avoid intolerable risks through adaptive action. Ecosystems already reaching hard limits (high confidence): some warm water coral reefs, some coastal wetlands, some rainforests, and some polar and mountain ecosystems. Groups reaching soft limits (medium confidence, due to financial/governance/institutional/policy constraints): individuals and households in low lying coastal areas in Australasia and Small Islands, and smallholder farmers in Central and South America, Africa, Europe and Asia.
- **Gold Source:** pages `[77]`, regions `[]`, note: Verified verbatim in PDF p.77 (printed p.61), Section 2.3.2 & Footnote 100.
- **Agent Answer:** According to Section 2.3.2 and Footnote 100 (printed p. 61 / PDF p. 77) of the IPCC AR6 Synthesis Report:

### 1. Distinction Between Hard and Soft Adaptation Limits
An **adaptation limit** is defined as the point at which an actor’s objectives (or system needs) cannot be secured from intolerable risks through adaptive actions [ADV_TXT:p077:c04]:
* **Hard adaptation limit:** No adaptive actions are possible to avoid intolerable risks [ADV_TXT:p077:c04].
* **Soft adaptation limit:** Options are currently not available to avoid intolerable risks through adaptive action [ADV_TXT:p077:c04].

---

### 2. Ecosystems Reported as Already Reaching Hard Adaptation Limits
Section 2.3.2 states (*high confidence*) that ecosystems already reaching hard adaptation limits include [ADV_TXT:p077:c07]:
* Some warm-water coral reefs
* Some coastal wetlands
* Some rainforests
* Some polar and mountain ecosystems

---

### 3. Human Groups and Regions Reported as Having Reached Soft Limits
Section 2.3.2 states (*medium confidence*) that soft limits have been reached by [ADV_TXT:p077:c07]:
* **Individuals and households** in low-lying coastal areas in **Australasia** and **Small Islands**
* **Smallholder farmers** in **Central and South America**, **Africa**, **Europe**, and **Asia**

*(Note: These soft limits result from financial, governance, institutional, and policy constraints, and can be overcome by addressing these constraints [ADV_TXT:p077:c07]).*
- **Citations:** ['ADV_TXT:p077:c04', 'ADV_TXT:p077:c07']
- **Citation Details:** [{"id": "ADV_TXT:p077:c04", "modality": "text", "label": "Section 2: Current Status and Trends (p.61)", "pdf_page": 77, "printed_page": "61", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p077:c07", "modality": "text", "label": "Section 2: Current Status and Trends (p.61)", "pdf_page": 77, "printed_page": "61", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_test_27 [unanswerable] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** What specific decisions or funding targets were adopted at COP28 or under UNFCCC Paris Agreement Article 6 international carbon-market rules according to the IPCC AR6 Synthesis Report?
- **Expected Behavior:** Abstain — Neither COP28 nor Paris Agreement Article 6 carbon-market rules appear anywhere in the 186-page IPCC AR6 Synthesis Report.
- **Agent Answer:** The IPCC AR6 Synthesis Report does not contain information on decisions or funding targets adopted at COP28, nor does it detail specific rules or funding targets adopted under Article 6 international carbon markets. The AR6 Synthesis Report was finalized and adopted in March 2023, prior to the COP28 conference (held in late 2023), and the assessed report text does not cover post-publication COP28 outcomes or specific Article 6 market mechanism decisions/funding targets.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []

## adv_test_28 [unanswerable] — `status=abstain` | `searches=5` | `inspects=1` | `err=None`
- **Question:** What are Vietnam's historical cumulative CO2 emissions (1850–2019) and national 2030 GHG emissions reduction target reported in Section 2 or Figure 2.2?
- **Expected Behavior:** Abstain — Vietnam is never mentioned in the report, and Figure 2.2 aggregates emissions only at macro-regional level (e.g., South-East Asia and Pacific) rather than country-by-country.
- **Agent Answer:** The IPCC AR6 Synthesis Report does not report Vietnam's individual historical cumulative CO2 emissions (1850–2019) or its national 2030 GHG emissions reduction target in Section 2 or Figure 2.2. 

Specifically:
- In Figure 2.2 (Panel a), historical cumulative net anthropogenic CO2 emissions (1850–2019) are presented only for aggregate geographic regions (such as North America, Europe, Eastern Asia, Latin America and Caribbean, Eastern Europe and West-Central Asia, South-East Asia and Pacific, Africa, Australia/Japan/New Zealand, Southern Asia, Middle East, and international shipping and aviation), with no country-level breakdown for Vietnam.
- In Section 2 (including Section 2.3.1 and Table 2.2), greenhouse gas emissions trajectories, implementation gaps, and 2030 Nationally Determined Contribution (NDC) targets are assessed at the global aggregate level, without reporting Vietnam's specific national 2030 emissions reduction target.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** ['VIS:Figure_2_2_charts:p061']

## adv_test_29 [unanswerable] — `status=abstain` | `searches=5` | `inspects=1` | `err=None`
- **Question:** According to Figure 2.4 or Section 2.2, what were the 2020 unit costs (USD per MWh or USD per kilogram) of nuclear fusion, small modular reactors (SMRs), or green hydrogen?
- **Expected Behavior:** Abstain — Nuclear fusion, small modular reactors (SMRs), and per-kg green hydrogen costs are not covered anywhere in Figure 2.4 or the report.
- **Agent Answer:** Neither Figure 2.4 nor Section 2.2 provides 2020 unit costs (in USD per MWh, USD per kg, or any other unit) for nuclear fusion, small modular reactors (SMRs), or green hydrogen. Figure 2.4 and the associated text only report unit costs for Photovoltaics (PV), Onshore wind, Offshore wind (in USD/MWh), and lithium-ion battery packs for passenger electric vehicles (in USD/kWh).
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** ['VIS:Figure_2_4:p070']

## adv_test_30 [unanswerable] — `status=abstain` | `searches=3` | `inspects=1` | `err=None`
- **Question:** In the synthetic burning-ember risk diagrams of Figure 3.3 panel (e) (p.92 / printed p.76), what numerical global warming levels (°C) mark the transitions from Moderate to High and High to Very high risk for 'Urban infrastructure damage in Asia'?
- **Expected Behavior:** Abstain — Figure 3.3e explicitly states that no synthetic burning-ember risk diagrams were developed for Asia (nor Small Islands or Central and South America); only bulleted text risks appear.
- **Agent Answer:** Figure 3.3 panel (e) (p. 92 / printed p. 76) does not provide synthetic burning-ember risk diagrams or numerical transition temperatures for Asia. 

As stated in the explanatory text of panel (e), "The development of synthetic diagrams for Small Islands, Asia and Central and South America was limited due to the paucity of adequately downscaled climate projections, with uncertainty in the direction of change, the diversity of climatologies and socioeconomic contexts across countries within a region, and the resulting few numbers of impact and risk projections for different warming levels." 

Although "Urban infrastructure damage and impacts on human well-being and health due to flooding, especially in coastal cities and settlements" is listed in the text table for Asia as an assessed key risk (with at least medium confidence), no burning ember diagram exists for it, and therefore no numerical global warming levels (°C) marking transitions from Moderate to High or High to Very high risk are quantified or presented in Figure 3.3 panel (e).
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** ['VIS:Figure_3_3_reg:p092']

## adv_test_31 [unanswerable] — `status=answered` | `searches=2` | `inspects=1` | `err=None`
- **Question:** In Figure 4.5 (p.125–126), what synergy/trade-off score is shown across columns for 'SDG 13 (Climate Action)', and what confidence levels (High/Medium/Low) are reported for the 'Ocean ecosystems - Adaptation' cells?
- **Expected Behavior:** Abstain — Figure 4.5 omits SDG 13 (Climate Action) intentionally, and its caption on p.126 explicitly states that confidence levels are not reported due to knowledge gaps.
- **Agent Answer:** Based on Figure 4.5 and its accompanying text (pp. 125–126 / Section 4, p. 110):

1. **SDG 13 (Climate Action)**: 
   There is no synergy/trade-off score or row shown for **SDG 13 (Climate Action)**; the rows in Figure 4.5 skip directly from SDG 12 to SDG 14 [VIS:Figure_4_5:p125]. As stated in the figure note, *"SDG 13 (Climate Action) is not listed because mitigation/ adaptation is being considered in terms of interaction with SDGs and not vice versa"* [ADV_TXT:p126:c01] [ADV_TXT:p126:c02].

2. **Confidence levels for 'Ocean ecosystems - Adaptation' cells**: 
   No confidence levels (High, Medium, or Low) are reported for the 'Ocean ecosystems - Adaptation' cells or any other cells in Figure 4.5 [VIS:Figure_4_5:p125]. The report explicitly notes: *"For the sake of uniformity, we are not reporting the confidence levels because there is knowledge gap in adaptation option wise relation with SDGs and their confidence level which is evident from WGII fig SPM.4b"* [ADV_TXT:p126:c02].
- **Citations:** ['VIS:Figure_4_5:p125', 'ADV_TXT:p126:c01', 'ADV_TXT:p126:c02']
- **Citation Details:** [{"id": "VIS:Figure_4_5:p125", "modality": "diagram_map", "label": "Figure 4.5", "pdf_page": 125, "printed_page": "109", "bbox": [45.0, 45.0, 570.0, 645.0], "crop_relpath": "data/advanced/crops/VIS_Figure_4_5_p125.png"}, {"id": "ADV_TXT:p126:c01", "modality": "text", "label": "Section 4: Near-Term Responses (p.110)", "pdf_page": 126, "printed_page": "110", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p126:c02", "modality": "text", "label": "Section 4: Near-Term Responses (p.110)", "pdf_page": 126, "printed_page": "110", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** ['VIS:Figure_4_5:p125']

## adv_test_32 [unanswerable] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** What annual electricity consumption and CO2 emissions from cryptocurrency mining (such as Bitcoin) or projected fiscal revenues from the EU Carbon Border Adjustment Mechanism (CBAM) are reported in the IPCC AR6 Synthesis Report?
- **Expected Behavior:** Abstain — Neither cryptocurrency/Bitcoin mining nor the EU Carbon Border Adjustment Mechanism (CBAM) is mentioned anywhere in the 186-page IPCC AR6 Synthesis Report.
- **Agent Answer:** The IPCC AR6 Synthesis Report does not report or assess annual electricity consumption or CO2 emissions from cryptocurrency mining (such as Bitcoin), nor does it report projected fiscal revenues from the EU Carbon Border Adjustment Mechanism (CBAM). Because these specific metrics and mechanisms are not presented or quantified in the report, there is insufficient evidence to provide the requested figures.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []
