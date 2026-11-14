# Advanced Audit Worksheet — `multimodal_vision_agent` (`dev`, N=20)

## adv_dev_01 [table] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** According to Box SPM.1, Table 1, which WGIII modelled pathway categories have a corresponding RCPy designation listed for WGI and WGII, and what are their respective category descriptions, GHG emissions scenarios (SSPx-y), and RCPy labels?
- **Expected Answer:** Three categories have RCPy designations: C3 ('limit warming to 2°C (>67%)', Low (SSP1-2.6), RCP2.6), C6 ('limit warming to 3°C (>50%)', Intermediate (SSP2-4.5), RCP 4.5), and C8 ('exceed warming of 4°C (>50%)', Very high (SSP5-8.5), RCP 8.5).
- **Gold Source:** pages `[26]`, regions `['VIS:Table_Box_SPM1:p026']`, note: Verified from VIS_Table_Box_SPM1_p026.png (PDF p.26, printed p.10): only rows C3, C6, and C8 have populated RCPy cells.
- **Agent Answer:** According to Box SPM.1, Table 1, the WGIII modelled pathway categories that have a corresponding RCPy designation listed for WGI and WGII are **C3**, **C6**, and **C8** [VIS:Table_Box_SPM1:p026]. 

Their respective details are as follows:

- **Category C3**:
  - **Category description**: limit warming to 2°C (>67%) [VIS:Table_Box_SPM1:p026]
  - **GHG emissions scenario (SSPx-y)**: Low (SSP1-2.6) [VIS:Table_Box_SPM1:p026]
  - **RCPy label**: RCP2.6 [VIS:Table_Box_SPM1:p026]

- **Category C6**:
  - **Category description**: limit warming to 3°C (>50%) [VIS:Table_Box_SPM1:p026]
  - **GHG emissions scenario (SSPx-y)**: Intermediate (SSP2-4.5) [VIS:Table_Box_SPM1:p026]
  - **RCPy label**: RCP 4.5 [VIS:Table_Box_SPM1:p026]

- **Category C8**:
  - **Category description**: exceed warming of 4°C (>50%) [VIS:Table_Box_SPM1:p026]
  - **GHG emissions scenario (SSPx-y)**: Very high (SSP5-8.5) [VIS:Table_Box_SPM1:p026]
  - **RCPy label**: RCP 8.5 [VIS:Table_Box_SPM1:p026]

(The remaining categories in the table—C1, C2, C4, C5, and C7—do not have an RCPy designation listed [VIS:Table_Box_SPM1:p026].)
- **Citations:** ['VIS:Table_Box_SPM1:p026']
- **Citation Details:** [{"id": "VIS:Table_Box_SPM1:p026", "modality": "table", "label": "Box SPM.1, Table 1", "pdf_page": 26, "printed_page": "10", "bbox": [65.0, 48.0, 550.0, 350.0], "crop_relpath": "data/advanced/crops/VIS_Table_Box_SPM1_p026.png"}]
- **Inspected Crops:** ['VIS:Table_Box_SPM1:p026']

## adv_dev_02 [table] — `status=answered` | `searches=2` | `inspects=1` | `err=None`
- **Question:** In Table 2.1, what are the assessed confidence/likelihood levels (from the colour key) and any cell text annotations for both 'Observed change assessment' and 'Human contribution assessment' on 'Greenland ice sheet mass loss since 1990s' and 'Antarctic ice sheet mass loss since 1990s'?
- **Expected Answer:** Greenland ice sheet mass loss since 1990s: Observed change = virtually certain (dark maroon), Human contribution = medium confidence (pale cream, no extra text). Antarctic ice sheet mass loss since 1990s: Observed change = very likely (orange), Human contribution = Limited evidence & medium agreement (unshaded cell with text).
- **Gold Source:** pages `[63]`, regions `['VIS:Table_2_1:p063']`, note: Verified from VIS_Table_2_1_p063.png (PDF p.63, printed p.47) under Cryosphere rows; cells encode likelihood purely via color key.
- **Agent Answer:** Based on Table 2.1 of the IPCC AR6 Synthesis Report [VIS:Table_2_1:p063], the assessments and annotations are:

### **Greenland ice sheet mass loss since 1990s**
* **Observed change assessment:**
  * **Confidence/Likelihood level:** **Virtually certain** (dark maroon/dark red cell fill corresponding to *virtually certain* in the colour key) [VIS:Table_2_1:p063].
  * **Cell text annotations:** None (no text annotation) [VIS:Table_2_1:p063].
* **Human contribution assessment:**
  * **Confidence/Likelihood level:** **Medium confidence** (pale cream/off-white cell fill corresponding to *medium confidence* in the colour key) [VIS:Table_2_1:p063].
  * **Cell text annotations:** None (no text annotation) [VIS:Table_2_1:p063].

---

### **Antarctic ice sheet mass loss since 1990s**
* **Observed change assessment:**
  * **Confidence/Likelihood level:** **Very likely** (orange cell fill corresponding to *very likely* in the colour key) [VIS:Table_2_1:p063].
  * **Cell text annotations:** None (no text annotation) [VIS:Table_2_1:p063].
* **Human contribution assessment:**
  * **Confidence/Likelihood level:** Not assigned a colour from the colour key (white/unshaded cell; as stated in the table caption, explanatory text is provided when colour coding is not available) [VIS:Table_2_1:p063].
  * **Cell text annotation:** ***Limited evidence & medium agreement*** [VIS:Table_2_1:p063].
- **Citations:** ['VIS:Table_2_1:p063']
- **Citation Details:** [{"id": "VIS:Table_2_1:p063", "modality": "table", "label": "Table 2.1", "pdf_page": 63, "printed_page": "47", "bbox": [40.0, 42.0, 570.0, 610.0], "crop_relpath": "data/advanced/crops/VIS_Table_2_1_p063.png"}]
- **Inspected Crops:** ['VIS:Table_2_1:p063']

## adv_dev_03 [table] — `status=answered` | `searches=1` | `inspects=2` | `err=None`
- **Question:** In Figure SPM.7 panel (a) under 'SETTLEMENTS AND INFRASTRUCTURE' in the left-hand 'Climate responses and adaptation options' table, what are the assessed potential feasibility levels (up to 1.5°C), synergies with mitigation, and confidence dot levels for all three listed options?
- **Expected Answer:** 1) Sustainable urban water management: Potential feasibility = Medium (2 dots / Medium confidence), Synergies = Low (1 dot / Low confidence). 2) Sustainable land use and urban planning: Potential feasibility = Medium (2 dots / Medium confidence), Synergies = High (1 dot / Low confidence). 3) Green infrastructure and ecosystem services: Potential feasibility = Medium (3 dots / High confidence), Synergies = High (2 dots / Medium confidence).
- **Gold Source:** pages `[43]`, regions `['VIS:Table_SPM7_Feasibility:p043']`, note: Verified from VIS_Table_SPM7_Feasibility_p043.png (PDF p.43, printed p.27) matrix legend and SETTLEMENTS AND INFRASTRUCTURE block.
- **Agent Answer:** Based on Figure SPM.7 panel (a) (and the identical Figure 4.4 panel a), the legend defines the assessed levels and confidence dots as follows [VIS:Table_SPM7_Feasibility:p043], [VIS:Figure_4_4:p119]:
- **Feasibility level and synergies with mitigation:**
  - **High** (dark blue)
  - **Medium** (medium purple)
  - **Low** (light purple)
