# pages/5_About.py
import streamlit as st

st.title("About this Project")

st.markdown("""
**Project Title:** Data analysis of livable conditions in selected Indian cities based on Sustainable Development Goals
            
**Team:** E1 - R. Sanjna Sukirti

**SDGs addressed:**  
- SDG 1 — No poverty  
- SDG 3 — Good health and well-being 
- SDG 11 — Sustainable cities & communities

**Methodology:**  
- Data were compiled for five cities Chennai, Bangalore, Mumbai, Delhi and Kolkata for the years 2019 to 2023.  
- Indicators: PM2.5, PM10, NO2, SO2, Population, Area, Below Poverty Line %, Infant Mortality Rate, Life Expectancy.  
- Sub-indices computed: Air Quality Index, Population Density Index, Health Index, Below Poverty Line Index.  
- Composite livability index = mean(AQI, PDI, HI, BPL_index) scaled 0–100.

**Usage:**  
Use the City Analysis page to inspect a single city, Comparison to compare multiple cities, Visualizations for figures used in the journal paper, and Leaderboard for ranking of cities based on urban livability index.

""")
