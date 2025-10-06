# pages/5_About.py
import streamlit as st

st.title("About this Project")

st.markdown("""
**Project Title:** Data analysis of livable conditions in selected Indian cities based on Sustainable Development Goals

**SDGs addressed:**  
- SDG 1 — No poverty  
- SDG 3 — Good health and well-being  
- SDG 6 — Clean water and sanitation (linked via water quality in extended versions)  
- SDG 11 — Sustainable cities & communities

**Methodology (brief):**  
- Data were compiled for five cities (2019–2023).  
- Indicators: PM2.5, PM10, NO2, SO2, population, area (density), BPL %, infant mortality rate, life expectancy.  
- Sub-indices computed: AQI (air pollutants), PDI (population density), HI (health), BPL_index.  
- Final livability index = mean(AQI, PDI, HI, BPL_index) scaled 0–100.

**Usage:**  
Use the City Analysis page to inspect a single city, Comparison to compare multiple cities, Visualizations for figures used in the paper, and Leaderboard for ranking.

**Deploying:**  
To deploy this app publicly: push the repo to GitHub and connect it to Streamlit Cloud (https://share.streamlit.io). See README for instructions.
""")
