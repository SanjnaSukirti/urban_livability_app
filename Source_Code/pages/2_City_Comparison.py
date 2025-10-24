# pages/2_City_Comparison.py
import streamlit as st
import plotly.express as px
import pandas as pd
from utils import load_and_process

st.title("City Comparison")

df = load_and_process("urban_data.csv")
cities = sorted(df["city"].unique())

selected = st.multiselect("Select cities (2-5)", cities, default=cities[:2])
year = st.selectbox("Select year", sorted(df["year"].dropna().unique().astype(int)))

if len(selected) < 2:
    st.info("Select at least two cities for comparison.")
else:
    df_sel = df[(df["city"].isin(selected)) & (df["year"]==year)]
    if df_sel.empty:
        st.warning("No data for selected cities/year.")
    else:
        st.subheader(f"Livability Index Comparison — {year}")
        fig = px.bar(df_sel, x="city", y="livability_index", color="city", text="livability_index",
                     title=f"Livability Index ({year}) - Comparison")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Sub-indices comparison (AQI, PDI, HI, BPL)")
        subcols = [c for c in ["aqi","pdi","hi","bpl_index"] if c in df.columns]
        if subcols:
            mdf = df_sel.set_index("city")[subcols].reset_index().melt(id_vars="city", var_name="subindex", value_name="value")
            fig2 = px.bar(mdf, x="city", y="value", color="subindex", barmode="group",
                          title=f"Sub-indices Comparison ({year})")
            st.plotly_chart(fig2, use_container_width=True)

        st.markdown("### Table")
        st.dataframe(df_sel.reset_index(drop=True))
