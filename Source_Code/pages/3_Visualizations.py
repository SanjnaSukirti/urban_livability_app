# pages/3_Visualizations.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils import load_and_process

st.title("Visualization Dashboard (6 Figures)")

df = load_and_process("urban_data.csv")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1. Livability Trend", "2. Heatmap", "3. Radar (sub-indices)",
    "4. Grouped Bar", "5. Boxplot", "6. Sub-indices (2023)"])

# 1 - Line trend
with tab1:
    st.header("1. Livability Index Trends (2019–2023)")
    fig = px.line(df, x="year", y="livability_index", color="city", markers=True,
                  title="Livability Index Trends (2019–2023)")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("**Result:** The line plot presents the temporal variation of the livability index for all five cities.")
    st.markdown("**Discussion:** Chennai shows high and stable scores; Bangalore and Mumbai are mid-range; Delhi and Kolkata show lower scores historically, with Kolkata improving recently.")

# 2 - Heatmap
with tab2:
    st.header("2. Livability Heatmap")
    pivot = df.pivot(index="city", columns="year", values="livability_index")
    fig2 = px.imshow(pivot, text_auto=".1f", aspect="auto", color_continuous_scale="YlGnBu",
                     title="Livability Index Heatmap (2019–2023)")
    fig2.update_xaxes(title="Year")
    fig2.update_yaxes(title="City")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("**Result:** The heatmap displays comparative livability values across cities and years.")
    st.markdown("**Discussion:** Highlights inter-city disparities and temporal improvements (e.g., Kolkata).")

# 3 - Radar (sub-indices) for a selected city/year
with tab3:
    st.header("3. Radar Chart — Sub-indices (AQI, PDI, HI, BPL)")
    city = st.selectbox("Select city for radar", sorted(df["city"].unique()), index=0)
    year = st.selectbox("Select year", sorted(df["year"].dropna().unique().astype(int)), index=0)
    row = df[(df.city==city) & (df.year==year)]
    if row.empty:
        st.warning("No data for selection.")
    else:
        categories = ["AQI","PDI","HI","BPL_index"]
        values = [row[c.lower()].values[0] for c in categories]
        fig3 = go.Figure()
        fig3.add_trace(go.Scatterpolar(r=values + [values[0]],
                                       theta=categories + [categories[0]],
                                       fill='toself', name=f"{city} {year}"))
        fig3.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,1])), showlegend=True,
                           title_text=f"Sub-indices Radar – {city} ({year})")
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("**Result:** Radar shows relative strengths/weaknesses across sub-indices.")
        st.markdown("**Discussion:** Use this to interpret the drivers of a city's overall score.")

# 4 - Grouped Bar
with tab4:
    st.header("4. City-wise Livability by Year (Grouped Bar)")
    fig4 = px.bar(df, x="year", y="livability_index", color="city", barmode="group",
                  title="City-wise Livability Index by Year")
    st.plotly_chart(fig4, use_container_width=True)
    st.markdown("**Result:** Grouped bars show inter-city rank per year.")
    st.markdown("**Discussion:** Useful to compare yearly ranking and see changes across time.")

# 5 - Boxplot
with tab5:
    st.header("5. Distribution of Livability (Boxplot)")
    fig5 = px.box(df, x="city", y="livability_index", points="all", title="Distribution of Livability Index (2019–2023)")
    st.plotly_chart(fig5, use_container_width=True)
    st.markdown("**Result:** Boxplot summarizes distribution of scores for each city.")
    st.markdown("**Discussion:** Highlights stability/variability across years for each city.")

# 6 - Sub-indices bar (2023)
with tab6:
    st.header("6. Sub-Indices Comparison (Choose Year)")
    sel_year = st.selectbox("Select year for sub-index comparison", sorted(df["year"].dropna().unique().astype(int)), index=len(df["year"].unique())-1)
    subset = df[df["year"]==sel_year][["city","aqi","pdi","hi","bpl_index"]].set_index("city")
    mdf = subset.reset_index().melt(id_vars="city", var_name="subindex", value_name="value")
    fig6 = px.bar(mdf, x="city", y="value", color="subindex", barmode="group", title=f"Sub-indices Comparison ({sel_year})")
    st.plotly_chart(fig6, use_container_width=True)
    st.markdown("**Result:** Bar chart compares the four sub-indices across cities for the selected year.")
    st.markdown("**Discussion:** Identifies which sub-index drives differences in overall livability.")
