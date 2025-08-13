#
## **CoCliCo SpatioTemporal Asset Catalog**

The CoCliCo platform offers structured access to datasets on coastal climate risks, sea level rise, extreme weather events, and adaptation strategies. These datasets are managed within a [SpatioTemporal Asset Catalog (STAC)](https://radiantearth.github.io/stac-browser/#/external/storage.googleapis.com/coclico-data-public/coclico/coclico-stac-4oct/catalog.json), facilitating efficient search and retrieval of geospatial data.

CoCliCo leverages STAC to provide structured access to geospatial datasets. The table below outlines key dataset categories available in the platform.

| **Category**                     | **Description**                                                                                       |
|----------------------------------|-------------------------------------------------------------------------------------------------------|
| **Sea Level Rise Projections**   | Regional and global sea level rise forecasts based on AR5 & AR6 climate models, including high-end scenarios. |
| **Flood and Surge Risk Assessments** | Storm surge levels, flood extents, expected damages, and total water levels under RCP4.5 & RCP8.5 scenarios. |
| **Coastal Vulnerability Data**   | Erosion risk classifications, asset mapping, infrastructure exposure, and coastal hazard projections. |
| **Shoreline Dynamics**           | Long-term shoreline evolution, coastal transects, and future shoreline change predictions.            |
| **Wave and Surge Climate Data**  | Storm surge projections, wave energy flux, and total water level estimates for coastal target points.  |
| **Adaptation Cost-Benefit Analyses** | Cost-benefit analyses of raising coastal defenses at the NUTS2 level under different climate and socio-economic scenarios. |
| **Population & Infrastructure Projections** | SSP-based population growth, critical infrastructure mapping, and building footprints.                |
| **Coastal Geomorphology**        | Global coastal digital terrain models (DeltaDTM) and shoreline morphodynamics.                        |
| **Administrative and Statistical Units** | Local administrative units (LAUs), NUTS regions, and flood statistics aggregated by administrative boundaries. |


---

## **Data Layers in the CoCliCo platform**

In the CoCliCo Platform, each data layer is the result of modeling and transforming various datasets from the STAC (SpatioTemporal Asset Catalog) to generate the final geospatial data layers. The platform is organized into five main categories: Sea Levels, Natural Hazards, Exposure and Vulnerability, Risk and Adaptation, and Background Layers, each containing its own specific data layers. Keep reading to discover which datasets are used to create the data layers in the platform.

---

## **Sea Levels**


The **CoCliCo Platform** provides access to **sea-level rise (SLR) projections** based on the latest scientific assessments from the **Intergovernmental Panel on Climate Change (IPCC) Sixth Assessment Report (AR6)**. These projections are essential for understanding how sea levels may change in the future and for planning coastal adaptation strategies. The platform focuses on **AR6-based projections**, which are considered the most up-to-date and comprehensive estimates of future sea-level rise.

---

### **Sea Level Rise Projections**

**1. Scenarios**

The platform offers sea-level rise projections for three **Shared Socioeconomic Pathways (SSPs)** and a **high-end scenario**:

| Scenario       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **SSP1-2.6**   | A low-emission scenario where global temperatures are limited to 1.5°C above pre-industrial levels, reflecting a sustainable future with rapid decarbonization. |
| **SSP2-4.5**   | A medium-emission scenario where global temperatures rise moderately, reflecting a future with some efforts to mitigate climate change. |
| **SSP5-8.5**   | A high-emission scenario where global temperatures rise significantly, reflecting a future with continued high greenhouse gas emissions and limited mitigation efforts. |
| **High-End**   | Represents more extreme but plausible outcomes of sea-level rise, useful for risk assessment and worst-case planning. |

---

**2. Ensembles**

The projections are provided in three **ensemble ranges** to reflect the uncertainty in future sea-level rise:

| Ensemble       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **MSL_h**      | Represents the **upper range** of projected sea-level rise, reflecting higher uncertainty and more extreme outcomes. |
| **MSL_m**      | Represents the **median projection** of sea-level rise, based on the central estimates from the IPCC AR6. |
| **MSL_l**      | Represents the **lower range** of projected sea-level rise, reflecting more optimistic outcomes with lower uncertainty. |

---

**3. Time Horizon**

The projections are available for **decadal time steps** from **2031 to 2151**, allowing users to explore how sea levels may change over the coming decades and into the next century.

| Time Period    | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **2031–2151**  | Projections are provided for every decade (e.g., 2031, 2041, 2051, etc.), enabling long-term planning. |

---

**4. Regional and Global Coverage**

The projections are provided at both **regional** and **global scales**:

- **Regional Scale**: Users can explore how sea-level rise may vary across different parts of the world, accounting for local factors such as land subsidence, ocean currents, and glacial isostatic adjustment.
- **Global Scale**: The platform also provides **global mean sea-level (GMSL) projections**, which represent the average rise in sea levels worldwide.

---

**5. Baseline Period**

All projections are relative to a **1995–2014 baseline period**, consistent with the IPCC AR6 methodology. This baseline provides a common reference point for comparing future sea-level rise scenarios.

---

#### How to Use the Sea Level Rise Projections

1. **Scenario Selection**: Choose from the available scenarios (SSP1-2.6, SSP2-4.5, SSP5-8.5, and high-end) to explore different future pathways of sea-level rise.
2. **Ensemble Selection**: Select between the high (MSL_h), median (MSL_m), and low (MSL_l) ensembles to understand the range of possible outcomes.
3. **Time Horizon**: View projections for specific decades (e.g., 2031, 2041, 2051, etc.) to assess how sea levels may change over time.
4. **Regional Analysis**: Zoom in on specific regions to see how sea-level rise may impact local coastlines.

---

#### Why Are These Projections Important?

- **Coastal Risk Assessment**: The sea-level rise projections are critical for assessing the risks of coastal flooding, erosion, and other hazards. They help identify areas that may be most vulnerable to future sea-level rise.
- **Adaptation Planning**: By understanding how sea levels may change in the future, coastal planners and policymakers can develop strategies to protect communities, infrastructure, and ecosystems.
- **Scientific Consistency**: The projections are based on the latest IPCC AR6 report, ensuring that users have access to the most reliable and up-to-date scientific information.

---

### **Extreme Surge Level**

The **Extreme Surge Level (SSL) data layer** provides projections of storm surge levels along the European coastline under different climate scenarios. Storm surges are a critical component of coastal hazards, and understanding how they may evolve in the future is essential for coastal risk assessment and adaptation planning. This dataset is part of the **LISCOAST project** and is based on hydrodynamic modeling and climate projections.


**Key Features of the Extreme Surge Level Data**

**1. Climate Scenarios**

The dataset includes projections for three climate scenarios:

| Scenario       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Historical** | Represents the baseline period (1970–2000) for validating the model.        |
| **RCP4.5**     | A medium-emission scenario where global temperatures rise moderately.       |
| **RCP8.5**     | A high-emission scenario where global temperatures rise significantly.      |

---

**2. Return Periods**

The dataset provides SSL estimates for **eight return periods**, which represent the frequency of extreme events:

| Return Period (Years) | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **5**                 | Events expected to occur once every 5 years.                               |
| **10**                | Events expected to occur once every 10 years.                              |
| **20**                | Events expected to occur once every 20 years.                              |
| **50**                | Events expected to occur once every 50 years.                              |
| **100**               | Events expected to occur once every 100 years.                             |
| **200**               | Events expected to occur once every 200 years.                             |
| **500**               | Events expected to occur once every 500 years.                             |
| **1000**              | Events expected to occur once every 1000 years.                            |

---

**3. Geographic Coverage**
The dataset covers the **European coastline**, with detailed projections for:

- **Northern Europe**: Areas north of 50°N, where significant increases in SSL are projected, especially under RCP8.5.
- **Southern Europe**: Areas south of 50°N, where minimal changes or small decreases in SSL are projected, except under RCP8.5 towards the end of the century.

---

**4. Methodology**
The SSL projections are based on:

- **Hydrodynamic Modeling**: The **Delft3D-Flow** model was used to simulate storm surge dynamics.
- **Climate Forcing**: The model was forced by surface wind and atmospheric pressure fields from an **8-member climate model ensemble**.
- **Validation**: The model was validated using data from **110 tidal gauge stations** across Europe, showing good predictive skill (RMSE: 0.06 m to 0.29 m).
- **Extreme Value Analysis**: The **Peak-Over-Threshold (POT) method** was applied to estimate SSL values for different return periods.

---

#### How to Use the Extreme Surge Level Data

1. **Scenario Selection**: Choose from the available scenarios (Historical, RCP4.5, RCP8.5) to explore how storm surge levels may change under different climate futures.
2. **Return Period Selection**: Select a return period (e.g., 5, 10, 20, 50, 100, 200, 500, or 1000 years) to assess the frequency and magnitude of extreme storm surge events.
3. **Geographic Analysis**: Zoom in on specific regions (e.g., Northern or Southern Europe) to see how storm surge levels may vary across the coastline.

---

#### Why Is This Data Important?

- **Coastal Risk Assessment**: The SSL data is critical for assessing the risks of coastal flooding and erosion, especially in areas prone to extreme storm surges.
- **Adaptation Planning**: By understanding how storm surge levels may change in the future, coastal planners and policymakers can develop strategies to protect communities, infrastructure, and ecosystems.
- **Combined Effects**: The dataset highlights the combined effects of **relative sea-level rise (RSLR)** and **storm surge levels**, which can significantly increase coastal hazards, particularly under high-emission scenarios like RCP8.5.

### **Extreme Sea Level**

The **Extreme Sea Level (ESL) data layer** provides projections of total water levels (TWL) along European coastlines under climate change. This dataset combines **mean sea level rise**, **tides**, **storm surges**, and **wave heights** to assess future coastal flood risks. It is part of the **LISCOAST project** and is critical for understanding how climate change will impact coastal hazards.

---

**Key Features of the Extreme Sea Level Data**

**1. Climate Scenarios**
The dataset includes projections for two climate scenarios:

| Scenario       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **RCP4.5**     | Medium-emission scenario with moderate warming.                            |
| **RCP8.5**     | High-emission scenario with significant warming.                           |

---

**2. Return Periods**
The dataset estimates extreme sea levels for **eight return periods**, representing the frequency of extreme events:

| Return Period (Years) | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **5**                 | Events expected once every 5 years.                                        |
| **10**                | Events expected once every 10 years.                                       |
| **20**                | Events expected once every 20 years.                                       |
| **50**                | Events expected once every 50 years.                                       |
| **100**               | Events expected once every 100 years.                                      |
| **200**               | Events expected once every 200 years.                                      |
| **500**               | Events expected once every 500 years.                                      |
| **1000**              | Events expected once every 1000 years.                                     |

---

**3. Components of Extreme Sea Levels**

**- Total Water Level (TWL)**: Combines mean sea level (MSL), tides, storm surges, and wave setup.

**- Episodic Extreme Water Level (EEWL)**: Includes extreme storm surge levels and wave heights during episodic events (e.g., storms).

---

**4. Geographic Coverage**
The dataset covers **Europe’s coastline**, with regional projections highlighting:
- **North Sea**: Highest projected increase in ESLs (up to 1 m under RCP8.5 by 2100).
- **Baltic Sea & UK/Ireland Atlantic Coasts**: Significant increases in ESLs.
- **Southern Europe**: Stable or decreasing extremes, except for Portugal and the Gulf of Cadiz.

---

#### How to Use the Extreme Sea Level Data

1. **Scenario Selection**: Choose between **RCP4.5** (moderate warming) and **RCP8.5** (high warming) to explore future risks.
2. **Return Period Selection**: Select a return period (e.g., 100-year event) to assess the magnitude and frequency of extreme sea levels.
3. **Regional Analysis**: Focus on specific regions (e.g., North Sea, Southern Europe) to understand local impacts.

---

#### Why Is This Data Important?

- **Coastal Flood Risk**: ESL projections help identify areas most vulnerable to flooding, particularly under high-emission scenarios.
- **Adaptation Planning**: Supports decision-making for coastal defenses, land-use planning, and emergency preparedness.
- **Combined Effects**: Highlights how **relative sea level rise (RSLR)**, storm surges, and waves interact to amplify risks.

---

---

## **Natural Hazards**

### Inundation Distribution During Flood Events

The **Inundation Distribution During Flood Events** data layer provides flood extent projections under various scenarios, including different coastal defense levels, return periods, and future climate conditions. These projections are essential for understanding the impact of extreme coastal flooding and aiding in risk assessment and adaptation planning.

#### Flood Mapping Methods

This dataset is generated using advanced flood modeling techniques:

- **Two-dimensional inundation models**: More realistic than simple bathtub methods, as they account for flood defense failure and wave propagation.
- **2D hydraulic storage-cell models**: Used at the pan-European scale, incorporating projected total water levels, land use-based roughness, and multiple flood sources.
- **Bathtub method**: Applied as an initial assessment tool, though it may overestimate flood extent.
- **Hydrodynamic modeling**: Acknowledged for its accuracy but not widely applied due to computational constraints.

**Consideration of Defenses and Scenarios**

- **Coastal defenses**: Both natural (e.g., dunes) and artificial (e.g., dikes) structures are considered.
- **Failure mechanisms**: Flood maps account for defense failures due to overtopping, overflow, and breaching.

**Protection Levels:**

- **High Defended**: Areas with robust, well-maintained protection.
- **Low Defended**: Areas with some protection but vulnerable to failure.
- **Undefended**: Areas without significant coastal protection.

**Future Scenarios:**

Projections include present-day (2020) and future conditions (2050, 2100) under different climate models:

- **SSP126**
- **SSP245**
- **SSP585**

**Flood Drivers:**

- **High tides**
- **Frequent storms**
- **Extreme “perfect storm” scenarios**
- **Erosion**: The compounded impact of coastal erosion and flooding is considered.

#### How to Use the Data

**Filtering the Data**

Users can filter the inundation distribution dataset based on:

- **Defense level**: High, low, or no protection.
- **Return periods**: 1-year, 100-year, 1000-year events.
- **Scenarios**: Climate projections under different Shared Socioeconomic Pathways (SSP126, SSP245, SSP585, High-End).
- **Timeframes**: Available for 2010, 2030, 2050, 2100, and 2150.

**Data Format and Access**

- The flood extent maps are provided as **GeoTIFF (.tif) files**.
- These can be visualized using **Geographic Information Systems (GIS)** such as QGIS or ArcGIS.
- Layers are structured under folders corresponding to defense level, return period, scenario, and time (e.g., `HIGH_DEFENDED_MAPS/SLR/SSP585/2050.tif`).

**Integration with Other Datasets**

- The dataset can be combined with **Digital Elevation Models (DEMs)** and **bathymetric data** for enhanced analysis.
- It aligns with **coastal typology classifications**, enabling better decision-making for flood management.

#### Why Is This Data Important?

The **Inundation Distribution During Flood Events** dataset is crucial for coastal risk assessment and adaptation planning by:

- **Supporting flood risk management**: Helps identify vulnerable areas and evaluate different protection strategies.
- **Informing coastal adaptation**: Aids in designing climate-resilient infrastructure and nature-based solutions.
- **Enhancing emergency preparedness**: Allows authorities to plan for extreme events and mitigate disaster impacts.
- **Improving scientific research**: Provides a consistent, large-scale dataset for studying climate change effects on coastal flooding.
- **Assisting policymakers**: Supports data-driven decision-making for long-term coastal management.

By leveraging this dataset, stakeholders can enhance **coastal resilience**, optimize **flood defense investments**, and safeguard **communities from future climate-induced flooding**.


### **Shoreline Change**

**Understanding Shoreline Change**

The **Shoreline Change** dataset provides projections of global shoreline evolution under climate change. This assessment considers the combined effects of:

- **Ambient change**: Historical shoreline trends.
- **Sea level rise (SLR)**: Based on RCP4.5 and RCP8.5 climate scenarios.
- **Storm-driven erosion**: Instantaneous shoreline changes due to extreme events.

Data is computed for seven statistical ensembles (1st, 5th, 17th, 50th, 83rd, 95th, and 99th percentiles) at two key timeframes: **2050 and 2100**. The projections stem from the **LISCOAST project**, a comprehensive study of coastal dynamics under climate change.

#### **How to Use the Data**

Users can filter the dataset based on:

- **Climate scenarios**: RCP4.5 (moderate emissions) and RCP8.5 (high emissions).
- **Statistical ensembles**: Different confidence levels (e.g., 1st percentile for extreme retreat, 99th for conservative estimates).
- **Timeframes**: Future projections for **2050 and 2100**.

Each dataset is structured as follows:

```text
sc-mapbox-ensemble-{ENSEMBLE}-scenarios-RCP{SCENARIO}
```

For example:

- `sc-mapbox-ensemble-50-scenarios-RCP85` → Median shoreline change under RCP8.5.
- `sc-mapbox-ensemble-99-scenarios-RCP45` → Extreme retreat case under RCP4.5.

These datasets can be integrated into GIS platforms to analyze shoreline retreat risks and assess adaptation strategies.

#### **Why Is This Data Important?**

The **Shoreline Change** dataset is critical for:

- **Coastal risk management**: Identifying areas vulnerable to erosion and planning protective measures.
- **Infrastructure planning**: Supporting long-term decision-making for sustainable coastal development.
- **Climate adaptation**: Evaluating potential impacts of sea level rise and storm events.
- **Scientific research**: Providing a robust dataset for studying coastal responses to climate change.

By leveraging this dataset, stakeholders can develop data-driven strategies to **enhance coastal resilience and mitigate climate-induced shoreline retreat**.

## Exposure and Vulnerability

While dedicated layers for exposure and vulnerability are still in development, CoCliCo combines **land-use data** from **Copernicus Coastal Zones 2018** with **Digital Terrain Models (DTMs)** to estimate exposure levels.

Future improvements will include datasets on **critical infrastructure assets** and **population exposure scenarios** for better risk evaluation.

---

## Risk and Adaptation

### Cost-Benefit Analysis of Coastal Adaptation

The **Cost-Benefit Analysis (CBA) of Coastal Adaptation per Floodplain** dataset provides insights into efficient coastal adaptation pathways along the European coastline. It evaluates different adaptation strategies based on a dynamic, inter-temporal cost-benefit analysis. The dataset includes projections up to the years **2050, 2100, and 2150**, offering key metrics to inform decision-making for coastal resilience.

**Adaptation Strategies Considered:**
- **Protection** – Raising coastal defenses.
- **Retreat** – Managed withdrawal from vulnerable areas.
- **Accommodation** – Implementing flood-proofing measures.
- **Protection & Retreat** – A combined strategy where both approaches are efficient.
- **No Adaptation** – Areas where adaptation measures are deemed inefficient.

The analysis accounts for adaptation costs, residual flood damages, and the most cost-efficient adaptation strategies for each floodplain.

---

#### **How to Use the Data**

This dataset is structured to support **policymakers, coastal managers, and researchers** in evaluating adaptation strategies at multiple spatial and temporal scales. The data is organized under three primary filters:

**Filters:**

**Adaptation Strategy:**
- Protection
- Retreat
- Accommodation
- Protection & Retreat
- No Adaptation

**Climate & Socioeconomic Scenarios:**
- **SSP126** (Sustainability Pathway)
- **SSP245** (Middle of the Road Pathway)
- **SSP585** (Fossil-Fueled Development Pathway)

**Time Periods:**
- 2050
- 2100
- 2150

**Dataset Variables:**

**Floodplain-Specific Data:**
- Efficient protection height *(m)*
- Return period of protection level
- Retreat height triggering full retreat
- Accommodation feasibility *(binary indicator)*
- Adaptation costs *(€)* & residual flood damages *(€)*

**Country-Level Aggregates:**
- Percentage of coastline where each adaptation strategy is efficient
- Total adaptation and damage costs over time

---

#### **Why Is This Data Important?**

This dataset is crucial for guiding **cost-effective and sustainable coastal adaptation strategies** under different climate change and socioeconomic scenarios. It helps:

- **Coastal decision-makers** initiate proactive adaptation planning.
- **Global institutions** estimate future adaptation costs at regional and national scales.
- **Researchers and policymakers** assess the effectiveness of adaptation pathways over time.

By leveraging this data, stakeholders can make **informed decisions** to mitigate flood risks while optimizing economic investments in coastal adaptation strategies.

---

<div align="center">
    <img src="../assets/logo1.png" width="150" alt="CoCliCo Logo">
    <p><small>Copyright &copy; 2025 CoCliCo Services</small></p>
</div>