- **Confidence level in potential feasibility and in synergies with mitigation:**
  - **High** (••• / three dots)
  - **Medium** (•• / two dots)
  - **Low** (• / one dot)

Under **SETTLEMENTS AND INFRASTRUCTURE**, the assessments for the three listed options are [VIS:Table_SPM7_Feasibility:p043], [VIS:Figure_4_4:p119]:

1. **Sustainable urban water management**:
   - **Potential feasibility (up to 1.5°C):** **Medium** with **Medium confidence** (•• / two dots)
   - **Synergies with mitigation:** **Low** with **Low confidence** (• / one dot)

2. **Sustainable land use and urban planning**:
   - **Potential feasibility (up to 1.5°C):** **Medium** with **Medium confidence** (•• / two dots)
   - **Synergies with mitigation:** **High** with **Low confidence** (• / one dot)

3. **Green infrastructure and ecosystem services**:
   - **Potential feasibility (up to 1.5°C):** **High** with **High confidence** (••• / three dots)
   - **Synergies with mitigation:** **High** with **Medium confidence** (•• / two dots)
- **Citations:** ['VIS:Table_SPM7_Feasibility:p043', 'VIS:Figure_4_4:p119']
- **Citation Details:** [{"id": "VIS:Table_SPM7_Feasibility:p043", "modality": "table", "label": "Figure SPM.7 Adaptation Feasibility Table", "pdf_page": 43, "printed_page": "27", "bbox": [50.0, 56.0, 412.0, 628.0], "crop_relpath": "data/advanced/crops/VIS_Table_SPM7_Feasibility_p043.png"}, {"id": "VIS:Figure_4_4:p119", "modality": "chart", "label": "Figure 4.4", "pdf_page": 119, "printed_page": "103", "bbox": [45.0, 45.0, 570.0, 750.0], "crop_relpath": "data/advanced/crops/VIS_Figure_4_4_p119.png"}]
- **Inspected Crops:** ['VIS:Figure_4_4:p119', 'VIS:Table_SPM7_Feasibility:p043']

## adv_dev_04 [diagram_map] — `status=answered` | `searches=5` | `inspects=4` | `err=None`
- **Question:** In Figure SPM.1 panel (a) under 'Water availability and food production', which specific indicators show both 'Adverse and positive impacts' (striped red-and-green circles) at the global level, which show solely 'Adverse impacts' (solid red circles), and what is the attribution confidence level for all four indicators?
- **Expected Answer:** Physical water availability and Animal and livestock health and productivity show both 'Adverse and positive impacts' (striped red-and-green circles), whereas Agriculture/crop production and Fisheries yields and aquaculture production show solely 'Adverse impacts' (solid red circles). Attribution confidence is Medium confidence (2 dots) for Physical water availability, Agriculture/crop production, and Fisheries yields and aquaculture production, and Low confidence (1 dot) for Animal and livestock health and productivity.
- **Gold Source:** pages `[23]`, regions `['VIS:Figure_SPM1:p023']`, note: Verified at 400 DPI from PDF p.23 (printed p.7) Figure SPM.1 panel (a) top-left block under Water availability and food production + Key.
- **Agent Answer:** In Figure SPM.1 panel (a), under the category **'Water availability and food production'**, the four assessed indicators, their impact classifications at the global level, and their attribution confidence levels are as follows [VIS:Figure_SPM1:p023]:

### 1. Indicators showing both 'Adverse and positive impacts' (striped red-and-green circles):
* **Physical water availability** [VIS:Figure_SPM1:p023]
* **Animal and livestock health and productivity** [VIS:Figure_SPM1:p023]

### 2. Indicators showing solely 'Adverse impacts' (solid red circles):
* **Agriculture/crop production** [VIS:Figure_SPM1:p023]
* **Fisheries yields and aquaculture production** [VIS:Figure_SPM1:p023]

---

### Attribution Confidence Levels for all four indicators:
According to the figure legend, confidence in attribution to climate change is indicated by dot counts [VIS:Figure_SPM1:p023]:
* **Physical water availability:** **Medium confidence** (represented by two dots: ••) [VIS:Figure_SPM1:p023]
* **Agriculture/crop production:** **Medium confidence** (represented by two dots: ••) [VIS:Figure_SPM1:p023]
* **Animal and livestock health and productivity:** **Low confidence** (represented by one dot: •) [VIS:Figure_SPM1:p023]
* **Fisheries yields and aquaculture production:** **Medium confidence** (represented by two dots: ••) [VIS:Figure_SPM1:p023]
- **Citations:** ['VIS:Figure_SPM1:p023']
- **Citation Details:** [{"id": "VIS:Figure_SPM1:p023", "modality": "diagram_map", "label": "Figure SPM.1", "pdf_page": 23, "printed_page": "7", "bbox": [45.0, 48.0, 565.0, 745.0], "crop_relpath": "data/advanced/crops/VIS_Figure_SPM1_p023.png"}]
- **Inspected Crops:** ['VIS:Figure_SPM1:p023']

## adv_dev_05 [diagram_map] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Cross-Section Box.2 Figure 1 panel (a) (p.81 / printed p.65), list the three horizontal chain blocks downstream of 'Socio-economic changes', identify the two policy boxes linked underneath them, and list all five SSP scenarios plotted in the central 21st-century temperature graph.
- **Expected Answer:** Downstream from 'Socio-economic changes', the horizontal chain runs: 'Emissions' -> 'Climate' -> 'Impacts / Risks' (with feedback/influence arrows looping back to Socio-economic changes). The two policy boxes underneath are 'Mitigation Policy' (under Emissions) and 'Adaptation Policy' (under Impacts / Risks). The five SSP scenarios plotted are SSP1-1.9, SSP1-2.6, SSP2-4.5, SSP3-7.0, and SSP5-8.5.
- **Gold Source:** pages `[81, 82]`, regions `['VIS:CrossBox2_Diagram:p081']`, note: Verified from VIS_CrossBox2_Diagram_p081.png (PDF p.81) and caption on PDF p.82.
- **Agent Answer:** Based on Cross-Section Box.2 Figure 1 panel (a) (printed p. 65 / pdf p. 81) [VIS:CrossBox2_Diagram:p081]:

