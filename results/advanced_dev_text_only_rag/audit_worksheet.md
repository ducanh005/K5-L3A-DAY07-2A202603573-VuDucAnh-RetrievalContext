# Advanced Audit Worksheet — `text_only_rag` (`dev`, N=20)

## adv_dev_01 [table] — `status=answered` | `searches=5` | `inspects=0` | `err=None`
- **Question:** According to Box SPM.1, Table 1, which WGIII modelled pathway categories have a corresponding RCPy designation listed for WGI and WGII, and what are their respective category descriptions, GHG emissions scenarios (SSPx-y), and RCPy labels?
- **Expected Answer:** Three categories have RCPy designations: C3 ('limit warming to 2°C (>67%)', Low (SSP1-2.6), RCP2.6), C6 ('limit warming to 3°C (>50%)', Intermediate (SSP2-4.5), RCP 4.5), and C8 ('exceed warming of 4°C (>50%)', Very high (SSP5-8.5), RCP 8.5).
- **Gold Source:** pages `[26]`, regions `['VIS:Table_Box_SPM1:p026']`, note: Verified from VIS_Table_Box_SPM1_p026.png (PDF p.26, printed p.10): only rows C3, C6, and C8 have populated RCPy cells.
- **Agent Answer:** According to Box SPM.1, Table 1, the WGIII modelled pathway categories that have a corresponding RCPy designation listed for WGI and WGII are **C3**, **C6**, and **C8** [ADV_TXT:p026:c01]. 

Their respective details are as follows:

- **Category C3**:
  - **Category description**: limit warming to 2°C (>67%) [ADV_TXT:p026:c01]
  - **GHG emissions scenario (SSPx-y)**: Low (SSP1-2.6) [ADV_TXT:p026:c01]
  - **RCPy label**: RCP2.6 [ADV_TXT:p026:c01]

- **Category C6**:
  - **Category description**: limit warming to 3°C (>50%) [ADV_TXT:p026:c01]
  - **GHG emissions scenario (SSPx-y)**: Intermediate (SSP2-4.5) [ADV_TXT:p026:c01]
  - **RCPy label**: RCP 4.5 [ADV_TXT:p026:c01]

- **Category C8**:
  - **Category description**: exceed warming of 4°C (>50%) [ADV_TXT:p026:c01]
  - **GHG emissions scenario (SSPx-y)**: Very high (SSP5-8.5) [ADV_TXT:p026:c01]
  - **RCPy label**: RCP 8.5 [ADV_TXT:p026:c01]
- **Citations:** ['ADV_TXT:p026:c01']
- **Citation Details:** [{"id": "ADV_TXT:p026:c01", "modality": "text", "label": "Summary for Policymakers (p.10)", "pdf_page": 26, "printed_page": "10", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_02 [table] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** In Table 2.1, what are the assessed confidence/likelihood levels (from the colour key) and any cell text annotations for both 'Observed change assessment' and 'Human contribution assessment' on 'Greenland ice sheet mass loss since 1990s' and 'Antarctic ice sheet mass loss since 1990s'?
- **Expected Answer:** Greenland ice sheet mass loss since 1990s: Observed change = virtually certain (dark maroon), Human contribution = medium confidence (pale cream, no extra text). Antarctic ice sheet mass loss since 1990s: Observed change = very likely (orange), Human contribution = Limited evidence & medium agreement (unshaded cell with text).
- **Gold Source:** pages `[63]`, regions `['VIS:Table_2_1:p063']`, note: Verified from VIS_Table_2_1_p063.png (PDF p.63, printed p.47) under Cryosphere rows; cells encode likelihood purely via color key.
- **Agent Answer:** The provided context does not contain sufficient evidence to determine the specific assessed confidence/likelihood levels (from the colour key) or the cell text annotations in Table 2.1 for 'Greenland ice sheet mass loss since 1990s' and 'Antarctic ice sheet mass loss since 1990s'. While Table 2.1 appears on page 47 (ADV_TXT:p063:c01), the retrieved text only contains the caption and fragmented elements without the specific table rows, colour key classifications, or cell annotations for these cryospheric indicators.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []

## adv_dev_03 [table] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** In Figure SPM.7 panel (a) under 'SETTLEMENTS AND INFRASTRUCTURE' in the left-hand 'Climate responses and adaptation options' table, what are the assessed potential feasibility levels (up to 1.5°C), synergies with mitigation, and confidence dot levels for all three listed options?
- **Expected Answer:** 1) Sustainable urban water management: Potential feasibility = Medium (2 dots / Medium confidence), Synergies = Low (1 dot / Low confidence). 2) Sustainable land use and urban planning: Potential feasibility = Medium (2 dots / Medium confidence), Synergies = High (1 dot / Low confidence). 3) Green infrastructure and ecosystem services: Potential feasibility = Medium (3 dots / High confidence), Synergies = High (2 dots / Medium confidence).
- **Gold Source:** pages `[43]`, regions `['VIS:Table_SPM7_Feasibility:p043']`, note: Verified from VIS_Table_SPM7_Feasibility_p043.png (PDF p.43, printed p.27) matrix legend and SETTLEMENTS AND INFRASTRUCTURE block.
- **Agent Answer:** The retrieved evidence does not contain the visual table data from Figure SPM.7 panel (a). Specifically, while the figure caption and context are partially retrieved (noting that feasibility, feasibility dimensions, and synergies with mitigation are assessed at high, medium, or low levels along with confidence levels), the specific assessed potential feasibility levels (up to 1.5°C), synergies with mitigation, and confidence dot levels for the three options listed under 'SETTLEMENTS AND INFRASTRUCTURE' are not present in the accessible text chunks and the visual panel could not be inspected within the available search budget.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []

