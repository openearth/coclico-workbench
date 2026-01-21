# **Key Layers, Sources, and How to Interpret Them**


## **Data Layers in the CoCliCo platform**

In the CoCliCo Platform, each data layer is the result of modeling and transforming various datasets from the STAC (SpatioTemporal Asset Catalog) to generate the final geospatial data layers. The platform is organized into five main categories: Sea Levels, Natural Hazards, Exposure and Vulnerability, Risk and Adaptation, and Background Layers, each containing its own specific data layers. Keep reading to discover which datasets are used to create the data layers in the platform.

---

## **User Stories**

User Stories are ready-made map datasets in the CoCliCo platform. They combine different types of important information to show scenarios for coastal risk resulting from sea-level rise,  floods and / or erosion. These layers make complex analyses easier and help users to quickly get a sense of coastal risks.

User research showed that policymakers need clear, actionable data for flood directives, while urban planners want tools to assess local risks, and where infrastructure managers focus on long-term resilience planning. These insights helped shape User Stories to provide accessible, scenario-driven visualizations for diverse decision-making needs. There are five User Stories:

1. Flood Perspectives
2. People Exposure
3. Building Exposure
4. Cost Benefit Analysis
5. Damage Costs

---

## **Sea Levels**



???+  "Data Layers & User Stories"

    === "Sea Level Rise Projections"


        The **CoCliCo Platform** provides access to **sea-level rise (SLR) projections** based on the latest scientific assessments from the **Intergovernmental Panel on Climate Change (IPCC) Sixth Assessment Report (AR6)**, essential for understanding future changes and planning coastal adaptation.

        Use the **Sea Level Rise Projections User Story** for detailed insights into how sea levels may change under different climate scenarios. With projections ranging from 0.3 to 1 meter by 2100—and continuing to rise—this data is crucial for assessing coastal flood risks, infrastructure planning, and long-term adaptation.

        Unlike global estimates, these regional projections account for local factors like ocean circulation, ice melt, and land shifts, offering more precise insights for specific locations. This layer is a key foundation for flood models and supports all other User Stories in the platform.

        > *"I need to see mean sea-level rise information now and in the future for different climate change scenarios, so I can do a broad-scale preliminary evaluation of risks.”*

        ---

        **Data Sources**

        CoCliCo's regional sea-level projections are based on the IPCC AR6 dataset, incorporating all sea-level components except vertical land motions, which are corrected using GIA model outputs for improved regional accuracy.

        - IPCC AR6 (Fox-Kemper et al., 2021)
        - AR6 dataset is described and displayed at [Sea Level Projection Tool – NASA Sea Level Change Portal](https://sealevel.nasa.gov/ipcc-ar6-sea-level-projection-tool) and is publicly distributed at [IPCC AR6 Sea Level Projections](https://zenodo.org/records/6382554) (Garner et al., 2022).
        - Glacial Isostatic Adjustment (GIA) model outputs (Caron et al., 2018)

        ![](./assets/Tool/SLR_DATA.png){ width=900 .center}

        ---

        **Methods**

        CoCliCo regional mean sea-level projections are constructed by combining the IPCC AR6 sea-level change dataset and the GIA model outputs of Caron et al. (2018), and propagating uncertainty following a Monte Carlo approach. The regional sea-level changes therefore include the changes in ocean density and circulation, the changes due to continental glaciers and ice-sheet mass loss and their respective regional spatial distribution, changes in land water and groundwater, and the post-glacial rebound.


        **Climate Scenarios**

        The platform offers sea-level rise projections for three **Shared Socioeconomic Pathways (SSPs)** and a **high-end scenario**:

        <div class="grid cards" markdown>

        - **SSP1-2.6**
        *A low-emission scenario where global temperatures are limited to 1.5°C above pre-industrial levels, reflecting a sustainable future with rapid decarbonization.*

        - **SSP2-4.5**
        *A medium-emission scenario where global temperatures rise moderately, reflecting a future with some efforts to mitigate climate change.*

        - **SSP5-8.5**
        *A high-emission scenario where global temperatures rise significantly, reflecting a future with continued high greenhouse gas emissions and limited mitigation efforts.*

        - **High-End**
        *Represents more extreme but plausible outcomes of sea-level rise, useful for risk assessment and worst-case planning.*

        </div>

        ---

        **Ensembles**

        The projections are provided in three **ensemble ranges** to reflect the uncertainty in future sea-level rise:

        - **MSL_h:** Represents the **upper range** of projected sea-level rise, reflecting higher uncertainty and more extreme outcomes.

        - **MSL_m:** Represents the **median projection** of sea-level rise, based on the central estimates from the IPCC AR6.

        - **MSL_l:** Represents the **lower range** of projected sea-level rise, reflecting more optimistic outcomes with lower uncertainty.


        ---

        **Time Horizon**

        The projections are available for **decadal time steps** from **2030 to 2150**, allowing users to explore how sea levels may change over the coming decades and into the next century.

        ---

        **Regional and Global Coverage**

        The projections are provided at both **regional** and **global scales**:

        - **Regional Scale**: Users can explore how sea-level rise may vary across different parts of the world, accounting for local factors such as land subsidence, ocean currents, and glacial isostatic adjustment.
        - **Global Scale**: The platform also provides **global mean sea-level (GMSL) projections**, which represent the average rise in sea levels worldwide.

        ---

        **Baseline Period**

        All projections are relative to a **1995–2014 baseline period**, consistent with the IPCC AR6 methodology. This baseline provides a common reference point for comparing future sea-level rise scenarios.

        ---

        **How to Use the Sea Level Rise Projections**

        - [x]  **Scenario Selection**: Choose from the available scenarios (SSP1-2.6, SSP2-4.5, SSP5-8.5, and high-end) to explore different future pathways of sea-level rise.
        - [x]  **Ensemble Selection**: Select between the high (MSL_h), median (MSL_m), and low (MSL_l) ensembles to understand the range of possible outcomes.
        - [x]  **Time Horizon**: View projections for specific decades (e.g., 2030, 2040, 2050, etc.) to assess how sea levels may change over time.
        - [x]  **Specific Analysis**: Zoom in on specific regions to see how sea-level rise may impact local coastlines.

        ---

        **Model Outputs**

        ![](./assets/Tool/SLR_outputs.jpg){ width=800 .center}

        ---

        **Why Are These Projections Important?**

        - [x] **Coastal Risk Assessment**: The sea-level rise projections are critical for assessing the risks of coastal flooding, erosion, and other hazards. They help identify areas that may be most vulnerable to future sea-level rise.
        - [x] **Adaptation Planning**: By understanding how sea levels may change in the future, coastal planners and policymakers can develop strategies to protect communities, infrastructure, and ecosystems.
        - [x] **Scientific Consistency**: The projections are based on the latest IPCC AR6 report, ensuring that users have access to the most reliable and up-to-date scientific information.

        ---

        **Example of use**

        > *"Using the Sea Level Rise projections User Stories, city planners identified their neighbourhoods as having a higher risk of permanent flooding related to sea level rise by 2050 under high-emission scenarios high-emission scenarios compared to other neighbourhoods in the country. This analysis informed their decisions to prioritize green infrastructure development in those areas, reducing potential damage costs by 30%."*

        ---

        **Limitations**

        Limitations are twofold: first, vertical ground motions unrelated to the glacial isostatic adjustment are not integrated. Yet CoCliCo’s research has shown that urban areas and populations located in coastal flood plains in Europe (excluding Fennoscandia) are affected by subsidence of approximately 1mm/year in average.

        Second, sea level projections shown here have a resolution of 1°x1°, therefore not taking into account mesoscale ocean processes acting on the continental shelf and within semi-enclosed bassins such as the Mediterranean. Research undertaken by CoCliCo by ENEA and Mercator Ocean (D3.3, soon to be published) suggest that the order of magnitude of the error due to neglecting these processes can reach +/-10cm in Europe.

        ---

        **Further Analysis**

        Beside GIA, coastal regions in Europe can experience significant vertical land motion (VLM) which can be strong, robust and that can be assessed locally. There is for instance well known subsidence along the Italian Adriatic, the Netherlands or even in more localized shorelines such as the Aksiou delta next to Thessaloniki in Greece. This subsidence context can strongly inflate coastal hazards locally and should therefore be accounted for. The CoCliCo project explored local VLMs using the land vertical velocity estimates from the Copernicus European Ground Motion Service (EGMS) derived over the period 2016-2021 (​​Thiéblemont et al., 2024). While these estimates are not implemented in the regional sea-level projections of CoCliCo, they have been considered for the coastal hazard assessment and can be explored as an exploratory tool using the [Workbench](further_analysis.md).



    === "Future Total Water Levels and Return Periods"

        The **Future Total Water Levels (TWL)** and **Total Water Level Return Periods** data layers estimate how high sea levels may rise during coastal storm events in the future. These projections combine several key components that influence water levels along the coast:

        - **Storm surge** (temporary rise in sea level caused by storms)
        - **Wave setup** (increase in water level due to breaking waves)
        - **Tidal range** (variation in sea level due to tides)
        - **Sea Level Rise** (long-term rise including vertical land motion, like subsidence)

        These layers provide insight into **how extreme total water levels will change over time**—for example, what might be considered a “1-in-100-year” flood today could occur more frequently in the future under climate change.

        > *“I need to know how high-total water levels could reach along my coast by 2050 or 2100 so I can set safe design levels for infrastructure like sea walls or power stations.”*

        **Data Sources**
        These datasets are based on a combination of:

        - **Numerical model simulations** for storm surge and wave climate
        - **Global tidal models assimilating satellite altimetry** (e.g. TPXO9) to compute the astronomical tide
        - **Sea-level rise projections** from IPCC-consistent scenarios

        **Methods**

        The data represent **extreme total water levels** at **coastal target points** along the European shoreline. They account for the combined effect of multiple flood drivers under different:

        - **Time horizons**: e.g., 2030, 2050, 2100
        - **Emission scenarios**: Shared Socioeconomic Pathways (SSP1-2.6, SSP5-8.5, etc.)

        <div class="grid cards" markdown>

        -   :octicons-check-16:{ .lg .middle } __Future Total Water Levels Layer__

            ---

            This dataset provides the **total water level values** expected at each coastal point for a given return period, for different scenarios and time horizons. These values represent plausible **design levels** for planning and infrastructure.

        -   :octicons-check-16:{ .lg .middle } __Return Periods Layer__

            ---

            This dataset provides the **total water level values** expected at each coastal point for a given scenario and time horizon, for different return periods, such as: **1-in-10 years, 1-in-50 years, and 1-in-100 years.**

            These show how often such total water levels might be expected in the future, allowing for better risk assessment and planning.



        </div>

        **Climate Scenarios**

        The dataset includes projections for three climate scenarios:
        <div class="grid cards" markdown>

        - **Historical**
        *Represents the baseline period (1970–2000) for validating the model.*

        - **RCP4.5**
        *A medium-emission scenario where global temperatures rise moderately.*

        - **RCP8.5**
        *A high-emission scenario where global temperatures rise significantly.*


        </div>

        ---

        **Geographic Coverage**

        - Entire **European coastline**, including EU countries and the UK
        - Coastal **target points** represent strategic sampling locations for local flood modelling

        ---

        **How to Use the Future Total Water Levels and Return Periods Data**

        - [x] **Design coastal infrastructure**: Use future TWL data to set minimum elevation or structural thresholds for sea defences, ports, and buildings
        - [x] **Inform flood hazard mapping**: Identify which coastal areas are most at risk under future sea level and storm conditions
        - [x] **Set emergency thresholds**: Prepare response plans based on likely flood heights in future storms
        - [x] **Support long-term adaptation**: Evaluate how flood risk will evolve under different emissions scenarios and timeframes
        - [x] **Use return periods for planning**: Determine how often extreme flood levels may occur in the future to inform building codes or insurance strategies

        ---

        **Model Outputs**

        ![](./assets/Tool/FUTURE TWL.png){ width=900 .center}

        ---

        **Why Is This Data Important?**

        These layers support **evidence-based adaptation planning** by providing clear, localized estimates of **how sea levels and storm-driven floods will change** over time. They are crucial for:

        - [x] **Avoiding under-designing infrastructure** in future high-risk zones
        - [x] **Comparing today’s flood risks with future conditions**
        - [x] **Understanding how different climate pathways (e.g. low vs high emissions) will impact coastal flood hazards**

        ---

        **Example of use**

        > *“A regional planner working on the future of a coastal city used the Total Water Levels Return Period dataset to identify that the city’s current flood defence—designed for a 1-in-100-year event—will be overtopped more frequently by 2100 under high emissions. This helped secure funding for upgrades, ensuring the city remains protected against more frequent and intense flooding.”*

        ---

        **Further Analysis**
        The values provided here correspond to the best fit. However, it is also important to consider the uncertainty associated with extreme-value modeling when interpreting return levels. For further discussion of this issue, more details can be found in Cotrim et al., 2025.



    === "Drivers of Total Water Level"

        The *Drivers of Future Total Water Levels* data layer decomposes the contributing components of extreme coastal water levels under future climate scenarios. It shows **representative statistics** of individual physical drivers—**storm surge, wave height, tidal range, and sea-level rise (SLR)**—to the projected *Total Water Level (TWL)* at specific coastal locations.

        Understanding the *relative influence* of each driver helps identify which processes dominate flood risk in different regions and informs targeted adaptation measures.

        > *“I want to understand whether sea-level rise or storm surges will be the dominant factor increasing flood risk in my region by 2100, to design more effective coastal defences.”*

        ---

        **Data Sources**

        This dataset is derived from:

        - **Numerical model simulations** for storm surge and wave climate
        - **Global tidal models assimilating satellite altimetry** (e.g. TPXO9) to compute the astronomical tide
        - **Sea-level rise projections** from IPCC-consistent scenarios

        Each component is statistically analysed and summarised at key coastal points across Europe.

        ---

        **Methods**

        The data represent relevant statistics of each TWL driver, summarised at coastal "target points". For each point, the following indicators are provided:

        - ** Mean significant wave height (Hs)** – captures wave climate mean conditions
        - ** 99th percentile of storm surge level** – represents extreme storm surge events
        - ** 50th percentile of sea-level rise (SLR)** – median projection of SLR
        - ** Mean tidal range** – average difference between high and low tide

        These are estimated under future scenarios and time periods (e.g., 2050, 2100), allowing a component-by-component comparison of influence across Europe’s coastline.

        ---

        **Geographic Coverage**
        The dataset covers **coastal target points** along the **entire European coastline**, including EU countries and the United Kingdom. Each point represents a coastal segment with distinct hydrodynamic conditions.

        ---

        **How to Use the Extreme Sea Level Data**

        - [x] **Assess Local Drivers**: Identify whether storm surge, waves, tides, or sea-level rise contribute most to future flood risk in a specific area
        - [x] **Compare Regions**: Understand geographic variability in TWL drivers to support regional adaptation planning
        - [x] **Model Inputs**: Use component values to inform flood models or hybrid hazard simulations
        - [x] **Design Criteria**: Tailor flood protection designs based on the dominant local driver (e.g., wave-dominated vs surge-dominated coasts)
        - [x] **Support Stakeholder Dialogue**: Communicate clearly why specific interventions (e.g., breakwaters vs dikes) are necessary in different areas

        ---

        **Model Outputs**

        ![](./assets/Tool/DRIVERS TWL.png){ width=900 .center}

        ---

        **Why Is This Data Important?**

        While total future flood levels are essential for risk planning, knowing *which processes drive those levels* is equally critical. This data layer:

        - [x] Enables **mechanistic understanding** of coastal hazards
        - [x] Supports **tailored adaptation solutions** based on local conditions
        - [x] Helps identify **coastal segments where sea-level rise may be the main future risk,** versus those where **storms or waves** dominate
        - [x] Provides inputs for **dynamic modelling and hybrid flood simulations** that consider interacting drivers

        ---

        **Example of use**

        > *“A coastal engineer working on adaptation planning for the Dutch coastline used the Drivers of TWL data to determine that in their region, future total water levels were increasingly dominated by tidal range and sea-level rise, while wave height and storm surge level remained constant. This informed a dual approach of reinforcing flood barriers and elevating critical infrastructure, with less emphasis on wave attenuation measures.”*

        ---

        **Further Analysis**

        The statistics provided here offer a broad view of the role played by the different components of the total water level. It is important to consider the possible contribution of extreme waves, storm surge events associated with other percentiles, and tidal variability. A more detailed analysis of the contributions of the different components to the TWL can be found in Cotrim et al., 2025.


---

## **Natural Hazards**



???+  "Data Layers & User Stories"

    === "Flood Perspectives"

        The **Inundation Distribution During Flood Events** User Story in the CoCliCo platform helps users understand and prepare for coastal flooding. They are essential for assessing vulnerability, informing risk management strategies, and supporting decision-making for coastal planning, infrastructure protection, and emergency preparedness. These maps show areas at risk of flooding due to rising sea levels, coastal storms, or both. They combine data on land elevation, water movement, and climate predictions to estimate how floods might impact different coastal areas in Europe. This collection of flood maps serves as the basis for other User Stories.

        > *"I need to see flood extent and depth maps for different relative sea-level rise and storm scenarios so I can assess coastal flood risks and identify vulnerable areas across Europe."*

        ---

        **Data Sources**

        To map flood risks across Europe, we used detailed topographic data to represent the land. This included a high-resolution (25-meter) digital elevation model (DEM) from Copernicus (2019), a defined coastline to set boundary conditions from the European Environment Agency (EEA, 2017), and land-use data from Witjes et al. (2022), which was translated into Manning’s roughness coefficients to estimate how water moves across different surfaces.

        To understand how ocean forces contribute to flooding, we analyzed water levels at 1 km intervals along the European coast using two approaches. For permanent flooding scenarios, we used data from the CoCliCo Regional Sea Level Rise (SLR) Projections. For temporary flood events, we used extreme total water level (TWL) scenarios based on a reconstructed TWL hindcast. This hindcast included tidal data from the TPXO database, storm surge simulations from the ROMS model (Shchepetkin & McWilliams, 2005), and wave setup estimates based on downscaled wave conditions modeled with WaveWatch III (Tolman, 2009).

        Finally, we incorporated data on coastal flood protection measures developed by Vrije Universiteit Amsterdam (van Maanen et al., 2024) to improve the accuracy of the flood maps, ensuring they reflect existing defenses along Europe’s coasts.

        ![](./assets/Tool/FLOOD_DATA.png){ width=900 .center}

        ---

        **Methods**

        The methodology for mapping coastal flood risks followed three main steps:

        <div class="grid cards" markdown style="grid-template-columns: 1fr;">

        -    __1. Defining the Coastal Floodplain__

            ---

            We identified flood-prone areas as coastal regions between 0 and 15 meters in elevation, hydraulically connected to the sea. These areas were divided into 22 flood units, each with detailed topographic meshes. The meshes consisted of irregular impact zones that followed natural terrain features, with smaller 25-meter impact cells (based on the DEM). Each impact zone was assigned a Manning roughness coefficient based on dominant land use.

        -   __2. Constructing Flood Scenarios__

            ---

            For permanent flooding, hydrographs were created by combining sea level rise (SLR) projections with the mean spring high tide at each location. For episodic flooding, hydrographs were based on extreme total water level (TWL) analysis and storm duration estimates. The TWL hindcast was reconstructed by summing:

            - Astronomical tide (TPXO database)

            - Storm surge (ROMS model)

            - Wave setup (Stockdon et al., 2006; foreshore slopes from Sunamura, 1984)

            The peak over threshold (POT) method was used to identify extreme TWL events, estimating return levels with an exponential model. Future flood scenarios combined relative SLR with TWL returns values.

        -   __3. Running Coastal Flood Simulations__

            ---

            We used the RFSM-EDA 2D flood model (Jamieson et al., 2012) for large-scale flood simulations, incorporating terrain details. The Saint-Venant equations were applied to compute water flow between impact zones, and flood depth was calculated for each 25-meter impact cell.

            Final flood maps showed depth and extent for different scenarios along the European coast. These maps were post-processed to account for existing coastal defences, considering policy-based protection levels at the provincial level (NUTS 2).

        </div>

        **Climate Scenarios**

        The dataset includes projections for three climate scenarios:

        <div class="grid cards" markdown>

        - **SSP1-2.6**
        *A low-emission scenario where global temperatures are limited to 1.5°C above pre-industrial levels, reflecting a sustainable future with rapid decarbonization.*

        - **SSP2-4.5**
        *A medium-emission scenario where global temperatures rise moderately, reflecting a future with some efforts to mitigate climate change.*

        - **SSP5-8.5**
        *A high-emission scenario where global temperatures rise significantly, reflecting a future with continued high greenhouse gas emissions and limited mitigation efforts.*

        </div>

        **Protection Levels:**

        <div class="grid cards" markdown>

        - **High Defended**
            Maximum level of policy-based protection at the NUTS2 level.


        - **Low Defended**
            Minimum level of policy-based protection at the NUTS2 level.

        - **Undefended**
            Without protection (beyond what may be included in the DEM).

        </div>


        **Flood Drivers:**

        - **High tides**
        - **Frequent storms**
        - **Extreme “perfect storm” scenario**

        ---

        **How to Use the Inundation Distribution During Flood Events Data**

        - [x] **Defense level**: Choose between high, low, or no protection.
        - [x] **Return Period Selection**: Select a return period (e.g., 100-year event) to assess the magnitude and frequency of the flood event.
        - [x] **Scenario Selection**: Choose between the different climate projections under different Shared Socioeconomic Pathways (SSP126, SSP245, SSP585, High-End).
        - [x] **Timeframe selection**: Available for 2010, 2030, 2050, 2100, and 2150.

        ---

        **Model Outputs**

        Flood maps showing the maximum flood extent and depth for different extreme scenarios (1-year, 100-year, and 1000-year return period TWL events), various relative SLR projections (decadal time steps from 2030 to 2150 relative to the reference period 1995–2014 for three SSP scenarios and one high-end scenario), and the combination of each extreme scenario with every sea level rise scenario.

        ![](./assets/Tool/flood_pers_output.png){ width=800 .center}

        ---

        **Why Is This Data Important?**

        The **Inundation Distribution During Flood Events** dataset is crucial for coastal risk assessment and adaptation planning by:

        - [x] **Supporting flood risk management**: Helps identify vulnerable areas and evaluate different protection strategies.
        - [x] **Informing coastal adaptation**: Aids in designing climate-resilient infrastructure and nature-based solutions.
        - [x] **Enhancing emergency preparedness**: Allows authorities to plan for extreme events and mitigate disaster impacts.
        - [x] **Improving scientific research**: Provides a consistent, large-scale dataset for studying climate change effects on coastal flooding.
        - [x] **Assisting policymakers**: Supports data-driven decision-making for long-term coastal management.

        ---

        **Example of use**

        > *Using the Coastal Flood Maps, a marine conservation group identified several critical wetland areas at risk of being flooded due to storms combined with relative sea-level rise. The group used the flood extent and depth maps for different scenarios to prioritize restoration projects. By focusing on these vulnerable areas, they were able to implement targeted conservation efforts that helped protect the wetlands, preserving biodiversity and improving water quality for the surrounding community.*

        ---

        **Limitations**

        The flood maps provided in the platform offer a robust and homogeneous distribution of flood extent and depth under different scenarios for the coast of Europe considering the spatial variability of its marine dynamics and floodplain characteristics. However, working with large-scale studies entails assumptions and simplifications in order to achieve a homogeneous analysis. As such, the resulting maps provided serve as guidance and should not be used for local-scale interventions and adaptation planning.

        The maps without defences (undefended maps) provide the upper limit of coastal flooding. The maps with defences (defended maps) provide the lower limit of coastal flooding. Importantly, defended maps should be treated with caution as they assume that the whole province is protected with the same level of protection.

        **Further Analysis**


    === "Flood Maps"

        The Flood Maps Data Layer provides clear, reliable visualizations of flood maps for identifying coastal areas at risk from flooding due to extreme weather events and sea-level rise. Besides risk identification and planning, the spatial distribution of coastal flooding projections is key to guide well-informed decisions and enhance community and stakeholder preparedness.

        > *"Example"*

        > *“I need to see maps of flood extent and depth for different sea-level rise and storm scenarios so I can assess coastal flood risks and identify vulnerable areas across Europe.”*

        **Data Sources**

        Topographic data used to represent the European floodplain terrain included a 25-m resolution digital elevation model (DEM) (Copernicus, 2019), the corresponding coastline used to define boundary conditions (EEA, 2017), and land-use information (Witjes et al., 2022), which was translated into Manning's roughness coefficients.

        Marine dynamic forcing conditions were obtained using two approaches for 1 km-spaced coastal points along the European coastline. For permanent inundation scenarios, input data were derived from the CoCliCo Regional Sea-Level Rise (SLR) Projections. For episodic flood events, input data were obtained from extreme total water level (TWL) return level scenarios based on a reconstructed TWL hindcast. This hindcast consisted of the astronomical tide from the latest version of the TPXO database, storm surge simulated using the ROMS model (Shchepetkin & McWilliams, 2005), and wave setup estimated from wave conditions in a downscaled wave hindcast generated with the WaveWatch III model (Tolman, 2009).

        Additionally, the dataset on protection standards around Europe’s coast developed by Vrije Universiteit Amsterdam was incorporated into the flood maps in a post-processing step (van Maanen et al., 2024).

        ## **Methods**

        The methodology followed can be divided into three steps:
        # European Coastal Flood Modelling Process

        ### (1) Definition of Floodplain and Meshes

        - The European floodplain was defined as **coastal regions located between 0 and 15 m elevation** that are hydraulically connected to the sea.
        - This floodplain was segmented into **22 flood units**, from which **topographic meshes** were generated.
        - Each mesh is composed of **irregular cells (impact zones)** containing **sub-element topography** (impact cells with 25 m resolution inherited from the DEM).
        - Impact zones:
        - Are flexible, following terrain features.
        - Boundaries adjust to topographic crests.
        - Each impact zone was assigned a **Manning roughness coefficient**, based on the majority land use present.

        ---

        ### (2) Hydrograph Construction

        **Permanent inundation scenarios**

        - Hydrographs were created by combining **sea-level rise (SLR)** with the **mean spring high tide** at each coastal point.

        **Episodic flooding scenarios**

        - Hydrographs were based on:
        - **TWL (Total Water Level) extreme value analysis**.
        - A **storm duration function** for TWL storms.
        - TWL hindcast reconstructed by summing:
        - Astronomical tide
        - Storm surge
        - Wave setup
        - Wave setup:
        - Computed using the semi-empirical formulation of **Stockdon et al. (2006)**.
        - Foreshore slopes estimated via **Sunamura (1984)**.

        **Extreme event detection**

        - **Peak Over Threshold (POT) method** applied to identify TWL extreme events.
        - Threshold chosen to yield ~**2 events per year**.
        - **Return values** of TWL estimated by fitting extremes to an **exponential model**.
        - **Storm durations** for return-period events estimated from individual POT events.

        **Combined scenarios**

        - Future episodic flooding scenarios were obtained by **superimposing relative SLR** onto hydrographs generated from TWL return values (hindcast period).

        ---

        ### (3) Coastal Flood Simulations

        - Simulations conducted with the **RFSM-EDA 2D flood model**.
        - RFSM-EDA:
        - Efficient hydraulic model for **large-scale, process-based flood modelling**.
        - Incorporates topography as a **sub-element of the computational mesh**.
        - References: *Sayers and Marti (2006); Jamieson et al. (2012)*.
        - During simulations:
        - **Saint-Venant equations** solved between impact zones.
        - Flood depth computed at each impact cell.
        - Output:
        - Flood maps showing **depth and extent** under different scenarios across the European coastline.
        - Post-processing:
        - Maps adjusted to reflect the effect of **coastal defences**.
        - Considered both **minimum and maximum policy-based return periods** at the **NUTS 2 (province) level**.

        ---

        **Defence Level**

        Process-based flood maps were post-processed to incorporate the effect of existing coastal defences. The dataset of protection standards used (van Maanen et al., 2024) provides estimates of the minimum and maximum policy-based return periods at the province level (NUTS 2). For each scenario, three flood maps were provided: one undefended map (without defences) and two defended maps (with defences). Defended maps represent the low- or high-defended cases depending on whether the minimum or maximum level of protection is assumed in each province.

        | Defence Level  | Description                                                                 |
        |----------------|-----------------------------------------------------------------------------|
        | Undefended     | Without protection (beyond what may be included in the DEM).                |
        | Low defended   | Maximum level of policy-based protection at the NUTS2 level                 |
        | High defended  | Minimum level of policy-based protection at the NUTS2 level                 |


        **Climate Scenarios**

        The dataset includes projections for three climate scenarios with different levels of confidence of sea-level rise projections and time horizons:

        | Shared Socioeconomic Pathways (SSP) | Description                                               | Time Horizons      | SLR Confidence |
        |-------------------------------------|-----------------------------------------------------------|--------------------|----------------|
        | SSP1-2.6                            | A low-emission scenario where global temperatures rise slightly | 2100               | Medium         |
        | SSP2-4.5                            | A medium-emission scenario where global temperatures rise moderately | 2050, 2100         | Medium, Medium |
        | SSP5-8.5                            | A high-emission scenario where global temperatures rise significantly | 2030, 2050, 2100   | Medium, Medium, Medium |
        | High-end                            | Represents high-end but plausible outcomes of sea-level rise under a high-emission scenario | 2100, 2150         | Low, Low       |


        **Return Periods**

        The dataset estimates extreme sea levels for three return periods, representing the frequency of extreme events:

        | Return Period (Years) | Description                                 |
        |------------------------|---------------------------------------------|
        | 1                      | Events expected once every 1 year.          |
        | 100                    | Events expected once every 100 years.       |
        | 1000                   | Events expected once every 1000 years.      |


        **Ensembles**

        Data is computed for seven statistical ensembles (1st, 5th, 17th, 50th, 83rd, 95th, and 99th percentiles) at two key timeframes: **2050 and 2100**. The projections stem from the **LISCOAST project**, a comprehensive study of coastal dynamics under climate change.


        **Components of Flood Maps**

        To estimate flood extent and depth under various scenarios for the entire coast of Europe, these maps integrate:

        - [x] Elevation data
        - [x] Manning roughness information inferred from land cover data
        - [x] Hydrodynamic simulations
        - [x] Climate information (hindcast and projections)

        ---

        **How to Use the Flood Maps Data**

        - [x] **Scenario selection**: select between return periods of extreme events of total water level (i.e., 1-yr, 100-yr, and 1000-yr), sea-level rise scenarios (i.e., SSP1-2.6, SSP2-4.5, SSP5-8.5, and high-end), or a combination of both.
        - [x] **Ensemble selection**: select between the high, median, and low ensembles to understand the range of possible sea-level rise outcomes.
        - [x] **Time horizon**: view flood maps for specific time slices (i.e, 2010, 2030, 2050, 2100, 2150).
        - [x] **Current coastal defence level considered in the flood maps**: undefended (no protection beyond which is included in the DEM), minimum level of protection, or maximum level of protection.

        ---

        **Model Outputs**

        Pan-European flood maps covering different scenarios with their respective flood extent and depth.

        ![](./assets/Tool/FLOOD_outputs.png){ width=800 .center}

        ---

        **Why Is This Data Important?**

        TThe Flood Maps Data Layer in the CoCliCo platform allow assessment of risks, informing management strategies, and supporting decision-making for coastal planning, infrastructure protection, and emergency preparedness. Coastal flood maps provide a visual representation of potential areas at risk from flooding due to sea-level rise, extreme coastal storms, or both.

        **Example of use**

        > *"Using the Coastal Flood Maps, a marine conservation group identified several critical wetland areas at risk of being inundated due to storm surges combined with sea-level rise. The group used the flood extent and depth maps for different scenarios to prioritize restoration projects. By focusing on these vulnerable areas, they were able to implement targeted conservation efforts that helped protect the wetlands, preserving biodiversity and improving water quality for the surrounding community.”*

        ---

        **Further Analysis**

        The Flood Maps Data Layer in the CoCliCo platform provide a library of process-based flood simulations for the integrated scenarios. In the Workbench, these maps can be integrated with exposure information and vulnerability curves to estimate risks.

        **References**

        Copernicus. (2019). DEM - Global and European Digital Elevation Model. https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing- missions/collections-description/COP-DEM.

        EEA, C. E. E. A. (2017). EEA coastline for analysis. https://sdi.eea.europa.eu/catalogue/srv/api/records/af40333f-9e94-4926-a4f0-0a787f1d2b8f.

        Jamieson S, L’homme J, Wright G, Gouldby B (2012) Highly efficient 2D inundation modelling with enhanced diffusion-wave and sub-element topography. Proc. Inst. Wat. Man., 165(10): 581–595.

        Sayers, P.B and Marti, (2006) RFSM - Rapid Flood Spreading Method - Initial Development. Developed as part of Floodsite and TE2100 by Marti and Sayers, HR Wallingford report for the Environment Agency.

        Shchepetkin, A. F., & McWilliams, J. C. (2005). The regional oceanic modeling system (ROMS): A split-explicit, free-surface, topography-following-coordinate oceanic model. Ocean Modelling, 9(4), 347–404. https://doi.org/10.1016/j.ocemod.2004.08.002

        Stockdon, H. F., Holman, R. A., Howd, P. A., & Sallenger Jr, A. H. (2006). Empirical parameterization of setup, swash, and runup. Coastal engineering, 53(7), 573-588.

        Sunamura, T. (1984). Quantitative predictions of beach-face slopes. Geological Society of America Bulletin, 95(2), 242-245.

        Tolman, H. L. (2009). User manual and system documentation of WAVEWATCH-IIITM version 3.14. Technical Note, 3.14, 220. http://polart.ncep.noaa.gov/mmab/papers/tn276/MMAB_276.pdf%5Cnpapers2://publication/u uid/298F36C7-957F-4D13-A6AB-ABE61B08BA6B

        van Maanen, N., De Plaen, J. J.-F. G., Tiggeloven, T., Colmenares, M. L., Ward, P. J., Scussolini, P., and Koks, E.: Brief Communication: Bridging the data gap – enhancing the representation of global coastal flood protection, Nat. Hazards Earth Syst. Sci. Discuss. [preprint], https://doi.org/10.5194/nhess-2024-137, in review, 2024.

        Witjes, M., Parente, L., van Diemen, C. J., Hengl, T., Landa, M., Brodský, L., Halounova, L., Križan, J., Antonić, L., Ilie, C. M., Craciunescu, V., Kilibarda, M., Antonijević, O., & Glušica, L. (2022). A spatiotemporal ensemble machine learning framework for generating land use/land cover time-series maps for Europe (2000-2019) based on LUCAS, CORINE and GLAD Landsat. PeerJ, 10. https://doi.org/10.7717/peerj.13573.


    === "Coastal Change Segments"

        Coastal erosion and flooding are known to be linked, with erosion potentially exacerbating flood extents and risk, but analysis of the combined hazards is limited. Coastal environments are characterised by various key factors including sediment supply, beach materials, underlying geology and human infrastructure and activity, which all influence the dynamic nature of the coastal zone.

        The ‘Coastal Typologies and Erosion for Risk’ (CoasTER) database integrates existing information on erosion and other relevant coastal characteristics for Europe’s coastal floodplains. In particular, coastal areas where mobile sediments and coastal floodplains are co-located identifying the areas where erosion and flooding are most likely to interact. It also includes a coastal geomorphological typology which incorporates the influence of human modification in the form of hard engineering and infrastructure.

        The **Coastal Change Segments** CoasTER database provides projections of global shoreline evolution under climate change. This assessment considers the combined effects of:

        - **Ambient change**: Historical shoreline trends.
        - **Sea level rise (SLR)**: Based on RCP4.5 and RCP8.5 climate scenarios.
        - **Storm-driven erosion**: Instantaneous shoreline changes due to extreme events.


        > *"Example"*

        > *“Around Europe, where has notable erosion occurred along coastal floodplains over recent decades?.”*

        **Data Sources**

        The shoreline dataset for the analysis is that provided by the European Environment Agency (EEA, 2017). Other coastal characteristics were sourced as shown below.

        <div class="grid cards" markdown>

        **Geomorphology and sediment type**
        EEA/Eurosion (EEA, 2004); interpretation of World Imagery / Google Earth (Esri, 2024; Google Earth, 2024).

        **Land cover/use**
        Corine Land Cover 2018 (CLC, 2020).

        **Indicative coastal floodplain extent (extreme tides, storms, 2m sea-level rise)**
        CoCliCo flood units (Lincke & Hinkel, 2023).

        **Decadal shoreline movement trends (1984–2021)**
        ShorelineMonitor+ (extended from Luijendijk et al., 2018).

        **Location of coastal structures (hard defences, other human infrastructure constraining shoreline evolution)**
        EEA/Eurosion (EEA, 2004); interpretation of World Imagery / Google Earth (Esri, 2024; Google Earth, 2024).

        </div>

        ![](./assets/Tool/shoreline.png){ width=800 .center}

        **Methods**

        The EEA shoreline was disaggregated into its component segments, which were then used as the basic unit for the database. A coastal zone extending 100m landward of the shoreline was defined as a representative landward extent and used for the identification of descriptive attributes. Attributes from the coastal characteristics data sources were added using spatial joins capabilities within the QGIS geographic information system software. Attributes were checked and amended, where appropriate, following visual interpretation of satellite imagery.

        Important notes:

        - 1. Indicative coastal floodplains were used in the database, scenario-based modelled flood extents are available and described in the Flood Maps Data Layer.

        - 2. The historical shoreline movement trend is based on satellite measurements and is classified into three trends; erosion, accretion and stable. These broad classes identify rapidly eroding or accreting shorelines with slower changing shorelines classed as stable. The CoasTER database therefore provides broad shoreline movement trends rather than providing precise localised rates.

        **Climate Scenarios**

        The dataset includes projections for two climate scenarios

        <div class="grid cards" markdown>

        - **RCP4.5**
        *A medium-emission scenario where global temperatures rise moderately.*

        - **RCP8.5**
        *A high-emission scenario where global temperatures rise significantly.*


        </div>

        **Ensembles**

        Data is computed for seven statistical ensembles (1st, 5th, 17th, 50th, 83rd, 95th, and 99th percentiles) at two key timeframes: **2050 and 2100**. The projections stem from the **LISCOAST project**, a comprehensive study of coastal dynamics under climate change.

        ---

        **How to Use the CoasTER database**

        Users can query the database using a range of attributes. For example:

        - [x] **Coastal classification**: see the distribution of geomorphological classes
        - [x] **Hard engineering**: see where defences and other structures influence coastal evolution.
        - [x] **Shoreline evolution**: for the indicative coastal floodplains, see shorelines with recent rapid shoreline movement trends
        - [x] **Combine attributes**: to further define areas of interest

        ---

        **Database Outputs**

        The CoasTER database considers the current situation around Europe. Its attributes can be queried for coastal analysis.

        ![](./assets/Tool/shoreline_output.jpg){ width=800 .center}

        ---

        **Why Is This Data Important?**

        The CoasTER database allows coastal areas where mobile sediments and coastal floodplains are co-located to be identified. It can be used as a preliminary diagnostic tool to identify areas where the interaction between flooding and erosion should be examined more closely, especially where significant erosion has been a recent trend and may continue into the future. It can also show where coastal structures and development may be affected by, and/or influence, future coastal sediment movements.

        - [x] **Coastal risk management**: Identifying areas vulnerable to erosion and planning protective measures.
        - [x] **Infrastructure planning**: Supporting long-term decision-making for sustainable coastal development.
        - [x] **Climate adaptation**: Evaluating potential impacts of sea level rise and storm events.
        - [x] **Scientific research**: Providing a robust dataset for studying coastal responses to climate change.

        **Example of use**

        > *"I would like to know where developed areas have coastal structures within 100m of the shoreline and have been subject to recent erosion and may need further management.”*

        ---

        **Limitations**

        The CoasTER database is limited in coverage and accuracy by its source data. This has resulted in some counties and sections of the shoreline (e.g., inlets and small islands) not being included. It provides an interpretation of the coastal system as defined by the 2017 shoreline which omits more recent coastal developments such as port expansions and has digitizing artifacts that have not always been corrected.

        **Further Analysis**

        The CoasTER database provides a base to which further information relevant to the broadscale analysis of coastal floodplains can be added or updated as required.

        **References:**

        CLC. (2020). CORINE Land Cover 2018 (vector), Europe, 6-yearly - version 2020_20u1, May 2020. https://land.copernicus.eu/en/products/corine-land-cover/clc2018

        EEA. (2004). Geology and geomorphology (EUROSION). Retrieved April 2023, from https://www.eea.europa.eu/data-and-maps/figures/geology-and-geomorphology

        Esri. (2024). Esri World Imagery https://www.arcgis.com/home/webmap/viewer.html?webmap=50c23e4987a44de4ab 163e1baeab4a46

        Google Earth. (2024). https://earth.google.com/web/

        Lincke, D., & Hinkel, J. (2023). Report and final GIS layer of flood risk management units.

        CoCliCo project deliverable 6.2. https://coclicoservices.eu/wp- content/uploads/2021/11/WP6_D6.2.Report-and-final-GIS-layer-of-flood-risk- management-units.pdf

        Luijendijk, A., Hagenaars, G., Ranasinghe, R., Baart, F., Donchyts, G., & Aarninkhof, S. (2018). The state of the world’s beaches. Scientific Reports, 8(1), 6641. https://doi.org/10.1038/s41598-018-24630-6

---

## **Exposure and Vulnerability**



???+  "Data Layers & User Stories"

    === "Building Exposure"

        The Building Exposure User Story in the CoCliCo platform maps the risk of coastal flooding to buildings in low-lying coastal areas under different climate scenarios. As sea levels rise and extreme weather events become more frequent, understanding which areas are most at risk is crucial for resilience planning and adaptation.

        This tool combines building data from OpenStreetMap with advanced flood maps, providing policymakers, urban planners, and coastal managers with detailed insights on flood vulnerability. By highlighting localized risks, it supports evidence-based decision-making for long-term coastal adaptation.

        > *"I need to see building exposure now and in the future for different climate change scenarios, so I can better understand the potential risk hotspots."*

        ---

        **Methods**

        The building footprints extracted from OpenStreetMap are combined with CoCliCo’s state-of-the-art inundation maps.

        **Data Sources**

        The building exposure is based on the latest building information extracted from OpenStreetMap. OpenStreetMap provides a consistent data layer across Europe, with standardized information on building type and location. 

        ![](./assets/Tool/EXP_DATA.png){ width=900 .center}

        ---

        **How to Use the Building Exposure data**

        The Building Exposure data can be used to:

        - [x] **Visualize flood risk**: Explore which buildings are exposed to sea-level rise and coastal flooding under different scenarios.
        - [x] **Compare scenarios**: Switch between SSPs, percentiles, and time horizons to understand how exposure changes over time.
        - [x] **Overlay with other layers**: Combine with hazard, infrastructure, or socio-economic layers for a more complete risk assessment.
        - [x] **Export and analyze**: Download exposure maps or raw data for detailed local analysis in the Workbench or external GIS tools.

        ---

        **Model Outputs**

        - [x] Visualizations display building exposure at decadal timesteps from 2030 to 2150 for three SSPs scenarios and one high-end scenario.
        - [x] Interactive features allow scenario comparisons and data downloads for local and regional decision-making.

        ![](./assets/Tool/building_output.png){ width=800 .center}

        ---

        **Why is this Data Important?**

        - [x] **Resilience planning**: Identifies hotspots of flood risk to guide adaptation strategies.
        - [x] **Policy support**: Informs compliance with EU and national flood directives.
        - [x] **Investment prioritization**: Helps authorities and planners focus resources on the most vulnerable areas.
        - [x] **Community safety**: Ensures critical buildings and neighborhoods remain protected as sea levels rise.

        ---

        **Example of use**

        > *"Using the Building Exposure User Stories, city planners identified their neighbourhoods as having a higher risk of flooding related to sea level rise by 2050 under high-emission scenarios high-emission scenarios compared to other neighbourhoods in the country"*

        **Limitations**

        While OpenStreetMap provides a consistent coverage across Europe, it does not provide a complete coverage. Across Europe, the average completeness is estimated to be roughly 70%. Some countries have integrated national-scale databases within OpenStreetMap (e.g. The Netherlands, France & Italy) and are therefore almost complete, other countries have very active user communities that aim for a near-complete data (e.g., Germany). However, some countries still experience several gaps (e.g., Ireland and the United Kingdom). Given the potential of missed buildings, we advise local authorities to careful check, and if possible to re-run the analysis with local information before any decisions are made.

        **Further Analysis**

        The building exposure layer is the starting point for the coastal risk assessment. Moreover, within the [Workbench](further_analysis.md) one can extract exposure data for their area of preference, allowing to better understand how sea-level rise will increase future coastal flood risk within any coastal area across Europe.


    === "People Exposure"

        The **People Exposure** User Story in the CoCliCo platform shows how many people may be affected by coastal flooding in the future. It combines high-resolution flood and population data to provide clear insights under different climate and socioeconomic scenarios.

        Since future population growth and movement are uncertain, this tool considers multiple scenarios to improve flood risk assessments. By mapping projected exposure to coastal flooding, it helps policymakers, urban planners, and resilience experts make informed decisions for adaptation and risk reduction.

        > *"I need information of the development of exposed population in the future for different combinations of climate and socioeconomic scenarios on a regional to national scale, so I can preliminary assess exposure to coastal flooding."*

        ---

        **Data Sources**

        CoCliCo's population projections use IIASA data, downscaled with historical trends and spatial factors like roads, urban areas, and coastline proximity. Areas unsuitable for development, such as steep slopes, water-covered regions, and protected areas, are excluded. These projections are combined with CoCliCo flood data to assess population exposure to coastal flooding.

        - Based on national population and urbanization projections from IIASA
        - Downscaled and spatially distributed using historic population data (GHS-POP)

        Projections account for key geographic and infrastructural influences. Distance to:

        - Roads (OSM data)
        - Urban areas (defined by population density, Degree of Urbanization method)
        - Coastline (MERIT DEM coastal mask)
        - Urban centers (travel time model by Weiss et al., 2018)

        Excluded from future population growth

        - High elevation or steep slopes (MERIT DEM)
        - Permanently flooded areas (Corine Land Cover)
        - Protected areas (World Database on Protected Areas)

        ![](./assets/Tool/EXP_POP_DATA_2.png){width=800px .center}

        ---

        **Methods**

        CoCliCo’s population projections are created by using a model (Reimann et al. (2021)) that helps distribute updated national population data from IIASA (2010–2100) in 10-year intervals. The data is broken down at a 1 km resolution for EU countries and the UK, for different Shared Socioeconomic Pathways (SSPs).

        The model works by first calculating the "potential" or attractiveness of each area (or grid cell). It then distributes population changes over time based on this potential. The "potential" of an area is influenced by factors like how close it is to nearby areas, population density, and distance from the coastline. The model also considers past patterns of people moving between coastal/inland and urban/rural areas, adjusting for two time periods. In addition, urbanization projections are used to account for the different ways urban and rural areas develop over time in each SSP.

        These population projections are combined with flood projections based on the integrated climate and socioeconomic scenarios to assess how many people are exposed to coastal flooding. The population and flood projections are aligned to ensure they match in both projection and resolution, allowing for accurate calculation of exposed populations at the Local Administrative Units (LAUs) level in coastal areas. These results are then summarized at smaller spatial levels.

        ---

        **How to Use the People Exposure data**

        The Exposed Population data can be used to:

        - [x] **Explore current and future exposure**: See how many people are projected to be affected by coastal flooding under different climate and socioeconomic scenarios.
        - [x] **Compare scenarios**: Analyze differences across SSPs, defence levels, and return periods (e.g., 100-year vs. 1000-year events).
        - [x] **Zoom into multiple scales**: View projections at national, NUTS2, and LAU levels for both broad and detailed insights.
        - [x] **Overlay with other layers**: Combine with sea-level rise or exposure datasets for a more complete picture of coastal risk.
        - [x] **Export and analyze further**: Download data and maps for advanced analysis in the Workbench or other GIS platforms.


        ---

        **Model Outputs**

        - [x] Visualizations display gridded population projections for the years 2010, 2030, 2050 and 2100 for five integrated scenarios (No SLR-SSP2, SSP1-2.6, SSP2-4.5, SSP5-8.5 and one high-end scenario with SSP5).
        - [x] Interactive features allow scenario comparisons and data downloads for local to national decision-making.

        ![](./assets/Tool/people_output.png){ width=800 .center}

        ---

        **Why Is This Data Important?**

        - [x] **Holistic planning**: Accounts for both climate change and population dynamics, the two key drivers of future flood exposure.
        - [x] **Supports adaptation**: Helps policymakers and planners target strategies where people are most at risk.
        - [x] **Improves equity**: Highlights vulnerable populations that may need priority protection and resources.
        - [x] **Evidence-based policy**: Provides transparent, high-resolution projections to align with EU directives and national adaptation plans.


        ---

        **Example of use**

        > *"Using the exposed population projections User Story, local authorities identified a concentration of population exposure in a specific area by 2050 under a high sea level scenario and low defence level. This analysis initiated a systematic and targeted adaptation planning process in this area, focusing on enhancing defences to eliminate the population exposure."*

        **Limitations**

        Limitations of the population projections:

        - **Population Decline:** In areas with population decline, the model treats cell potential differently. In urban areas, higher cell potential is linked to population loss due to suburbanization. In rural areas, lower cell potential is associated with higher population loss. This is a general assumption and might not apply to all EU regions.
        - **Urban and Rural Definitions:** Urban and rural areas are redefined after each timestep based on urbanization share. However, this measure only reflects the fraction of the population living in urban areas and doesn’t capture the complex structure of urban regions.

        Limitations of the exposed population:

        - **Data Alignment:** To combine flood and population projections, both need to have the same resolution and projection. We adjust the population data to match the flood projections, but this can affect population counts.
        - **Coastline Differences:** The population and flood projections use different coastlines, so some people living near the coast might not be considered at risk, even if they are on the ocean side of the coastline.

        **Further Analysis**

        To account for the full range of uncertainty in population development and its impact on coastal flooding, it’s useful to explore other socioeconomic scenarios beyond the integrated ones. While these additional estimates aren’t included directly in the platform, they can be explored in the [Workbench](further_analysis.md) by combining various climate and socioeconomic scenarios at different spatial scales.


    === "Critical Infrastructure"

        The **Critical Infrastructure layer** provides EU-wide high-resolution, object-based representations of key economic assets, buildings, and infrastructure systems in coastal areas prone to flooding.

        It includes spatially explicit information on **buildings**, **transportation networks**, and **essential service facilities** that are vital for economic and societal functioning. These components are mapped as distinct object types to support risk assessments and inform coastal adaptation efforts.

        **Example:**
        > *“I want to assess which critical infrastructure elements—like power stations, roads, or public service buildings—are at risk in coastal flood zones to help inform emergency planning and resilience investment.”*

        ---

        ### Data Sources
        The dataset combines building and critical infrastructure data from:

        - **OpenStreetMap (OSM)**
        - **EUBUCCO database**
        - Auxiliary datasets (national and European-specific databases)

        This ensures both comprehensive coverage and data accuracy.

        ---

        ### Critical Infrastructure Systems and Subsystems

        <div class="grid cards" markdown>

        - **Energy**
        - **Generation**: Power Plant, Generator
        - **Transmission**: Cable, Line
        - **Distribution**: Towers (Transmission Towers), Utility Poles, Substation, Switch, Catenary Mast, Transformer

        - **Transportation**
        - **Railways**: Railway
        - **Roads**: Primary, Secondary, Tertiary, Trunk, Link, Road
        - **Airports**: Aerodrome, Airport

        - **Telecommunication**
        - **Telecom**: Communication Tower, Mobile Phone

        - **Health**
        - **Healthcare**: Clinic, Doctors, Hospital, Dentist, Pharmacy, Physiotherapist, Alternative, Laboratory, Optometrist, Rehabilitation, Blood Donation, Birthing Center

        - **Education**
        - **Education**: College, Kindergarten, Library, School, University

        </div>

        ---

        ### Infrastructure Object Types

        - **Grey polygons** → Buildings (residential, commercial, industrial, public)
        - **Blue lines** → Linear infrastructure (roads, railways, power lines)
        - **Red dots** → Point infrastructure (power stations, telecom towers, water pumping stations)

        All features are curated and geospatially aligned to reflect their **true footprint and geometry** as accurately as possible.

        ---

        ### Methods

        1. **Data Extraction**

        - Critical infrastructure subsystems from **OSM**.
        - Buildings from **EUBUCCO** (EU + UK coverage).

        2. **Attribute Completion**

        - Missing OSM attributes filled using a **Random Forest algorithm**.
        - Example: If road attributes (e.g., maximum speed, number of lanes) are missing, values are inferred from similar road segments.

        3. **Spatial Refinement**

        - Assets and buildings **clipped to the coastal zone**.
        - Subdivided by **Local Administrative Units (LAU)** for greater granularity.

        ---

        ### Geographic Coverage

        - Coastal **LAUs (municipality level)** within the **European Union** and the **United Kingdom**.

        ---

        ### How to Use the Data

        - **Visual Analysis** → Identify infrastructure exposed to flood risks.
        - **Overlay with Hazard Layers** → Combine with SLR and flood models to assess exposure.
        - **Stakeholder Engagement** → Support discussions with municipalities, utilities, planners.
        - **Risk Prioritisation** → Inform emergency preparedness, resilience planning, and investment.

        ---

        ### Model Output

        The two following illustration provides an overview of how the infrastructure layer and the building can be used within the platform. For instance, Figure 1 shows a screenshot on overlying the flood map assuming a scenario with no protection standards for SSP5 for an event with a return period of a 1000 years at the time horizon of 2100 around the LAU Couarde-sur-Mer (FR). The shades of the LAUs give an indication on the percentage of building exposed. Furthermore, by clicking on the LAU polygon, the dashboard provides a timeline of the percentage of building exposed across all scenarios.

        ***Figure 1**: Building exposure*

        ![](./assets/Tool/ci_output.png){ width=800 .center}

        The critical infrastructure layer can also be overlayed with the flood maps. Figure 2 displays the flood depth around Couarde-sur-Mer (FR) assuming no protection standards, SSP5, for 2100 in combination to the infrastructure network.

        ***Figure 2**: Critical infrastructure exposure*

        ![](./assets/Tool/ci_output2.png){ width=800 .center}

        ---

        ### Why Is This Data Important?

        Critical infrastructure is essential for **public safety, economic stability, and disaster recovery**.
        Mapping and assessing exposure in coastal zones supports:

        - [x] Evaluating direct & cascading impacts of flooding.
        - [x] Strengthening **climate resilience planning**.
        - [x] Guiding **land-use decisions & investment**.
        - [x] Ensuring continuity of **essential services**.

        ---

        ### Example of Use

        > *“A regional planning authority overlaid the critical infrastructure dataset with projected coastal flooding extents. This revealed that several **emergency response buildings** and **power substations** were at high risk under future sea-level rise scenarios. The data helped prioritise relocation efforts and informed a new coastal zoning policy, ensuring service continuity and community safety.”*


    === "Population Projections"

        The Population Projections layer provides projections of population counts and their distribution, at a high spatial level, for different futures of socioeconomic development until 2100. The dataset has been developed based on historical population dynamics and projections of population development at national scale. The future distribution of population is important for assessing potential differences in spatial population development for a range of socioeconomic futures and to see changes in mobility patterns.

        > *"I need information about the future distribution of population in my region to identify areas of high population concentration for demographic planning."*

        ---

        **Data Sources**

        The population projections downscale the national IIASA population projections (Release 3.1) to a higher spatial level of ~1km resolution based on historical trends and factors such as road networks, urban areas, and coastal proximity. Areas unsuitable for development, such as steep slopes, water-covered regions, and protected areas, are excluded.

        The national population and urbanization projections from IIASA are downscaled and spatially distributed using historic population data (GHS-POP).

        Projections account for key geographic and infrastructural influences. Distance to:

        - Roads (OSM data)
        - Urban areas (defined by population density, Degree of Urbanization method)
        - Coastline (MERIT DEM coastal mask)
        - Urban centers (travel time model by Weiss et al., 2018)

        Excluded from future population growth

        - High elevation or steep slopes (MERIT DEM)
        - Permanently flooded areas (Corine Land Cover)
        - Protected areas (World Database on Protected Areas)

        ---

        **Methods**

        CoCliCo’s population projections are created by extending the model of Reimann et al. (2021) that helps distribute updated national population data from IIASA (2010–2100) in 10-year intervals. The data are resolved at a 1 km resolution for EU countries and the UK, for different Shared Socioeconomic Pathways (SSPs).

        The extended model first calculates the "potential" or attractiveness of each area (or grid cell). It then distributes population changes over time based on this potential. The "potential" of an area is influenced by factors such as how close it is to nearby areas, population density, and distance from the coast. The model also considers past patterns of people moving between coastal/inland and urban/rural areas, during two time periods. In addition, urbanization projections are used to account for the different ways urban and rural areas develop over time in each SSP.

        Socioeconomic scenarios:

        Shared Socioeconomic Pathways (SSP): Five different pathways describing potential socioeconomic futures and their challenges to adaptation and mitigation. Population, urbanization and GDP development have been quantified on a national level.

        The population dataset includes projections for three SSP:

        - SSP1: Focus on sustainable development and an open and globalized economy with rapid technological development. Population growth is low and urbanization is high as cities become more attractive.

        - SSP2: Following recent development trends. Intermediate population growth and urbanization with considerable urban sprawl.

        - SSP5: Focus on economic growth based on conventional development through fossil fuels. Strong population growth and high urbanization with urban sprawl.

        ---

        **How to Use the Exposed People data**

        - Scenario Selection: Select a Shared Socioeconomic Pathway (SSP1, SSP2, SSP5)

        - Timeframe selection: Available for 2010, 2030, 2050, 2100

        ---

        **Model Outputs**

        Maps of population distribution at ~1km resolution for different Shared Socioeconomic Pathways (SSP1, SSP2, SSP5) and timesteps (2010, 2030, 2050, 2100) for the EU countries and the United Kingdom.

        ---

        **Why Is This Data Important?**

        The population projections are crucial for accounting for uncertainties in socioeconomic development by depicting a wide range of possible futures in terms of population development. Furthermore, the population projections can be combined with spatial data on hazards to assess exposure and inform adaptation planning.

        ---

        **Example of use**

        > *"County authorities utilized spatial population projections based on different SSPs to anticipate future demographic trends. The projections revealed a consistent pattern across scenarios: population increasingly concentrated in the county town, while rural areas faced ongoing depopulation. Though the intensity of this trend varied by SSP, the insights enabled the county to take proactive, informed action. By leveraging these projections, decision-makers were able to adopt a balanced development strategy that promoted fair and sustainable urban growth without neglecting rural communities. This approach reduced socio-spatial inequalities and ensured that both urban and rural populations received equal protection from coastal hazards."*

        **Further Analysis**

        To account for the full range of uncertainty in population development and associated future exposure to coastal flooding, it’s useful to explore other socioeconomic scenarios beyond the integrated ones. While these additional estimates aren’t included directly in the platform, they can be explored in the Workbench by combining various climate and socioeconomic scenarios at different spatial scales.

---

## **Risk and Adaptation**



???+  "Data Layers & User Stories"

    === "Cost-Benefit Analyses"

        The Cost-Benefit Analyses User Story in the CoCliCo platform helps identify the most cost-effective ways to manage coastal flood risks under different climate scenarios. It evaluates three key adaptation strategies:

        - Protection – Building coastal defences like seawalls.
        - Retreat – Relocating people and assets away from flood zones.
        - Accommodation – Flood-proofing buildings to withstand extreme events.

        The platform provides country-level insights on the best mix of these strategies, with more detailed local assessments available through the workbench. This helps policymakers and planners make informed, cost-effective adaptation decisions.

        > *"I want to see economically optimal coastal adaptation options both today and, in the future, as well as the expected investments in coastal adaptation and the potential costs of flood damages"*

        **Data Sources**

        The data flow of the cost-benefit model can be seen in this workflow chart. The output of the model (efficient adaptation pathways in the middle of the Figure) then feed onto the CoCliCo platform. Several parts or even components of this detailed Figure can be excluded to simplify it, e.g. dynamic programming, implementation of adaptation options, etc. The SSP/RCP scenarios inform the sea level rise (SLR) and vertical land motion (VLM) data.

        ![](./assets/Tool/CBA_DATA.png){ width=900 .center}

        **Methods**

        The cost-benefit optimisation integrates several components:

        - A hazard component to model extreme sea level
        - An exposure component to assess population and assets at risk
        - A vulnerability component to assess the susceptibility of assets to hazards
        - An adaptation state space to outline potential adaptation pathways
        - Cost functions to estimate the costs associated with adaptation actions

        The multi-stage cost-benefit optimisation is conducted for each of the 41,327 coastal floodplains individually. We consider a time horizon from 2020 to 2150 with 10-year time steps, a discount rate of 3% and three greenhouse gas emission scenarios: low emissions (SSP1-2.6), high emissions (SSP2-4.5) and very high emissions (SSP5-8.5).

        **Climate Scenario**

        The dataset includes projections for three climate scenarios:

        <div class="grid cards" markdown>

        - **SSP1-2.6**
        *A low-emission scenario where global temperatures are limited to 1.5°C above pre-industrial levels, reflecting a sustainable future with rapid decarbonization.*

        - **SSP2-4.5**
        *A medium-emission scenario where global temperatures rise moderately, reflecting a future with some efforts to mitigate climate change.*

        - **SSP5-8.5**
        *A high-emission scenario where global temperatures rise significantly, reflecting a future with continued high greenhouse gas emissions and limited mitigation efforts.*

        </div>

        **Projections**

        The dataset includes projections up to the years **2050, 2100, and 2150**, offering key metrics to inform decision-making for coastal resilience.

        **Adaptation Strategy**

        <div class="grid cards" markdown>

        - **Protection**
            *Raising coastal defenses.*
        - **Retreat**
            *Managed withdrawal from vulnerable areas.*
        - **Accommodation**
            *Implementing flood-proofing measures.*
        - **Protection & Retreat**
            *A combined strategy where both approaches are efficient.*
        - **No Adaptation**
            *Areas where adaptation measures are deemed inefficient.*

        </div>

        The analysis accounts for adaptation costs, residual flood damages, and the most cost-efficient adaptation strategies for each floodplain.

        ---

        **How to Use the Data**

        - [x] **Scenario Selection**: Choose from the available scenarios ( RCP4.5, RCP8.5) to explore how Cost-Benefit Analysis may change under different climate futures.
        - [x] **Adaptation Strategy**: Select an adaptation strategy between Protection, Retreat, Accommodation, Protection & Retreat adn No Adaptation
        - [x] **Projection**: Choose between 2050, 2100, or 2150, depending on the timeframe for the adaptation strategy.


        ---

        **Model Outputs**

        - For each coastal floodplain, the model determines the economically optimal adaptation pathway, which is a sequence of adaptation options over time. These adaptation pathways can be explored through the workbench.

        - The web viewer illustrates the proportion of the coastline where each adaptation option is economically optimal by 2150 for each country, based on the economically optimal coastal adaptation pathways for all 41,327 floodplains.

        ![](./assets/Tool/cba_output1.png){ width=800 .center}
        ![](./assets/Tool/cba_output2.png){ width=800 .center}


        ---

        **Why Is This Data Important?**

        This dataset is crucial for guiding **cost-effective and sustainable coastal adaptation strategies** under different climate change and socioeconomic scenarios. It helps:

        - [x] **Coastal decision-makers** initiate proactive adaptation planning.
        - [x] **Global institutions** estimate future adaptation costs at regional and national scales.
        - [x] **Researchers and policymakers** assess the effectiveness of adaptation pathways over time.

        ---

        **Example of use**

        > *"National policymakers identified that significant funding would be required to address coastal flood risks in various regions. They allocated funding for coastal adaptation, encouraging local authorities to conduct their own research. This approach allowed local governments to assess specific risks and develop tailored solutions, ensuring more effective, region-specific adaptation strategies."*

        ---

        **Limitations**

        This cost-benefit model uses broad data to manage computational limits, which means it doesn't include detailed information about properties, land use, or infrastructure. As a result, the model may be less accurate for specific floodplains. For example, it might suggest retreat as the best adaptation option for an area with a nuclear power plant, but this could present major challenges that the model doesn’t account for.

        The model also only considers the median sea-level rise (SLR), leaving out high-end SLR scenarios. A sensitivity analysis showed that uncertainties in factors like the discount rate, protection and retreat costs, and protection levels have a bigger impact on the choice of adaptation options, the timing of actions, and total costs than the climate change scenarios themselves.

        ---

        **Further Analysis**

        Technical users can use the [Workbench](./further_analysis.md) to perform detailed, localized analyses by adjusting variables like flood risks, cost factors, and adaptation options. This allows for tailored assessments of the most cost-effective strategies and the timing of actions at the local scale.

        Users can explore different sea-level rise scenarios, test adaptation measures, and incorporate local data such as infrastructure details to refine their analysis. The Workbench enables deeper insights, helping inform more precise local adaptation strategies.



    === "Damage Costs"


        The Damage Costs User Story in the CoCliCo aim at presenting the direct economical impacts of coastal flooding under different climate scenarios. While many coastal infrastructures are protected today, rising sea levels will increase flood extent and depth, leading to higher damage costs without further adaptation.

        This tool helps policymakers and planners assess these costs at national, regional, and local levels in order to inform adaptation strategies. It combines the latest sea level projections, European flood hazard data, and infrastructure inventories to provide city-scale estimates of future flood damage.

        > *"I need to quantify damage costs of infrastructures exposed to flooding and assess how it evolves under different climate change scenarios"*

        **Data Sources**

        Damage costs on infrastructures are calculated by combining three main components: **hazard**, **exposure**, and **vulnerability curves**.

        - **Hazards**

            - Source: CoCliCo project (data producer: IH-Cantabria; available on the CoCliCo STAC Catalog)
            - Data: Flood maps (water depth) with or without defences
            - Coverage: Hindcast, 2030, 2050, 2100, and 2150
            - Scenarios: Permanent flooding, 1-year, 100-year, and 1000-year return periods under multiple SLR scenarios

        - **Exposure**

            - Source: Coastal European Exposure Database (data producer: Institute for Environmental Studies, Vrije Universiteit Amsterdam; available on the CoCliCo STAC Catalog)
            - Classes: 11 infrastructure types – Building, Power, Wastewater, Telecom, Oil, Gas, Education, Healthcare, Rail, Road, and Water
            - Geometry: Infrastructures represented as **points, lines, polygons, or multipolygons**

        - **Vulnerability Curves**

            - Source: *Physical Vulnerability Database for Critical Infrastructure Hazard Risk Assessments* (data producer: Institute for Environmental Studies, Vrije Universiteit Amsterdam)
            - Data: Compilation of published vulnerability curves and associated costs
            - Coverage: 102 vulnerability curves linked to 179 cost values
            - Purpose: Characterize the **percentage of damage** to infrastructure as a function of **water depth**, differentiated by infrastructure type


        ![](./assets/Tool/DAM_DATA.png){width=900px .center}


        **Methods**

        The damage costs are calculated by intersecting hazard (raster) and exposure (polygons) data layers, and vulnerability curves. First, we overlay the coastal flood hazard map with infrastructure data to obtain an average water height for each infrastructure. Then, based on the category of the infrastructure, we apply the corresponding vulnerability curves (e.g. healthcare, education, railway, etc).

        For the CoCliCo project, we used 18 different vulnerability curves. Once the damage is determined, the associated cost calculation is carried out: the damage cost is the product of the building's surface area, the percentage of damage, and the maximum damage, based on construction costs.

        **How to Use the Data**

        The Damage Cost data can be used to:

        - [x] **Estimate economic impacts**: Quantify the direct financial losses from coastal flooding under different climate and sea-level rise scenarios.
        - [x] **Compare across scales**: Assess costs at municipal, regional, and national levels to understand where risks and damages are concentrated.
        - [x] **Support planning and investment**: Use damage estimates to prioritize adaptation strategies and allocate resources efficiently.
        - [x] **Overlay with exposure data**: Combine with building and infrastructure exposure layers for a more complete risk assessment.
        - [x] **Export and refine**: Download datasets for further analysis in the Workbench or other GIS tools.

        ---

        **Model Outputs**

        Potential costs can be visualized in different ways: through a map that displays a color gradient based on the total damage cost for each LAU (Local Administrative Unit) across all infrastructures. To do this, the user selects the type of defense, the desired SSP scenario, the time horizon and the return period. The user can also view more details by clicking on a specific LAU. In this case, they can select the defense level, return period, and the category of infrastructure they are interested in. A graph will appear showing the evolution of costs over time, based on the different SSP scenarios.

        Importantly, the costs presented here are the costs associated to a particular return period. It neither corresponds to the costs associated to a particular event that would affect a specific region, nor to an expected annual damage value that would integrate costs of various return periods.

        ![](./assets/Tool/damage_output.png){ width=800 .center}

        ---

        **Why Is This Data Important?**

        - [x] **Economic justification for adaptation**: Provides tangible cost estimates that can help policymakers argue for timely investments in resilience.
        - [x] **Supports strategic prioritization**: Highlights areas where damage costs are projected to be highest, helping decision-makers focus resources.
        - [x] **Complements exposure data**: Goes beyond identifying assets at risk by showing the financial implications of flooding.
        - [x] **Improves disaster preparedness**: Assists in planning for compensation mechanisms, insurance schemes, and recovery strategies.


        ---

        **Example of use**

        > “National policy makers used the damage costs estimates to get a first order estimate of costs in regions and municipalities and prioritize on adaptation actions and investments in order to maximize the efficiency of public investments in adaptation. While this information can not be used as a single source of information to guide adaptation investments, it provides an element that can be considered together with additional evidence and selection criteria of decision makers”

    	> “The damage costs estimates at municipal level have been used to identify the potential damage costs in a particular flood plain, allowing to anticipate to what extent existing compensation mechanisms (e.g. insurance) are adequately designed to address loss and damages a now and in the future”

        ---

        **Limitations**

        One of the main limitations of this method lies in the assumption that infrastructures remain unchanged over time, without considering any construction or destruction of infrastructure. Additionally, the lack of detailed information on certain infrastructures can affect the accuracy of selecting the vulnerability curve, which may lead to variations in the estimated cost. Similarly, the price used is an average price that does not account for specific factors such as the location of the damage or the current local construction costs.

---



<div align="center">
    <a href="https://www.openearth.nl/coclico-workbench/">
        <img src="../assets/logo1.png" width="150" alt="CoCliCo Logo">
    </a>
    <p><small>Copyright &copy; 2025 CoCliCo Services</small></p>
</div>