1. **Three horizontal chain blocks downstream of 'Socio-economic changes':**
   - **Emissions** (connected via *"influence"*)
   - **Climate** (connected via *"that change"*)
   - **Impacts / Risks** (connected via *"which drives"*)

2. **Two policy boxes linked underneath them:**
   - **Mitigation Policy** (linked underneath *Emissions*)
   - **Adaptation Policy** (linked underneath *Impacts / Risks*)

3. **Five SSP scenarios plotted in the central 21st-century temperature graph:**
   - **SSP1-1.9**
   - **SSP1-2.6**
   - **SSP2-4.5**
   - **SSP3-7.0**
   - **SSP5-8.5** [VIS:CrossBox2_Diagram:p081]
- **Citations:** ['VIS:CrossBox2_Diagram:p081']
- **Citation Details:** [{"id": "VIS:CrossBox2_Diagram:p081", "modality": "diagram_map", "label": "Cross-Section Box.2 Figure 1", "pdf_page": 81, "printed_page": "65", "bbox": [45.0, 42.0, 575.0, 425.0], "crop_relpath": "data/advanced/crops/VIS_CrossBox2_Diagram_p081.png"}]
- **Inspected Crops:** ['VIS:CrossBox2_Diagram:p081']

## adv_dev_06 [diagram_map] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure 3.1 (p.86 / printed p.70), when was global surface temperature last sustained at or above 2.5°C according to the annotation on the Global warming level (GWL) scale, and how does panel (b) define the '1 standard deviation' unit for annual mean total column soil moisture change?
- **Expected Answer:** The annotation states the last time global surface temperature was sustained at or above 2.5°C was over 3 million years ago. In panel (b), soil moisture change is expressed in standard deviation (σ) of interannual variability during 1850–1900, where a projected reduction of 1 standard deviation corresponds to soil moisture conditions typical of droughts occurring about once every six years during 1850–1900 (also noting differences from precipitation due to evapotranspiration).
- **Gold Source:** pages `[86]`, regions `['VIS:Figure_3_1:p086']`, note: Verified from VIS_Figure_3_1_p086.png (PDF p.86, printed p.70) top GWL annotation and caption text.
- **Agent Answer:** Based on Figure 3.1 (printed p. 70 / pdf p. 86) of the IPCC AR6 Synthesis Report:

1. **Last time global surface temperature was sustained at or above 2.5°C:**
According to the annotation above the Global Warming Level (GWL) scale, the last time global surface temperature was sustained at or above 2.5°C was **over 3 million years ago** [VIS:Figure_3_1:p086].

2. **Definition of the standard deviation unit in panel (b):**
The caption specifies that the unit ($\sigma$) is **the standard deviation of interannual variability in soil moisture during 1850–1900** [VIS:Figure_3_1:p086]. The caption further notes that standard deviation is a widely used metric for drought severity, and a projected reduction in mean soil moisture by one standard deviation corresponds to soil moisture conditions typical of droughts that occurred about once every six years during 1850–1900 [VIS:Figure_3_1:p086].
- **Citations:** ['VIS:Figure_3_1:p086']
- **Citation Details:** [{"id": "VIS:Figure_3_1:p086", "modality": "diagram_map", "label": "Figure 3.1", "pdf_page": 86, "printed_page": "70", "bbox": [35.0, 45.0, 565.0, 745.0], "crop_relpath": "data/advanced/crops/VIS_Figure_3_1_p086.png"}]
- **Inspected Crops:** ['VIS:Figure_3_1:p086']

## adv_dev_07 [chart] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** According to Figure 2.1 panels (b) and (c) (p.59 / printed p.43), what were the annotated 2019 atmospheric concentrations (value and unit) of CO2, CH4, and N2O, and by how much had global surface temperature increased by 2011–2020 compared to 1850–1900?
- **Expected Answer:** 2019 atmospheric concentrations (panel b): Carbon dioxide (CO2) = 410 ppm, Methane (CH4) = 1866 ppb, Nitrous oxide (N2O) = 332 ppb. Global surface temperature (panel c) increased by 1.1°C by 2011–2020 compared to 1850–1900.
- **Gold Source:** pages `[59]`, regions `['VIS:Figure_2_1:p059']`, note: Verified from VIS_Figure_2_1_p059.png (PDF p.59, printed p.43), annotated labels on panels (b) and (c).
- **Agent Answer:** According to Figure 2.1 panels (b) and (c) (printed p. 43 / pdf p. 59) [VIS:Figure_2_1:p059]:

- **Atmospheric concentrations in 2019** (Panel b):
  - **CO₂ (Carbon dioxide):** 410 ppm (parts per million) [VIS:Figure_2_1:p059]
  - **CH₄ (Methane):** 1866 ppb (parts per billion) [VIS:Figure_2_1:p059]
  - **N₂O (Nitrous oxide):** 332 ppb (parts per billion) [VIS:Figure_2_1:p059]

- **Global surface temperature increase** (Panel c):
  - Global surface temperature had increased by **1.1°C** by 2011–2020 compared to 1850–1900 [VIS:Figure_2_1:p059].
- **Citations:** ['VIS:Figure_2_1:p059']
- **Citation Details:** [{"id": "VIS:Figure_2_1:p059", "modality": "chart", "label": "Figure 2.1", "pdf_page": 59, "printed_page": "43", "bbox": [45.0, 45.0, 570.0, 735.0], "crop_relpath": "data/advanced/crops/VIS_Figure_2_1_p059.png"}]
- **Inspected Crops:** ['VIS:Figure_2_1:p059']

## adv_dev_08 [chart] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure 2.2 panel (c) ('Global net anthropogenic GHG emissions by region 1990–2019', p.61 / printed p.45), what were the total global net anthropogenic GHG emissions (GtCO2-eq) and Eastern Asia's percentage share in 1990, 2000, 2010, and 2019?
- **Expected Answer:** Total global net GHG emissions: 38 GtCO2-eq in 1990, 42 GtCO2-eq in 2000, 53 GtCO2-eq in 2010, and 59 GtCO2-eq in 2019. Eastern Asia's percentage share rose from 13% (1990) to 16% (2000), 24% (2010), and 27% (2019).
- **Gold Source:** pages `[61]`, regions `['VIS:Figure_2_2_charts:p061']`, note: Verified from VIS_Figure_2_2_charts_p061.png (PDF p.61, printed p.45), panel (c) vertical year callouts.
- **Agent Answer:** Based on Figure 2.2 panel (c) (*Global net anthropogenic GHG emissions by region 1990–2019*, page 61 / printed page 45) [VIS:Figure_2_2_charts:p061], the total global net anthropogenic GHG emissions and Eastern Asia's percentage share for each requested year are:

- **1990:**
  - **Total global emissions:** 38 GtCO₂-eq [VIS:Figure_2_2_charts:p061]
  - **Eastern Asia's share:** 13% [VIS:Figure_2_2_charts:p061]

