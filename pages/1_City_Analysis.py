# pages/1_City_Analysis.py
import streamlit as st
import plotly.express as px
from utils import load_and_process

st.title("City-wise Analysis")

df = load_and_process("urban_data.csv")

cities = sorted(df["city"].unique())
city = st.selectbox("Select city", cities)

years = sorted(df["year"].dropna().unique().astype(int))
yr_range = st.select_slider("Select year (or range):", options=years, value=(years[0], years[-1]))

# filter
df_city = df[(df["city"]==city) & (df["year"]>=yr_range[0]) & (df["year"]<=yr_range[1])]

st.subheader(f"Overview — {city} ({yr_range[0]} to {yr_range[1]})")
if df_city.empty:
    st.warning("No data available for this selection.")
else:
    latest = df_city[df_city["year"]==df_city["year"].max()].iloc[-1]
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Livability Index (latest)", f"{latest['livability_index']:.2f}")
    col2.metric("AQI", f"{latest['aqi']:.2f}")
    col3.metric("PDI", f"{latest['pdi']:.2f}")
    col4.metric("HI", f"{latest['hi']:.2f}")

    st.markdown("### Trends")
    fig = px.line(df_city, x="year", y="livability_index", markers=True, title=f"{city} — Livability Index Trend")
    st.plotly_chart(fig, use_container_width=True)

    # sub-indices trends
    subcols = [c for c in ["aqi","pdi","hi","bpl_index"] if c in df_city.columns]
    if subcols:
        mdf = df_city.melt(id_vars=["year"], value_vars=subcols, var_name="subindex", value_name="value")
        fig2 = px.line(mdf, x="year", y="value", color="subindex", markers=True, title=f"{city} — Sub-indices")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Data table (filtered)")
    st.dataframe(df_city.reset_index(drop=True))
