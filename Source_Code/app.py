# app.py
import streamlit as st
from utils import load_and_process

st.set_page_config(page_title="Urban Livability Dashboard", layout="wide")

st.title("Urban Livability Index — Interactive Dashboard")
st.markdown("""
This dashboard presents an interactive analysis of urban livability (2019–2023) for selected Indian cities.
It computes a composite Livability Index from sub-indices: **Air Quality (AQI)**, **Population Density (PDI)**,
**Health Index (HI)** and **Poverty Index (BPL)**. Use the pages in the sidebar to explore city-level trends,
comparisons, visualizations, and the leaderboard.
""")

# load data once and cache
@st.cache_data
def load():
    return load_and_process("urban_data.csv")

df = load()

st.write("Dataset:")
st.dataframe(df)