- **2000:**
  - **Total global emissions:** 42 GtCO₂-eq [VIS:Figure_2_2_charts:p061]
  - **Eastern Asia's share:** 16% [VIS:Figure_2_2_charts:p061]

- **2010:**
  - **Total global emissions:** 53 GtCO₂-eq [VIS:Figure_2_2_charts:p061]
  - **Eastern Asia's share:** 24% [VIS:Figure_2_2_charts:p061]

- **2019:**
  - **Total global emissions:** 59 GtCO₂-eq [VIS:Figure_2_2_charts:p061]
  - **Eastern Asia's share:** 27% [VIS:Figure_2_2_charts:p061]
- **Citations:** ['VIS:Figure_2_2_charts:p061']
- **Citation Details:** [{"id": "VIS:Figure_2_2_charts:p061", "modality": "chart", "label": "Figure 2.2 Panels (a)-(c)", "pdf_page": 61, "printed_page": "45", "bbox": [42.0, 45.0, 575.0, 582.0], "crop_relpath": "data/advanced/crops/VIS_Figure_2_2_charts_p061.png"}]
- **Inspected Crops:** ['VIS:Figure_2_2_charts:p061']

## adv_dev_09 [chart] — `status=answered` | `searches=1` | `inspects=1` | `err=None`
- **Question:** In Figure 2.4 (p.70 / printed p.54), what cost range defines the yellow 'Fossil fuel cost (2020)' reference band in USD per MWh, how does the panel (a) y-axis unit for Passenger EV Li-ion battery packs differ from the renewables panels, and what are the different y-axis units and scales in panel (b) ('Market Adoption')?
- **Expected Answer:** The yellow 'Fossil fuel cost (2020)' band corresponds to USD 55 to 148 per MWh (for new coal and gas power). In panel (a), Photovoltaics (PV), Onshore wind, and Offshore wind plot LCOE in $2020/MWh (0–600), whereas Li-ion battery packs plot Cost in $2020/kWh (0–1600). In panel (b), PV and Onshore wind plot cumulative capacity in GW (0–800 scale), Offshore wind uses GW on a smaller 0–40 scale, and Passenger EVs plot Adoption in millions of EVs (0–8).
- **Gold Source:** pages `[70]`, regions `['VIS:Figure_2_4:p070']`, note: Verified from VIS_Figure_2_4_p070.png (PDF p.70, printed p.54) panel axes, yellow legend, and caption.
- **Agent Answer:** Based on **Figure 2.4** (p. 70 / printed p. 54) of the IPCC AR6 Synthesis Report [VIS:Figure_2_4:p070]:

### 1. 'Fossil fuel cost (2020)' Reference Band
* The yellow reference band represents the range of unit costs for new fossil fuel (coal and gas) power in 2020, which is defined as **USD 55 to 148 per MWh** (annotated with *"below this point, costs can be less than fossil fuels"*) [VIS:Figure_2_4:p070].

---

### 2. Panel (a) Y-Axis Unit: Passenger EV Li-ion Batteries vs Renewables
* **Renewables (Photovoltaics, Onshore wind, Offshore wind):** The y-axis unit is **Cost ($2020/MWh)** (measuring the levelised cost of energy, LCOE, per MWh of electricity produced), spanning from **0 to 600 $2020/MWh** (tick marks at 0, 150, 300, 450, 600) [VIS:Figure_2_4:p070].
* **Passenger EV Li-ion battery packs:** The y-axis unit is **Cost ($2020/kWh)** (measuring the cost per 1 kWh of battery storage capacity rather than per MWh of electricity generated), spanning from **0 to 1600 $2020/kWh** (tick marks at 0, 400, 800, 1200, 1600) [VIS:Figure_2_4:p070].

---

### 3. Panel (b) ('Market Adoption') Y-Axis Units and Scales
Panel (b) displays cumulative global adoption using two different metrics and three different scales across the four technologies [VIS:Figure_2_4:p070]:
* **Photovoltaics (PV):** 
  * Unit: **Adoption (GW)** (gigawatts of installed capacity)
  * Scale: **0 to 800 GW** (ticks at 0, 200, 400, 600, 800) [VIS:Figure_2_4:p070].
* **Onshore wind:** 
  * Unit: **Adoption (GW)** (gigawatts of installed capacity)
  * Scale: Shares the **0 to 800 GW** grid/scale [VIS:Figure_2_4:p070].
* **Offshore wind:** 
  * Unit: **Adoption (GW)** (gigawatts of installed capacity)
  * Scale: **0 to 40 GW** (ticks at 0, 10, 20, 30, 40) [VIS:Figure_2_4:p070].
* **Passenger electric vehicle:** 
  * Unit: **Adoption (millions of EVs)** (cumulative millions of battery-electric vehicles)
  * Scale: **0 to 8 million EVs** (ticks at 0, 2, 4, 6, 8) [VIS:Figure_2_4:p070].
- **Citations:** ['VIS:Figure_2_4:p070']
- **Citation Details:** [{"id": "VIS:Figure_2_4:p070", "modality": "chart", "label": "Figure 2.4", "pdf_page": 70, "printed_page": "54", "bbox": [35.0, 50.0, 565.0, 645.0], "crop_relpath": "data/advanced/crops/VIS_Figure_2_4_p070.png"}]
- **Inspected Crops:** ['VIS:Figure_2_4:p070']

## adv_dev_10 [chart] — `status=answered` | `searches=2` | `inspects=1` | `err=None`
- **Question:** In Figure 3.6 panel (c) ('Timing for net zero', p.102 / printed p.86), compare when global modelled pathways reach net zero CO2 versus net zero GHG under Category C1 (1.5°C >50%, no or limited overshoot) vs Category C3 (2°C >67%).
- **Expected Answer:** In both pathways CO2 reaches net zero earlier than total GHGs. Under 1.5°C (C1), net zero CO2 median is around early 2050s (~2050–2055), while net zero GHG median is much later (~late 2090s, around 2095–2100) and annotated 'not all scenarios reach net zero GHG by 2100'. Under 2°C (C3), net zero CO2 median shifts to around 2070 (~2070–2075), while the median for net zero GHG does not occur before 2100 (shaded bar appears only from late 2080s–2100).
- **Gold Source:** pages `[102]`, regions `['VIS:Figure_3_6:p102']`, note: Verified from VIS_Figure_3_6_p102.png (PDF p.102, printed p.86) panel (c) vertical median markers and callout.
- **Agent Answer:** Based on **Figure 3.6 panel (c)** (*'Timing for net zero'*, p. 102 / printed p. 86) and its accompanying text [ADV_TXT:p102:c01] [ADV_TXT:p102:c02] [ADV_TXT:p101:c03] [VIS:Figure_3_6:p102]:

