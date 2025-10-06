# pages/4_Leaderboard.py
import streamlit as st
import plotly.express as px
from utils import load_and_process

st.title("Leaderboard — Average Livability (2019–2023)")

df = load_and_process("urban_data.csv")
# compute average livability per city
rank = df.groupby("city", as_index=False)["livability_index"].mean().sort_values("livability_index", ascending=False)
rank["rank"] = range(1, len(rank)+1)

st.subheader("City ranking (average Livability Index)")
st.dataframe(rank.reset_index(drop=True))

fig = px.bar(rank, x="city", y="livability_index", text="livability_index", title="Average Livability Index (2019–2023)")
st.plotly_chart(fig, use_container_width=True)

# Short explanation
st.markdown("**Result:** Ranked list of cities by average livability across the study period.")
st.markdown("**Discussion:** The leaderboard helps summarize which cities consistently perform well and which require targeted policy interventions.")