## adv_dev_04 [diagram_map] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** In Figure SPM.1 panel (a) under 'Water availability and food production', which specific indicators show both 'Adverse and positive impacts' (striped red-and-green circles) at the global level, which shows solely 'Adverse impacts', and what is the attribution confidence level for all four indicators?
- **Expected Answer:** Physical water availability, Animal and livestock health and productivity, and Fisheries yields and aquaculture production show both 'Adverse and positive impacts' (striped red-and-green), whereas Agriculture/crop production shows solid red 'Adverse impacts' only. All four indicators in that group have Medium confidence (2 dots).
- **Gold Source:** pages `[23]`, regions `['VIS:Figure_SPM1:p023']`, note: Verified from VIS_Figure_SPM1_p023.png (PDF p.23, printed p.7), top-left block under Water availability and food production + Key.
- **Agent Answer:** The retrieved text chunks do not contain sufficient evidence to fully identify all four indicators under 'Water availability and food production' in Figure SPM.1 panel (a), their specific global impact patterns (whether striped red-and-green indicating both adverse and positive impacts, or solely adverse impacts), or their respective attribution confidence levels, as the visual figure itself could not be inspected before the tool budget was exhausted.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []

## adv_dev_05 [diagram_map] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** In Cross-Section Box.2 Figure 1 panel (a) (p.81 / printed p.65), list the three horizontal chain blocks downstream of 'Socio-economic changes', identify the two policy boxes linked underneath them, and list all five SSP scenarios plotted in the central 21st-century temperature graph.
- **Expected Answer:** Downstream from 'Socio-economic changes', the horizontal chain runs: 'Emissions' -> 'Climate' -> 'Impacts / Risks' (with feedback/influence arrows looping back to Socio-economic changes). The two policy boxes underneath are 'Mitigation Policy' (under Emissions) and 'Adaptation Policy' (under Impacts / Risks). The five SSP scenarios plotted are SSP1-1.9, SSP1-2.6, SSP2-4.5, SSP3-7.0, and SSP5-8.5.
- **Gold Source:** pages `[81, 82]`, regions `['VIS:CrossBox2_Diagram:p081']`, note: Verified from VIS_CrossBox2_Diagram_p081.png (PDF p.81) and caption on PDF p.82.
- **Agent Answer:** Không đủ bằng chứng trong tài liệu để trả lời.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []

## adv_dev_06 [diagram_map] — `status=answered` | `searches=1` | `inspects=0` | `err=None`
- **Question:** In Figure 3.1 (p.86 / printed p.70), when was global surface temperature last sustained at or above 2.5°C according to the annotation on the Global warming level (GWL) scale, and how does panel (b) define the '1 standard deviation' unit for annual mean total column soil moisture change?
- **Expected Answer:** The annotation states the last time global surface temperature was sustained at or above 2.5°C was over 3 million years ago. In panel (b), soil moisture change is expressed in standard deviation (σ) of interannual variability during 1850–1900, where a projected reduction of 1 standard deviation corresponds to soil moisture conditions typical of droughts occurring about once every six years during 1850–1900 (also noting differences from precipitation due to evapotranspiration).
- **Gold Source:** pages `[86]`, regions `['VIS:Figure_3_1:p086']`, note: Verified from VIS_Figure_3_1_p086.png (PDF p.86, printed p.70) top GWL annotation and caption text.
- **Agent Answer:** According to Figure 3.1 (printed p. 70, pdf p. 86):

1. **Past sustained temperature at or above 2.5°C:** 
The annotation on the Global warming level (GWL) scale states that "the last time global surface temperature was sustained at or above 2.5°C was over 3 million years ago" [ADV_TXT:p086:c01].