### 1. Category C1 (Limit warming to 1.5°C (>50%) with no or limited overshoot)
* **Net Zero $\text{CO}_2$**:
  * **Median timing**: Reached around **2050** (early 2050s; vertical dark purple line) [ADV_TXT:p102:c01] [ADV_TXT:p101:c03] [VIS:Figure_3_6:p102].
  * **Likely range** (thick bar): Spans from roughly the mid-to-late **2040s to late 2050s** (~2045–2060) [VIS:Figure_3_6:p102].
  * **Very likely range** (thin line): Extends from around the late **2030s to 2070** (~2035–2070) [VIS:Figure_3_6:p102].
* **Net Zero GHG**:
  * **Median timing**: Reached substantially later than $\text{CO}_2$, near the end of the century around **2095–2100** (vertical blue line) [VIS:Figure_3_6:p102].
  * **Likely range** (thick bar): Begins in the **2070s** (~2075) and extends to 2100 [VIS:Figure_3_6:p102].
  * **Very likely range** (thin line): Begins around the mid-**2050s** (~2055) and extends to 2100 [VIS:Figure_3_6:p102].
  * **Note**: An annotation explicitly points out: *"not all scenarios reach net zero GHG by 2100"* [ADV_TXT:p102:c01] [VIS:Figure_3_6:p102].

---

### 2. Category C3 (Limit warming to 2°C (>67%))
* **Net Zero $\text{CO}_2$**:
  * **Median timing**: Reached around the **early 2070s** (~2070–2075; vertical dark purple line) [ADV_TXT:p101:c03] [VIS:Figure_3_6:p102].
  * **Likely range** (thick bar): Spans from roughly the mid-**2060s to late 2070s** (~2065–2080) [VIS:Figure_3_6:p102].
  * **Very likely range** (thin line): Extends from roughly **2055 to ~2090** [VIS:Figure_3_6:p102].
* **Net Zero GHG**:
  * **Median timing**: **No median line is shown before 2100** because the median pathway in Category C3 does not reach net zero GHG emissions by 2100 [VIS:Figure_3_6:p102].
  * **Likely and very likely ranges**: The very likely thin line starts around **2085**, and the likely thick bar begins in the **2090s** (~2095) and extends past 2100 off the edge of the panel [VIS:Figure_3_6:p102].

---

### Summary of Key Differences
* **$\text{CO}_2$ vs. GHG**: In both categories, global modelled pathways reach net zero $\text{CO}_2$ emissions decades earlier than net zero GHGs (*"GHGs reach net zero later than $\text{CO}_2$"*) [ADV_TXT:p102:c01] [ADV_TXT:p101:c03] [VIS:Figure_3_6:p102].
* **C1 vs. C3**: Pathways limiting warming to 1.5°C (C1) reach net zero $\text{CO}_2$ approximately 20 years earlier (around 2050) than pathways limiting warming to 2°C (C3, around the early 2070s) [ADV_TXT:p101:c03] [VIS:Figure_3_6:p102]. For total GHGs, while Category C1 reaches net zero GHGs by 2095–2100 in the median pathway, Category C3 does not achieve net zero GHGs by 2100 at the median level [VIS:Figure_3_6:p102].
- **Citations:** ['ADV_TXT:p101:c03', 'ADV_TXT:p102:c01', 'ADV_TXT:p102:c02', 'VIS:Figure_3_6:p102']
- **Citation Details:** [{"id": "ADV_TXT:p101:c03", "modality": "text", "label": "Section 3: Long-Term Futures (p.85)", "pdf_page": 101, "printed_page": "85", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p102:c01", "modality": "text", "label": "Section 3: Long-Term Futures (p.86)", "pdf_page": 102, "printed_page": "86", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p102:c02", "modality": "text", "label": "Section 3: Long-Term Futures (p.86)", "pdf_page": 102, "printed_page": "86", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "VIS:Figure_3_6:p102", "modality": "chart", "label": "Figure 3.6", "pdf_page": 102, "printed_page": "86", "bbox": [35.0, 45.0, 565.0, 510.0], "crop_relpath": "data/advanced/crops/VIS_Figure_3_6_p102.png"}]
- **Inspected Crops:** ['VIS:Figure_3_6:p102']

## adv_dev_11 [multi_hop] — `status=answered` | `searches=2` | `inspects=2` | `err=None`
- **Question:** Using Figure 2.2 panel (a) and panel (d) on p.61 (printed p.45), compare 'North America' and 'Southern Asia': state each region's share (%) of historical cumulative net CO2 emissions (1850–2019), 2019 population (million persons), 2019 GDP per capita (USD1000_PPP 2017), and 2019 net GHG per capita (tCO2-eq/person).
- **Expected Answer:** Historical cumulative CO2 emissions (1850–2019, panel a): North America = 23% vs Southern Asia = 4%. Regional indicators (2019, panel d): North America has 366 million population, 61 USD1000_PPP 2017 GDP per capita, and 19 tCO2-eq/person net GHG; Southern Asia has 1836 million population, 6.2 USD1000_PPP 2017 GDP per capita, and 2.6 tCO2-eq/person net GHG.
- **Gold Source:** pages `[61]`, regions `['VIS:Figure_2_2_charts:p061', 'VIS:Table_Fig2_2d:p061']`, note: Verified by joining bar percentages in VIS_Figure_2_2_charts_p061.png (panel a) and table columns in VIS_Table_Fig2_2d_p061.png (panel d).
- **Agent Answer:** Based on **Figure 2.2** (printed p. 45 / pdf p. 61), the comparison between **North America** and **Southern Asia** across the requested indicators is as follows:

* **Share of historical cumulative net anthropogenic $\text{CO}_2$ emissions (1850–2019)** (Panel a) [VIS:Figure_2_2_charts:p061]:
  * **North America:** 23%
  * **Southern Asia:** 4%

* **2019 Population** (Panel d) [VIS:Table_Fig2_2d:p061]:
  * **North America:** 366 million persons
  * **Southern Asia:** 1836 million persons

* **2019 GDP per capita** ($\text{USD1000}_{\text{PPP}}\text{ 2017}$ per person) (Panel d) [VIS:Table_Fig2_2d:p061]:
  * **North America:** 61
  * **Southern Asia:** 6.2

* **2019 Net GHG per capita (production basis)** ($\text{tCO}_2\text{-eq}$ per person) (Panel d) [VIS:Table_Fig2_2d:p061]:
  * **North America:** 19
  * **Southern Asia:** 2.6
- **Citations:** ['VIS:Figure_2_2_charts:p061', 'VIS:Table_Fig2_2d:p061']
- **Citation Details:** [{"id": "VIS:Figure_2_2_charts:p061", "modality": "chart", "label": "Figure 2.2 Panels (a)-(c)", "pdf_page": 61, "printed_page": "45", "bbox": [42.0, 45.0, 575.0, 582.0], "crop_relpath": "data/advanced/crops/VIS_Figure_2_2_charts_p061.png"}, {"id": "VIS:Table_Fig2_2d:p061", "modality": "table", "label": "Figure 2.2 Panel (d) Table", "pdf_page": 61, "printed_page": "45", "bbox": [42.0, 565.0, 575.0, 750.0], "crop_relpath": "data/advanced/crops/VIS_Table_Fig2_2d_p061.png"}]
- **Inspected Crops:** ['VIS:Figure_2_2_charts:p061', 'VIS:Table_Fig2_2d:p061']

