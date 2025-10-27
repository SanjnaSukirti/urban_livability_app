# Urban Livability Dashboard

This Streamlit web application analyzes and visualizes the livability of selected Indian cities based on multiple sustainability and quality-of-life indicators, aligned with the UN Sustainable Development Goals (SDG 1, 3, 6, 11).

## Overview:

This data analysis project computes a Livability Index using four equally weighted sub-indices:

**1. Air Quality Index (AQI)** - based on PM<sub>2.5</sub>, PM<sub>10</sub>, NO₂, and SO₂

**2. Population Density Index (PDI)** - based on population and area

**3. Health Index (HI)** - based on life expectancy and infant mortality rate

**4. Poverty Index (BPL)** - based on BPL population percentage

Each sub-index is normalized and combined to produce a composite Livability Index (0-100 scale).

## **Key Features:**

* **City-wise Analysis** - explore sub-indices and livability trends for each city.

* **City Comparison** - compare multiple cities and years interactively.

* **Visualization Dashboard** - six interactive Plotly visualizations with results & discussions.

* **Leaderboard** - ranks cities by average livability over the study period.

* **About Page** - project methodology, data sources, and direct SDG mapping.

## **Tech Stack:**

* **Streamlit** - Interactive web application development.

* **Plotly** - Interactive, professional graphs.

* **Pandas** - Core data handling and manipulation.

* **NumPy** - Normalization and other calculations.

## **Live Dashboard:**

The live web application can be viewed in the following link:

https://urban-livability-dashboard.streamlit.app/

## **Execution Instructions:**

### **Option 1: Run Locally**

**Step 1:** Clone the Repository

You can either clone the repository and move into the `Source_Code` folder

```
git clone https://github.com/<your-username>/Urban-Livability-Dashboard.git
cd Urban-Livability-Dashboard/Source_Code
```

Or directly download the `Source_Code` folder as a ZIP file from GitHub.

**Step 2:** Create a Virtual Environment (Optional but Recommended)

```
python -m venv env
source env/bin/activate      # for macOS/Linux
env\Scripts\activate         # for Windows
```

**Step 3:** Install Dependencies

```
pip install -r requirements.txt
```

**Step 4:** Run the Streamlit Web Application

```
streamlit run app.py
```

The app will launch automatically in your browser (Default: http://localhost:8501).

### **Option 2: View Online (No Installation Needed)**

The live deployed app is available at:
https://urban-livability-dashboard.streamlit.app/

### **Execution Notes:**

* Ensure all dependencies listed in `requirements.txt` are installed.
* The app requires an active internet connection for initial Streamlit components.
* Avoid modifying `urban_data.csv` unless adding updated city data.

This web application is developed as part of an academic research project on data analysis of urban living conditions in selected cities of India based on Sustainable Development Goals.