2. **Definition of the '1 standard deviation' unit in panel (b):**
The caption specifies that the unit in panel (b) is "the standard deviation of interannual variability in soil moisture during 1850-1900" [ADV_TXT:p086:c02], [ADV_TXT:p086:c03]. It further explains that "a projected reduction in mean soil moisture by one standard deviation corresponds to soil moisture conditions typical of droughts that occurred about once every six years during 1850-1900" [ADV_TXT:p086:c03].
- **Citations:** ['ADV_TXT:p086:c01', 'ADV_TXT:p086:c02', 'ADV_TXT:p086:c03']
- **Citation Details:** [{"id": "ADV_TXT:p086:c01", "modality": "text", "label": "Section 3: Long-Term Futures (p.70)", "pdf_page": 86, "printed_page": "70", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p086:c02", "modality": "text", "label": "Section 3: Long-Term Futures (p.70)", "pdf_page": 86, "printed_page": "70", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p086:c03", "modality": "text", "label": "Section 3: Long-Term Futures (p.70)", "pdf_page": 86, "printed_page": "70", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_07 [chart] — `status=abstain` | `searches=1` | `inspects=0` | `err=None`
- **Question:** According to Figure 2.1 panels (b) and (c) (p.59 / printed p.43), what were the annotated 2019 atmospheric concentrations (value and unit) of CO2, CH4, and N2O, and by how much had global surface temperature increased by 2011–2020 compared to 1850–1900?
- **Expected Answer:** 2019 atmospheric concentrations (panel b): Carbon dioxide (CO2) = 410 ppm, Methane (CH4) = 1866 ppb, Nitrous oxide (N2O) = 332 ppb. Global surface temperature (panel c) increased by 1.1°C by 2011–2020 compared to 1850–1900.
- **Gold Source:** pages `[59]`, regions `['VIS:Figure_2_1:p059']`, note: Verified from VIS_Figure_2_1_p059.png (PDF p.59, printed p.43), annotated labels on panels (b) and (c).
- **Agent Answer:** Không đủ bằng chứng trong tài liệu để trả lời.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []

## adv_dev_08 [chart] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** In Figure 2.2 panel (c) ('Global net anthropogenic GHG emissions by region 1990–2019', p.61 / printed p.45), what were the total global net anthropogenic GHG emissions (GtCO2-eq) and Eastern Asia's percentage share in 1990, 2000, 2010, and 2019?
- **Expected Answer:** Total global net GHG emissions: 38 GtCO2-eq in 1990, 42 GtCO2-eq in 2000, 53 GtCO2-eq in 2010, and 59 GtCO2-eq in 2019. Eastern Asia's percentage share rose from 13% (1990) to 16% (2000), 24% (2010), and 27% (2019).
- **Gold Source:** pages `[61]`, regions `['VIS:Figure_2_2_charts:p061']`, note: Verified from VIS_Figure_2_2_charts_p061.png (PDF p.61, printed p.45), panel (c) vertical year callouts.
- **Agent Answer:** Không đủ bằng chứng trong tài liệu để trả lời.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []

## adv_dev_09 [chart] — `status=answered` | `searches=4` | `inspects=0` | `err=None`
- **Question:** In Figure 2.4 (p.70 / printed p.54), what cost range defines the yellow 'Fossil fuel cost (2020)' reference band in USD per MWh, how does the panel (a) y-axis unit for Passenger EV Li-ion battery packs differ from the renewables panels, and what are the different y-axis units and scales in panel (b) ('Market Adoption')?
- **Expected Answer:** The yellow 'Fossil fuel cost (2020)' band corresponds to USD 55 to 148 per MWh (for new coal and gas power). In panel (a), Photovoltaics (PV), Onshore wind, and Offshore wind plot LCOE in $2020/MWh (0–600), whereas Li-ion battery packs plot Cost in $2020/kWh (0–1600). In panel (b), PV and Onshore wind plot cumulative capacity in GW (0–800 scale), Offshore wind uses GW on a smaller 0–40 scale, and Passenger EVs plot Adoption in millions of EVs (0–8).
- **Gold Source:** pages `[70]`, regions `['VIS:Figure_2_4:p070']`, note: Verified from VIS_Figure_2_4_p070.png (PDF p.70, printed p.54) panel axes, yellow legend, and caption.
- **Agent Answer:** Based on Figure 2.4 and its caption (p. 70 / printed p. 54):

1. **Yellow 'Fossil fuel cost (2020)' reference band range:**
   The yellow shading corresponds to a cost range of **USD 55 to 148 per MWh** for new fossil fuel (coal and gas) power in 2020 [ADV_TXT:p070:c02].

2. **Difference in panel (a) y-axis units:**
   - For the renewable energy panels (Photovoltaics, Onshore wind, and Offshore wind), the y-axis unit is **USD per MWh** (`Cost ($2020/MWh)`), reflecting the levelised cost of energy (LCOE) per MWh of electricity produced [ADV_TXT:p070:c01], [ADV_TXT:p070:c02].
   - For Passenger EV Li-ion battery packs, the y-axis unit is **USD per kWh** (`Cost ($2020/kWh)`), representing the cost for 1 kWh of battery storage capacity [ADV_TXT:p070:c01], [ADV_TXT:p070:c02].

3. **Y-axis units and scales in panel (b) ('Market Adoption'):**
   - **Units:**
     - Renewable energies are measured in **GW of installed capacity** (`Adoption (GW)`) [ADV_TXT:p070:c01], [ADV_TXT:p070:c03].
     - Passenger electric vehicles are measured in **millions of vehicles** (`Adoption (millions of EVs)`) [ADV_TXT:p070:c01], [ADV_TXT:p070:c03].
   - **Scales:**
     - Passenger electric vehicles scale ranges from **0 to 8** (millions of EVs; tick marks at 0, 2, 4, 6, 8) [ADV_TXT:p070:c01].
     - Photovoltaics and Onshore wind share a scale from **0 to 800** GW (tick marks at 0, 200, 400, 600, 800) [ADV_TXT:p070:c01].
     - Offshore wind uses a smaller scale from **0 to 40** GW (tick marks at 0, 10, 20, 30, 40) [ADV_TXT:p070:c01].
- **Citations:** ['ADV_TXT:p070:c01', 'ADV_TXT:p070:c02', 'ADV_TXT:p070:c03']
- **Citation Details:** [{"id": "ADV_TXT:p070:c01", "modality": "text", "label": "Section 2: Current Status and Trends (p.54)", "pdf_page": 70, "printed_page": "54", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p070:c02", "modality": "text", "label": "Section 2: Current Status and Trends (p.54)", "pdf_page": 70, "printed_page": "54", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p070:c03", "modality": "text", "label": "Section 2: Current Status and Trends (p.54)", "pdf_page": 70, "printed_page": "54", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_10 [chart] — `status=answered` | `searches=5` | `inspects=0` | `err=None`
- **Question:** In Figure 3.6 panel (c) ('Timing for net zero', p.102 / printed p.86), compare when global modelled pathways reach net zero CO2 versus net zero GHG under Category C1 (1.5°C >50%, no or limited overshoot) vs Category C3 (2°C >67%).
- **Expected Answer:** In both pathways CO2 reaches net zero earlier than total GHGs. Under 1.5°C (C1), net zero CO2 median is around early 2050s (~2050–2055), while net zero GHG median is much later (~late 2090s, around 2095–2100) and annotated 'not all scenarios reach net zero GHG by 2100'. Under 2°C (C3), net zero CO2 median shifts to around 2070 (~2070–2075), while the median for net zero GHG does not occur before 2100 (shaded bar appears only from late 2080s–2100).
- **Gold Source:** pages `[102]`, regions `['VIS:Figure_3_6:p102']`, note: Verified from VIS_Figure_3_6_p102.png (PDF p.102, printed p.86) panel (c) vertical median markers and callout.
- **Agent Answer:** Based on Figure 3.6 panel (c) and its associated text on pages 85–86 (pdf pages 101–102) of the report:

1. **Net Zero $\text{CO}_2$ vs. Net Zero GHG Timing**:
   - In all pathways, **total greenhouse gases (GHGs) reach net zero later than $\text{CO}_2$** [ADV_TXT:p101:c03], [ADV_TXT:p102:c01]. This occurs because residual non-$\text{CO}_2$ emissions (such as $\text{CH}_4$, $\text{N}_2\text{O}$, and F-gases) remain and must be counterbalanced by net negative $\text{CO}_2$ emissions [ADV_TXT:p101:c03].

2. **Category C1 ($1.5^\circ\text{C}$ >50%, no or limited overshoot)**:
   - Global modelled pathways reach **net zero $\text{CO}_2$ emissions around 2050** (early 2050s) [ADV_TXT:p101:c03], [ADV_TXT:p102:c01].
   - **Net zero GHG emissions** are reached later, in the second half of the century [ADV_TXT:p101:c03], [ADV_TXT:p102:c01].

3. **Category C3 ($2^\circ\text{C}$ >67%)**:
   - Global modelled pathways reach **net zero $\text{CO}_2$ emissions around the early 2070s** [ADV_TXT:p101:c03], which is approximately two decades later than in Category C1.
   - For **net zero GHG emissions**, pathways reach it even later than $\text{CO}_2$, and panel (c) explicitly notes that **not all scenarios reach net zero GHG by 2100** [ADV_TXT:p102:c01].
- **Citations:** ['ADV_TXT:p101:c03', 'ADV_TXT:p102:c01']
- **Citation Details:** [{"id": "ADV_TXT:p101:c03", "modality": "text", "label": "Section 3: Long-Term Futures (p.85)", "pdf_page": 101, "printed_page": "85", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p102:c01", "modality": "text", "label": "Section 3: Long-Term Futures (p.86)", "pdf_page": 102, "printed_page": "86", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_11 [multi_hop] — `status=answered` | `searches=5` | `inspects=0` | `err=None`
- **Question:** Using Figure 2.2 panel (a) and panel (d) on p.61 (printed p.45), compare 'North America' and 'Southern Asia': state each region's share (%) of historical cumulative net CO2 emissions (1850–2019), 2019 population (million persons), 2019 GDP per capita (USD1000_PPP 2017), and 2019 net GHG per capita (tCO2-eq/person).
- **Expected Answer:** Historical cumulative CO2 emissions (1850–2019, panel a): North America = 23% vs Southern Asia = 4%. Regional indicators (2019, panel d): North America has 366 million population, 61 USD1000_PPP 2017 GDP per capita, and 19 tCO2-eq/person net GHG; Southern Asia has 1836 million population, 6.2 USD1000_PPP 2017 GDP per capita, and 2.6 tCO2-eq/person net GHG.
- **Gold Source:** pages `[61]`, regions `['VIS:Figure_2_2_charts:p061', 'VIS:Table_Fig2_2d:p061']`, note: Verified by joining bar percentages in VIS_Figure_2_2_charts_p061.png (panel a) and table columns in VIS_Table_Fig2_2d_p061.png (panel d).
- **Agent Answer:** Based on Figure 2.2 on page 61 (printed page 45) of the Longer Report:

### **North America**
- **Share of historical cumulative net CO₂ emissions (1850–2019) [Panel (a)]:** 23% [ADV_TXT:p061:c01]
- **2019 Population [Panel (d)]:** 366 million persons [ADV_TXT:p061:c01, ADV_TXT:p061:c02]
- **2019 GDP per capita [Panel (d)]:** 61 USD1000_PPP 2017 per person [ADV_TXT:p061:c02]
- **2019 Net GHG per capita [Panel (d)]:** 19 tCO₂-eq per person [ADV_TXT:p061:c02]

---

### **Southern Asia**
- **Share of historical cumulative net CO₂ emissions (1850–2019) [Panel (a)]:** 4% [ADV_TXT:p061:c01]
- **2019 Population [Panel (d)]:** 1836 million persons [ADV_TXT:p061:c02]
- **2019 GDP per capita [Panel (d)]:** 6.2 USD1000_PPP 2017 per person [ADV_TXT:p061:c02]
- **2019 Net GHG per capita [Panel (d)]:** 2.6 tCO₂-eq per person [ADV_TXT:p061:c02]
- **Citations:** ['ADV_TXT:p061:c01', 'ADV_TXT:p061:c02']
- **Citation Details:** [{"id": "ADV_TXT:p061:c01", "modality": "text", "label": "Section 2: Current Status and Trends (p.45)", "pdf_page": 61, "printed_page": "45", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p061:c02", "modality": "text", "label": "Section 2: Current Status and Trends (p.45)", "pdf_page": 61, "printed_page": "45", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_12 [multi_hop] — `status=answered` | `searches=5` | `inspects=0` | `err=None`
- **Question:** Combining Table 2.2 (p.74) and Figure 2.5 (p.75), state for 2030: (1) median projected emissions and [min–max] (GtCO2-eq/yr) for 'policies implemented by end of 2020' vs COP26 NDCs (unconditional and conditional), (2) percentage change from 2019 shown in Figure 2.5 panel (b) for implemented policies, NDCs, 2°C (>67%), and 1.5°C (>50%), and (3) the 2030 emissions gap between NDCs and 1.5°C pathways.
- **Expected Answer:** 1) Table 2.2 2030 projected emissions (GtCO2-eq/yr): Implemented policies = 57 [52–60]; NDCs unconditional = 53 [50–57]; NDCs including conditional = 50 [47–55]. 2) Figure 2.5(b) 2030 change relative to 2019: Implemented policies = +5%, NDCs = -4%, Limit warming to 2°C (>67%) = -26%, Limit warming to 1.5°C (>50%) = -43%. 3) 2030 emissions gap between NDCs and 1.5°C (>50% no/limited overshoot): 19–26 GtCO2-eq/yr (unconditional) and 16–23 GtCO2-eq/yr (conditional).
- **Gold Source:** pages `[74, 75]`, regions `['VIS:Table_2_2:p074', 'VIS:Figure_2_5:p075']`, note: Verified from VIS_Table_2_2_p074.png (p.74) and VIS_Figure_2_5_p075.png (p.75).
- **Agent Answer:** Based on **Table 2.2** (p. 74) and **Figure 2.5** (p. 75) of the AR6 Synthesis Report:

### 1. Median Projected Global Emissions in 2030 and [min–max] (GtCO2-eq/yr)
* **Policies implemented by the end of 2020:** **57 [52–60] GtCO2-eq/yr** [ADV_TXT:p073:c06] [ADV_TXT:p074:c03].
* **NDCs announced prior to COP26:**
  * **Unconditional elements:** **53 [50–57] GtCO2-eq/yr** [ADV_TXT:p074:c03].
  * **Including conditional elements:** **50 [47–55] GtCO2-eq/yr** [ADV_TXT:p074:c03].

---

### 2. Percentage Change in Emissions from 2019 to 2030 (Figure 2.5, Panel b)
Figure 2.5 panel (b) shows the following emission changes relative to 2019 [ADV_TXT:p075:c01]:
* **Trend from implemented policies:** **+5%**
* **NDCs until 2030:** **–4%**
* **Limit warming to 2°C (>67%):** **–26%**
* **Limit warming to 1.5°C (>50%) with no or limited overshoot:** **–43%**

---

### 3. 2030 Emissions Gap Between NDCs and 1.5°C Pathways
According to Table 2.2, the 2030 emissions gap between NDCs and pathways that limit warming to 1.5°C (>50%) with no or limited overshoot (with immediate action) is **19–26 GtCO2-eq/yr** [ADV_TXT:p074:c03]. *(For context, the emissions gap between NDCs and pathways limiting warming to 2°C (>67%) is 10–16 GtCO2-eq/yr for unconditional NDCs and 6–14 GtCO2-eq/yr including conditional elements)* [ADV_TXT:p074:c03].
- **Citations:** ['ADV_TXT:p073:c06', 'ADV_TXT:p074:c03', 'ADV_TXT:p075:c01']
- **Citation Details:** [{"id": "ADV_TXT:p073:c06", "modality": "text", "label": "Section 2: Current Status and Trends (p.57)", "pdf_page": 73, "printed_page": "57", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p074:c03", "modality": "text", "label": "Section 2: Current Status and Trends (p.58)", "pdf_page": 74, "printed_page": "58", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p075:c01", "modality": "text", "label": "Section 2: Current Status and Trends (p.59)", "pdf_page": 75, "printed_page": "59", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_13 [multi_hop] — `status=answered` | `searches=5` | `inspects=0` | `err=None`
- **Question:** Combine Section 3.3.1 (p.98) and Figure 3.5 panel (a) (p.99): state the global warming increment per 1000 GtCO2 emitted, the remaining carbon budget from the beginning of 2020 for limiting warming to 1.5°C (50% likelihood), and explain how Figure 3.5 panel (a) compares that 1.5°C budget against lifetime CO2 emissions from existing and planned fossil fuel infrastructure without additional abatement.
- **Expected Answer:** Section 3.3.1 (p.98): for every 1000 GtCO2 emitted by human activity, global mean temperature rises by likely 0.27°C to 0.63°C (best estimate 0.45°C). The remaining carbon budget from 2020 for 1.5°C (50% likelihood) is estimated at 500 GtCO2 (varying 300–600 GtCO2 depending on non-CO2 warming). Figure 3.5 panel (a) shows that cumulative lifetime CO2 emissions from existing fossil fuel infrastructure alone (without additional abatement) already exceed the 500 GtCO2 dashed line for 1.5°C (>50%), and existing plus planned infrastructure approaches the 2°C (83%, 900 GtCO2) line.
- **Gold Source:** pages `[98, 99]`, regions `['VIS:Figure_3_5:p099']`, note: Verified from PDF p.98 text (Section 3.3.1) and VIS_Figure_3_5_p099.png panel (a).
- **Agent Answer:** Based on Section 3.3.1 and Figure 3.5 panel (a):

1. **Global warming increment per 1000 GtCO2 emitted:**
   For every 1000 GtCO2 emitted by human activity, global mean temperature increases by a likely range of 0.27°C to 0.63°C, with a best estimate of 0.45°C [ADV_TXT:p098:c01].

2. **Remaining carbon budget for 1.5°C (50% likelihood):**
   From the beginning of 2020, the best estimate of the remaining carbon budget for limiting global warming to 1.5°C with a 50% likelihood is 500 GtCO2 (with a range of 300 to 600 GtCO2 depending on non-CO2 warming) [ADV_TXT:p098:c02].

3. **Comparison with lifetime fossil fuel infrastructure emissions in Figure 3.5 panel (a):**
   Figure 3.5 panel (a) compares remaining carbon budgets against projected lifetime emissions from fossil fuel infrastructure without additional abatement (if historical operating patterns are maintained) [ADV_TXT:p099:c01]:
   - Projected lifetime emissions from **existing** fossil fuel infrastructure alone already exceed the remaining carbon budget for limiting warming to 1.5°C (>50% chance) [ADV_TXT:p036:c01], [ADV_TXT:p074:c01], [ADV_TXT:p099:c01].
   - Projected lifetime emissions from **existing and planned** fossil fuel infrastructure exceed the 1.5°C budget by an even larger margin, reaching a level approximately equal to the remaining carbon budget for limiting warming to 2°C with an 83% likelihood [ADV_TXT:p036:c01], [ADV_TXT:p074:c01], [ADV_TXT:p099:c01].
- **Citations:** ['ADV_TXT:p098:c01', 'ADV_TXT:p098:c02', 'ADV_TXT:p099:c01', 'ADV_TXT:p036:c01', 'ADV_TXT:p074:c01']
- **Citation Details:** [{"id": "ADV_TXT:p098:c01", "modality": "text", "label": "Section 3: Long-Term Futures (p.82)", "pdf_page": 98, "printed_page": "82", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p098:c02", "modality": "text", "label": "Section 3: Long-Term Futures (p.82)", "pdf_page": 98, "printed_page": "82", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p099:c01", "modality": "text", "label": "Section 3: Long-Term Futures (p.83)", "pdf_page": 99, "printed_page": "83", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p036:c01", "modality": "text", "label": "Summary for Policymakers (p.20)", "pdf_page": 36, "printed_page": "20", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p074:c01", "modality": "text", "label": "Section 2: Current Status and Trends (p.58)", "pdf_page": 74, "printed_page": "58", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_14 [text] — `status=answered` | `searches=1` | `inspects=0` | `err=None`
- **Question:** According to SPM A.2.1 (PDF p.21 / printed p.5), by how much did global mean sea level rise in total between 1901 and 2018, and what were the average rates of sea level rise (in mm yr-1) during each of the three sub-periods 1901–1971, 1971–2006, and 2006–2018?
- **Expected Answer:** Global mean sea level increased by 0.20 [0.15 to 0.25] m between 1901 and 2018. The average rate accelerated from 1.3 [0.6 to 2.1] mm yr-1 (1901–1971), to 1.9 [0.8 to 2.9] mm yr-1 (1971–2006), and to 3.7 [3.2 to 4.2] mm yr-1 (2006–2018).
- **Gold Source:** pages `[21]`, regions `[]`, note: Verified verbatim in PDF p.21 (printed p.5), paragraph A.2.1.
- **Agent Answer:** According to SPM A.2.1, global mean sea level and its rate of rise changed as follows [ADV_TXT:p021:c03]:

- **Total rise between 1901 and 2018:** increased by **0.20 [0.15 to 0.25] m** [ADV_TXT:p021:c03].
- **Average rate of sea level rise by sub-period (high confidence):**
  - **1901–1971:** **1.3 [0.6 to 2.1] mm yr⁻¹** [ADV_TXT:p021:c03]
  - **1971–2006:** **1.9 [0.8 to 2.9] mm yr⁻¹** [ADV_TXT:p021:c03]
  - **2006–2018:** **3.7 [3.2 to 4.2] mm yr⁻¹** [ADV_TXT:p021:c03]
- **Citations:** ['ADV_TXT:p021:c03']
- **Citation Details:** [{"id": "ADV_TXT:p021:c03", "modality": "text", "label": "Summary for Policymakers (p.5)", "pdf_page": 21, "printed_page": "5", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_15 [text] — `status=answered` | `searches=2` | `inspects=0` | `err=None`
- **Question:** According to Section 2.2 (PDF p.69 / printed p.53), by what percentages did the unit costs of solar energy, wind energy, and lithium-ion batteries decrease during 2010–2019, what share of global GHG emissions was covered by carbon taxes or emissions trading systems by 2020, and by how much did annual tracked total climate finance flows increase between 2013/14 and 2019/20?
- **Expected Answer:** From 2010–2019, unit costs decreased by 85% for solar energy, 55% for wind energy, and 85% for lithium-ion batteries (with >10x deployment growth for solar and >100x for EVs). By 2020, over 20% of global GHG emissions were covered by carbon taxes or emissions trading systems (though coverage and prices remained insufficient for deep reductions). Annual tracked total climate finance increased by up to 60% between 2013/14 and 2019/20 (with growth slowing since 2018 and most staying within national borders).
- **Gold Source:** pages `[69]`, regions `[]`, note: Verified verbatim in PDF p.69 (printed p.53).
- **Agent Answer:** According to Section 2.2 (PDF p. 69 / printed p. 53):

- **Unit cost decreases (2010–2019):** Sustained decreases occurred in the unit costs of **solar energy (by 85%)**, **wind energy (by 55%)**, and **lithium-ion batteries (by 85%)** [ADV_TXT:p069:c02].
- **Emissions covered by carbon pricing (by 2020):** **Over 20%** of global GHG emissions were covered by carbon taxes or emissions trading systems [ADV_TXT:p069:c06].
- **Increase in annual tracked total climate finance flows (2013/14 to 2019/20):** Annual tracked total financial flows for climate mitigation and adaptation increased **by up to 60%** between 2013/14 and 2019/20 [ADV_TXT:p069:c05].
- **Citations:** ['ADV_TXT:p069:c02', 'ADV_TXT:p069:c05', 'ADV_TXT:p069:c06']
- **Citation Details:** [{"id": "ADV_TXT:p069:c02", "modality": "text", "label": "Section 2: Current Status and Trends (p.53)", "pdf_page": 69, "printed_page": "53", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p069:c05", "modality": "text", "label": "Section 2: Current Status and Trends (p.53)", "pdf_page": 69, "printed_page": "53", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p069:c06", "modality": "text", "label": "Section 2: Current Status and Trends (p.53)", "pdf_page": 69, "printed_page": "53", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_16 [text] — `status=answered` | `searches=1` | `inspects=0` | `err=None`
- **Question:** According to Section 2.2.3 and preceding mitigation text on PDF p.71 (printed p.55), how many countries have included adaptation in climate policies/planning, what approximate share of all documented adaptation targets water-related risks, and what magnitude of avoided emissions was estimated in 2016 from laws and executive orders?
- **Expected Answer:** At least 170 countries (and many cities) have included adaptation in climate policies and planning. Water-related risks and impacts account for the majority (~60%) of all documented adaptation. Growing numbers of laws and executive orders were estimated to have resulted in 5.9 GtCO2-eq yr-1 of avoided emissions in 2016 (with at least 1.8 GtCO2-eq yr-1 accounted for by aggregating separate estimates for economic and regulatory instruments).
- **Gold Source:** pages `[71]`, regions `[]`, note: Verified verbatim in PDF p.71 (printed p.55).
- **Agent Answer:** According to Section 2.2.3 and the preceding mitigation text on PDF p. 71 (printed p. 55):

- **Avoided emissions from laws and executive orders in 2016:** Growing numbers of laws and executive orders are estimated to have resulted in **5.9 GtCO2-eq yr–1** of avoided emissions in 2016 (medium confidence) [ADV_TXT:p071:c01].
- **Countries including adaptation in policies/planning:** **At least 170 countries** (and many cities) have included adaptation in their climate policies and planning processes (high confidence) [ADV_TXT:p071:c02].
- **Share of documented adaptation targeting water-related risks:** Adaptation to water-related risks and impacts accounts for the majority, or approximately **~60%**, of all documented adaptation (high confidence) [ADV_TXT:p071:c02].
- **Citations:** ['ADV_TXT:p071:c01', 'ADV_TXT:p071:c02']
- **Citation Details:** [{"id": "ADV_TXT:p071:c01", "modality": "text", "label": "Section 2: Current Status and Trends (p.55)", "pdf_page": 71, "printed_page": "55", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p071:c02", "modality": "text", "label": "Section 2: Current Status and Trends (p.55)", "pdf_page": 71, "printed_page": "55", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_17 [text] — `status=answered` | `searches=1` | `inspects=0` | `err=None`
- **Question:** According to Section 3.1.2 and Footnote 122 (PDF p.88 / printed p.72), what four Solar Radiation Modification (SRM) approaches are explicitly named, and what does the report conclude about SRM's effects on atmospheric CO2 concentrations, ocean acidification, and a sudden termination?
- **Expected Answer:** Footnote 122 names four proposed SRM approaches: stratospheric aerosol injection, marine cloud brightening, ground-based albedo modifications, and ocean albedo change. Section 3.1.2 states that SRM would not restore climate to a previous state (leaving residual or overcompensating regional/seasonal changes), would not stop atmospheric CO2 concentrations from increasing nor reduce resulting ocean acidification, and that sudden and sustained termination in a high CO2 scenario would cause rapid climate change (plus international tensions from lack of robust governance).
- **Gold Source:** pages `[88]`, regions `[]`, note: Verified verbatim in PDF p.88 (printed p.72), Section 3.1.2 & Footnote 122.
- **Agent Answer:** According to Section 3.1.2 and Footnote 122 (page 72 / PDF page 88):

**Four explicitly named Solar Radiation Modification (SRM) approaches:**
Footnote 122 explicitly names the following four proposed SRM approaches [ADV_TXT:p088:c04]:
1. Stratospheric aerosol injection
2. Marine cloud brightening
3. Ground-based albedo modifications
4. Ocean albedo change

**Conclusions regarding SRM's effects:**
* **Atmospheric $\text{CO}_2$ concentrations:** SRM would not stop atmospheric $\text{CO}_2$ concentrations from increasing under continued anthropogenic emissions (*high confidence*) [ADV_TXT:p088:c03].
* **Ocean acidification:** SRM would not reduce resulting ocean acidification under continued anthropogenic emissions (*high confidence*) [ADV_TXT:p088:c03].
* **Sudden termination:** A sudden and sustained termination of SRM in a high $\text{CO}_2$ emissions scenario would cause rapid climate change (*high confidence*) [ADV_TXT:p088:c03].
- **Citations:** ['ADV_TXT:p088:c03', 'ADV_TXT:p088:c04']
- **Citation Details:** [{"id": "ADV_TXT:p088:c03", "modality": "text", "label": "Section 3: Long-Term Futures (p.72)", "pdf_page": 88, "printed_page": "72", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}, {"id": "ADV_TXT:p088:c04", "modality": "text", "label": "Section 3: Long-Term Futures (p.72)", "pdf_page": 88, "printed_page": "72", "bbox": [35.0, 35.0, 575.0, 760.0], "crop_relpath": null}]
- **Inspected Crops:** []

## adv_dev_18 [unanswerable] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** What were the observed global net anthropogenic greenhouse gas (GHG) emissions (in GtCO2-eq) reported for the years 2022 and 2023 in the IPCC AR6 Synthesis Report?
- **Expected Behavior:** Abstain — The AR6 Synthesis Report's observed historical global GHG emissions inventory ends in 2019 (59 GtCO2-eq) and does not report observed global emissions for 2022 or 2023.
- **Agent Answer:** The IPCC AR6 Synthesis Report does not report observed global net anthropogenic greenhouse gas (GHG) emissions for the years 2022 and 2023. The report assesses historical observed global net anthropogenic GHG emissions up to the year 2019 (reported as 59 ± 6.6 GtCO2-eq in 2019). Observed emissions data for 2022 and 2023 are not contained or quantified in the report.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []

## adv_dev_19 [unanswerable] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** In Figure SPM.7 / Figure 4.4 panel (a), what is the assessed mitigation synergy level (High, Medium, or Low) and confidence rating for 'Coastal defence and hardening', and what numerical net lifetime cost bracket (in USD per tCO2-eq) is allocated to 'Electric vehicles'?
- **Expected Behavior:** Abstain — In Figure SPM.7/4.4a, synergies with mitigation for 'Coastal defence and hardening' are explicitly marked 'not assessed', and 'Electric vehicles' is grey ('Cost not allocated due to high variability or lack of data').
- **Agent Answer:** The retrieved text and figure excerpts do not provide sufficient evidence to determine the assessed mitigation synergy level and confidence rating for 'Coastal defence and hardening', nor the specific numerical net lifetime cost bracket (in USD per tCO2-eq) allocated to 'Electric vehicles' in Figure SPM.7 / Figure 4.4. Visual inspection of the corresponding figure panels and tables was not completed before the search tool budget was exhausted.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []

## adv_dev_20 [unanswerable] — `status=abstain` | `searches=5` | `inspects=0` | `err=None`
- **Question:** How much financial compensation was pledged to the Loss and Damage Fund established at COP27 in Sharm el-Sheikh, according to Section 4.8 of the IPCC AR6 Synthesis Report?
- **Expected Behavior:** Abstain — COP27, Sharm el-Sheikh, and the COP27 Loss and Damage Fund do not appear anywhere in the 186-page IPCC AR6 Synthesis Report.
- **Agent Answer:** The IPCC AR6 Synthesis Report (including Section 4.8) does not contain information about or quantify any financial compensation pledged to a Loss and Damage Fund established at COP27 in Sharm el-Sheikh.
- **Citations:** []
- **Citation Details:** []
- **Inspected Crops:** []