## adv_dev_12 [multi_hop] — `status=answered` | `searches=1` | `inspects=2` | `err=None`
- **Question:** Combining Table 2.2 (p.74) and Figure 2.5 (p.75), state for 2030: (1) median projected emissions and [min–max] (GtCO2-eq/yr) for 'policies implemented by end of 2020' vs COP26 NDCs (unconditional and conditional), (2) percentage change from 2019 shown in Figure 2.5 panel (b) for implemented policies, NDCs, 2°C (>67%), and 1.5°C (>50%), and (3) the 2030 emissions gap between NDCs and 1.5°C pathways.
- **Expected Answer:** 1) Table 2.2 2030 projected emissions (GtCO2-eq/yr): Implemented policies = 57 [52–60]; NDCs unconditional = 53 [50–57]; NDCs including conditional = 50 [47–55]. 2) Figure 2.5(b) 2030 change relative to 2019: Implemented policies = +5%, NDCs = -4%, Limit warming to 2°C (>67%) = -26%, Limit warming to 1.5°C (>50%) = -43%. 3) 2030 emissions gap between NDCs and 1.5°C (>50% no/limited overshoot): 19–26 GtCO2-eq/yr (unconditional) and 16–23 GtCO2-eq/yr (conditional).
- **Gold Source:** pages `[74, 75]`, regions `['VIS:Table_2_2:p074', 'VIS:Figure_2_5:p075']`, note: Verified from VIS_Table_2_2_p074.png (p.74) and VIS_Figure_2_5_p075.png (p.75).
- **Agent Answer:** Based on Table 2.2 and Figure 2.5 of the IPCC AR6 Synthesis Report:

### 1. Median Projected Emissions and [min–max] for 2030 (GtCO₂-eq/yr)
From **Table 2.2** [VIS:Table_2_2:p074]:
* **Policies implemented by the end of 2020:** **57 [52–60] GtCO₂-eq/yr**
* **NDCs announced prior to COP26 (unconditional elements):** **53 [50–57] GtCO₂-eq/yr**
* **NDCs announced prior to COP26 (including conditional elements):** **50 [47–55] GtCO₂-eq/yr**

---

### 2. Percentage Change from 2019 Shown in Figure 2.5 Panel (b)
From **Figure 2.5 panel (b)** [VIS:Figure_2_5:p075]:
* **Implemented policies:** **+5%**
* **NDCs:** **–4%**
* **Limit warming to 2°C (>67%):** **–26%**
* **Limit warming to 1.5°C (>50% with no or limited overshoot):** **–43%**

---

### 3. 2030 Emissions Gap Between NDCs and 1.5°C Pathways
From **Table 2.2** [VIS:Table_2_2:p074], the emissions gap between NDCs and pathways limiting warming to 1.5°C (>50%) with no or limited overshoot with immediate action is:
* **Unconditional NDC elements:** **19–26 GtCO₂-eq/yr**
* **Including conditional NDC elements:** **16–23 GtCO₂-eq/yr**
- **Citations:** ['VIS:Table_2_2:p074', 'VIS:Figure_2_5:p075']
- **Citation Details:** [{"id": "VIS:Table_2_2:p074", "modality": "table", "label": "Table 2.2", "pdf_page": 74, "printed_page": "58", "bbox": [35.0, 240.0, 560.0, 610.0], "crop_relpath": "data/advanced/crops/VIS_Table_2_2_p074.png"}, {"id": "VIS:Figure_2_5:p075", "modality": "chart", "label": "Figure 2.5", "pdf_page": 75, "printed_page": "59", "bbox": [45.0, 45.0, 575.0, 480.0], "crop_relpath": "data/advanced/crops/VIS_Figure_2_5_p075.png"}]
- **Inspected Crops:** ['VIS:Figure_2_5:p075', 'VIS:Table_2_2:p074']

## adv_dev_13 [multi_hop] — `status=answered` | `searches=2` | `inspects=1` | `err=None`
- **Question:** Combine Section 3.3.1 (p.98) and Figure 3.5 panel (a) (p.99): state the global warming increment per 1000 GtCO2 emitted, the remaining carbon budget from the beginning of 2020 for limiting warming to 1.5°C (50% likelihood), and explain how Figure 3.5 panel (a) compares that 1.5°C budget against lifetime CO2 emissions from existing and planned fossil fuel infrastructure without additional abatement.
- **Expected Answer:** Section 3.3.1 (p.98): for every 1000 GtCO2 emitted by human activity, global mean temperature rises by likely 0.27°C to 0.63°C (best estimate 0.45°C). The remaining carbon budget from 2020 for 1.5°C (50% likelihood) is estimated at 500 GtCO2 (varying 300–600 GtCO2 depending on non-CO2 warming). Figure 3.5 panel (a) shows that cumulative lifetime CO2 emissions from existing fossil fuel infrastructure alone (without additional abatement) already exceed the 500 GtCO2 dashed line for 1.5°C (>50%), and existing plus planned infrastructure approaches the 2°C (83%, 900 GtCO2) line.
- **Gold Source:** pages `[98, 99]`, regions `['VIS:Figure_3_5:p099']`, note: Verified from PDF p.98 text (Section 3.3.1) and VIS_Figure_3_5_p099.png panel (a).
- **Agent Answer:** Based on Section 3.3.1 (p. 82 / pdf p. 98) and Figure 3.5 panel (a) (p. 83 / pdf p. 99):

1. **Global warming increment per 1000 GtCO2 emitted:**
   - For every 1000 GtCO2 emitted by human activity, global mean surface temperature increases by a best estimate of **0.45°C**, with a likely range of **0.27°C to 0.63°C** [ADV_TXT:p098:c01].

2. **Remaining carbon budget for 1.5°C (50% likelihood):**
   - From the beginning of 2020, the best estimate of the remaining carbon budget to limit warming to 1.5°C with a 50% likelihood is **500 GtCO2** (varying between 300 and 600 GtCO2 depending on non-CO2 warming) [ADV_TXT:p098:c02].

3. **Comparison in Figure 3.5 panel (a):**
   - In Figure 3.5 panel (a), the remaining carbon budget for 1.5°C (>50% chance) is displayed as 500 GtCO2, marked by a green bar and an extended vertical dashed reference line at 500 GtCO2 [VIS:Figure_3_5:p099].
   - **Existing infrastructure alone:** Projected lifetime CO2 emissions from existing fossil fuel infrastructure without additional abatement already exceed the 500 GtCO2 remaining carbon budget for 1.5°C (the bar extends past the 500 GtCO2 dashed line) [VIS:Figure_3_5:p099] [ADV_TXT:p036:c01].
   - **Existing and planned infrastructure:** When planned infrastructure is included alongside existing infrastructure, projected lifetime CO2 emissions exceed the 1.5°C budget by an even wider margin, extending out to approximately equal the remaining carbon budget for limiting warming to 2°C with an 83% likelihood (near the ~900–1000 GtCO2 dashed line) [VIS:Figure_3_5:p099] [ADV_TXT:p036:c01].
- **Citations:** ['ADV_TXT:p098:c01', 'ADV_TXT:p098:c02', 'VIS:Figure_3_5:p099', 'ADV_TXT:p036:c01']
- **Citation Details:** [{"id": "ADV_TXT:p098:c01", "modality": "text", "label": "Section 3: Long-Term Futures (p.82)", "pdf_page": 98, "printed_page": "82", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p098:c02", "modality": "text", "label": "Section 3: Long-Term Futures (p.82)", "pdf_page": 98, "printed_page": "82", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "VIS:Figure_3_5:p099", "modality": "chart", "label": "Figure 3.5", "pdf_page": 99, "printed_page": "83", "bbox": [45.0, 45.0, 575.0, 520.0], "crop_relpath": "data/advanced/crops/VIS_Figure_3_5_p099.png"}, {"id": "ADV_TXT:p036:c01", "modality": "text", "label": "Summary for Policymakers (p.20)", "pdf_page": 36, "printed_page": "20", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** ['VIS:Figure_3_5:p099']

## adv_dev_14 [text] — `status=answered` | `searches=1` | `inspects=0` | `err=None`
- **Question:** According to SPM A.2.1 (PDF p.21 / printed p.5), by how much did global mean sea level rise in total between 1901 and 2018, and what were the average rates of sea level rise (in mm yr-1) during each of the three sub-periods 1901–1971, 1971–2006, and 2006–2018?
- **Expected Answer:** Global mean sea level increased by 0.20 [0.15 to 0.25] m between 1901 and 2018. The average rate accelerated from 1.3 [0.6 to 2.1] mm yr-1 (1901–1971), to 1.9 [0.8 to 2.9] mm yr-1 (1971–2006), and to 3.7 [3.2 to 4.2] mm yr-1 (2006–2018).
- **Gold Source:** pages `[21]`, regions `[]`, note: Verified verbatim in PDF p.21 (printed p.5), paragraph A.2.1.
- **Agent Answer:** According to SPM A.2.1 (p. 5), the observed changes in global mean sea level are as follows:

- **Total rise between 1901 and 2018:** Global mean sea level increased by **0.20 [0.15 to 0.25] m** [ADV_TXT:p021:c03].
- **Average rate between 1901 and 1971:** **1.3 [0.6 to 2.1] mm yr⁻¹** [ADV_TXT:p021:c03].
- **Average rate between 1971 and 2006:** **1.9 [0.8 to 2.9] mm yr⁻¹** [ADV_TXT:p021:c03].
- **Average rate between 2006 and 2018:** **3.7 [3.2 to 4.2] mm yr⁻¹** (*high confidence*) [ADV_TXT:p021:c03].
- **Citations:** ['ADV_TXT:p021:c03']
- **Citation Details:** [{"id": "ADV_TXT:p021:c03", "modality": "text", "label": "Summary for Policymakers (p.5)", "pdf_page": 21, "printed_page": "5", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_15 [text] — `status=answered` | `searches=2` | `inspects=0` | `err=None`
- **Question:** According to Section 2.2 (PDF p.69 / printed p.53), by what percentages did the unit costs of solar energy, wind energy, and lithium-ion batteries decrease during 2010–2019, what share of global GHG emissions was covered by carbon taxes or emissions trading systems by 2020, and by how much did annual tracked total climate finance flows increase between 2013/14 and 2019/20?
- **Expected Answer:** From 2010–2019, unit costs decreased by 85% for solar energy, 55% for wind energy, and 85% for lithium-ion batteries (with >10x deployment growth for solar and >100x for EVs). By 2020, over 20% of global GHG emissions were covered by carbon taxes or emissions trading systems (though coverage and prices remained insufficient for deep reductions). Annual tracked total climate finance increased by up to 60% between 2013/14 and 2019/20 (with growth slowing since 2018 and most staying within national borders).
- **Gold Source:** pages `[69]`, regions `[]`, note: Verified verbatim in PDF p.69 (printed p.53).
- **Agent Answer:** According to Section 2.2 (printed p. 53 / PDF p. 69) of the IPCC AR6 Synthesis Report:

- **Unit cost decreases (2010–2019):** Sustained decreases occurred in the unit costs of **solar energy** by **85%**, **wind energy** by **55%**, and **lithium-ion batteries** by **85%** [ADV_TXT:p069:c02].
- **Emissions covered by carbon taxes or emissions trading systems (by 2020):** **Over 20%** of global GHG emissions were covered by carbon taxes or emissions trading systems [ADV_TXT:p069:c06].
- **Increase in annual tracked total climate finance flows (between 2013/14 and 2019/20):** Annual tracked total financial flows for climate mitigation and adaptation increased **by up to 60%** [ADV_TXT:p069:c05].
- **Citations:** ['ADV_TXT:p069:c02', 'ADV_TXT:p069:c06', 'ADV_TXT:p069:c05']
- **Citation Details:** [{"id": "ADV_TXT:p069:c02", "modality": "text", "label": "Section 2: Current Status and Trends (p.53)", "pdf_page": 69, "printed_page": "53", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p069:c06", "modality": "text", "label": "Section 2: Current Status and Trends (p.53)", "pdf_page": 69, "printed_page": "53", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p069:c05", "modality": "text", "label": "Section 2: Current Status and Trends (p.53)", "pdf_page": 69, "printed_page": "53", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_16 [text] — `status=answered` | `searches=1` | `inspects=0` | `err=None`
- **Question:** According to Section 2.2.3 and preceding mitigation text on PDF p.71 (printed p.55), how many countries have included adaptation in climate policies/planning, what approximate share of all documented adaptation targets water-related risks, and what magnitude of avoided emissions was estimated in 2016 from laws and executive orders?
- **Expected Answer:** At least 170 countries (and many cities) have included adaptation in climate policies and planning. Water-related risks and impacts account for the majority (~60%) of all documented adaptation. Growing numbers of laws and executive orders were estimated to have resulted in 5.9 GtCO2-eq yr-1 of avoided emissions in 2016 (with at least 1.8 GtCO2-eq yr-1 accounted for by aggregating separate estimates for economic and regulatory instruments).
- **Gold Source:** pages `[71]`, regions `[]`, note: Verified verbatim in PDF p.71 (printed p.55).
- **Agent Answer:** Based on Section 2.2.3 and the preceding mitigation text on PDF p. 71 (printed p. 55):

- **Countries including adaptation in climate policies/planning:** At least 170 countries (along with many cities) [ADV_TXT:p071:c02].
- **Approximate share of documented adaptation targeting water-related risks:** The majority, or approximately 60% (~60%) of all documented adaptation [ADV_TXT:p071:c02].
- **Avoided emissions estimated in 2016 from laws and executive orders:** 5.9 GtCO2-eq yr–1 (medium confidence) [ADV_TXT:p071:c01].
- **Citations:** ['ADV_TXT:p071:c01', 'ADV_TXT:p071:c02']
- **Citation Details:** [{"id": "ADV_TXT:p071:c01", "modality": "text", "label": "Section 2: Current Status and Trends (p.55)", "pdf_page": 71, "printed_page": "55", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p071:c02", "modality": "text", "label": "Section 2: Current Status and Trends (p.55)", "pdf_page": 71, "printed_page": "55", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_17 [text] — `status=answered` | `searches=1` | `inspects=0` | `err=None`
- **Question:** According to Section 3.1.2 and Footnote 122 (PDF p.88 / printed p.72), what four Solar Radiation Modification (SRM) approaches are explicitly named, and what does the report conclude about SRM's effects on atmospheric CO2 concentrations, ocean acidification, and a sudden termination?
- **Expected Answer:** Footnote 122 names four proposed SRM approaches: stratospheric aerosol injection, marine cloud brightening, ground-based albedo modifications, and ocean albedo change. Section 3.1.2 states that SRM would not restore climate to a previous state (leaving residual or overcompensating regional/seasonal changes), would not stop atmospheric CO2 concentrations from increasing nor reduce resulting ocean acidification, and that sudden and sustained termination in a high CO2 scenario would cause rapid climate change (plus international tensions from lack of robust governance).
- **Gold Source:** pages `[88]`, regions `[]`, note: Verified verbatim in PDF p.88 (printed p.72), Section 3.1.2 & Footnote 122.
- **Agent Answer:** According to Section 3.1.2 and Footnote 122 (printed p. 72 / PDF p. 88):

### Four Explicitly Named SRM Approaches
Footnote 122 explicitly names the following four proposed Solar Radiation Modification (SRM) approaches [ADV_TXT:p088:c04]:
1. **Stratospheric aerosol injection** [ADV_TXT:p088:c04]
2. **Marine cloud brightening** [ADV_TXT:p088:c04]
3. **Ground-based albedo modifications** [ADV_TXT:p088:c04]
4. **Ocean albedo change** [ADV_TXT:p088:c04]

---

### Effects of SRM Concluded by the Report
* **Atmospheric $\text{CO}_2$ Concentrations and Ocean Acidification:** 
  The report concludes that SRM would **not** stop atmospheric $\text{CO}_2$ concentrations from increasing, nor would it reduce the resulting ocean acidification under continued anthropogenic emissions (*high confidence*) [ADV_TXT:p088:c03].
* **Sudden Termination:** 
  A sudden and sustained termination of SRM in a high $\text{CO}_2$ emissions scenario would cause rapid climate change (*high confidence*) [ADV_TXT:p088:c03].
- **Citations:** ['ADV_TXT:p088:c03', 'ADV_TXT:p088:c04']
- **Citation Details:** [{"id": "ADV_TXT:p088:c03", "modality": "text", "label": "Section 3: Long-Term Futures (p.72)", "pdf_page": 88, "printed_page": "72", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p088:c04", "modality": "text", "label": "Section 3: Long-Term Futures (p.72)", "pdf_page": 88, "printed_page": "72", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_18 [unanswerable] — `status=abstain` | `searches=5` | `inspects=1` | `err=None`
- **Question:** What were the observed global net anthropogenic greenhouse gas (GHG) emissions (in GtCO2-eq) reported for the years 2022 and 2023 in the IPCC AR6 Synthesis Report?
- **Expected Behavior:** Abstain — The AR6 Synthesis Report's observed historical global GHG emissions inventory ends in 2019 (59 GtCO2-eq) and does not report observed global emissions for 2022 or 2023.
- **Agent Answer:** The IPCC AR6 Synthesis Report does not report observed global net anthropogenic greenhouse gas (GHG) emissions for the years 2022 and 2023. The historical assessment of observed global net anthropogenic GHG emissions in the report extends only through 2019 (estimated at 59 ± 6.6 GtCO2-eq in 2019). Observed emissions data for 2022 and 2023 postdate the report's assessed historical observation period and are therefore not available in the report.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** ['VIS:Figure_2_1:p059']

## adv_dev_19 [unanswerable] — `status=abstain` | `searches=1` | `inspects=2` | `err=None`
- **Question:** In Figure SPM.7 / Figure 4.4 panel (a), what is the assessed mitigation synergy level (High, Medium, or Low) and confidence rating for 'Coastal defence and hardening', and what numerical net lifetime cost bracket (in USD per tCO2-eq) is allocated to 'Electric vehicles'?
- **Expected Behavior:** Abstain — In Figure SPM.7/4.4a, synergies with mitigation for 'Coastal defence and hardening' are explicitly marked 'not assessed', and 'Electric vehicles' is grey ('Cost not allocated due to high variability or lack of data').
- **Agent Answer:** In Figure SPM.7 and Figure 4.4 panel (a):

1. For 'Coastal defence and hardening', the synergy with mitigation is explicitly marked as "not assessed" (no High, Medium, or Low level is assessed, and no confidence rating is provided).
2. For 'Electric vehicles', no numerical net lifetime cost bracket (in USD per tCO2-eq) is allocated; it is shaded grey, which the legend defines as "Cost not allocated due to high variability or lack of data".

Because these elements are explicitly marked "not assessed" and "Cost not allocated", the requested ratings and numerical cost bracket are not provided in the report.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** ['VIS:Figure_4_4:p119', 'VIS:Figure_SPM7:p043']

## adv_dev_20 [unanswerable] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** How much financial compensation was pledged to the Loss and Damage Fund established at COP27 in Sharm el-Sheikh, according to Section 4.8 of the IPCC AR6 Synthesis Report?
- **Expected Behavior:** Abstain — COP27, Sharm el-Sheikh, and the COP27 Loss and Damage Fund do not appear anywhere in the 186-page IPCC AR6 Synthesis Report.
- **Agent Answer:** Section 4.8 of the IPCC AR6 Synthesis Report does not mention or provide any quantified figure for financial compensation pledged to the Loss and Damage Fund established at COP27 in Sharm el-Sheikh. The report addresses climate finance, international cooperation, and mentions the Warsaw International Mechanism on Loss and Damage (established in 2013) and Article 8 of the Paris Agreement, but it does not assess or record specific financial pledges to a COP27 Loss and Damage Fund. Consequently, the requested evidence is missing from the report.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []
