# utils.py
import pandas as pd
import numpy as np

COND_TO_TDS = 0.67

def load_and_process(path="urban_data.csv"):
    """
    Load CSV and compute subindices & livability index.
    Returns processed DataFrame with lower-case columns.
    """
    df = pd.read_csv(path)
    # normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # ensure numeric columns cleaned (commas, percent signs)
    numcols = ["pm2.5","pm10","no2","so2","population","area","bpl_population",
               "infant_mortality_rate","life_expectancy"]
    for c in numcols:
        if c in df.columns:
            df[c] = df[c].astype(str).str.replace(",","",regex=False).str.replace("%","",regex=False)
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # population density
    if ("population" in df.columns) and ("area" in df.columns):
        df["pop_density"] = df["population"] / df["area"]
    else:
        df["pop_density"] = np.nan

    # Air quality normalization (negative indicators -> lower = better)
    aq_indicators = [c for c in ["pm2.5","pm10","no2","so2"] if c in df.columns]
    for col in aq_indicators:
        denom = df[col].max() - df[col].min()
        df[col + "_norm"] = (df[col].max() - df[col]) / (denom if denom!=0 else 1)

    if aq_indicators:
        df["aqi"] = df[[col + "_norm" for col in aq_indicators if (col + "_norm") in df.columns]].mean(axis=1)

    # PDI (population density index) - lower density better
    if "pop_density" in df.columns:
        denom = df["pop_density"].max() - df["pop_density"].min()
        df["pdi"] = (df["pop_density"].max() - df["pop_density"]) / (denom if denom!=0 else 1)
    else:
        df["pdi"] = np.nan

    # Health index: life expectancy (positive), IMR (negative)
    if ("life_expectancy" in df.columns) and ("infant_mortality_rate" in df.columns):
        le_denom = df["life_expectancy"].max() - df["life_expectancy"].min()
        df["le_norm"] = (df["life_expectancy"] - df["life_expectancy"].min()) / (le_denom if le_denom!=0 else 1)

        imr_denom = df["infant_mortality_rate"].max() - df["infant_mortality_rate"].min()
        df["imr_norm"] = (df["infant_mortality_rate"].max() - df["infant_mortality_rate"]) / (imr_denom if imr_denom!=0 else 1)

        df["hi"] = df[["le_norm","imr_norm"]].mean(axis=1)
    else:
        df["hi"] = np.nan

    # BPL index (lower BPL % better)
    if "bpl_population" in df.columns:
        denom = df["bpl_population"].max() - df["bpl_population"].min()
        df["bpl_index"] = (df["bpl_population"].max() - df["bpl_population"]) / (denom if denom!=0 else 1)
    else:
        df["bpl_index"] = np.nan

    # Final livability (equal-weight average of AQI, PDI, HI, BPL_index)
    subidxs = [c for c in ["aqi","pdi","hi","bpl_index"] if c in df.columns]
    if subidxs:
        df["livability_index"] = df[subidxs].mean(axis=1) * 100
    else:
        df["livability_index"] = np.nan

    # safe types
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["city"] = df["city"].astype(str)

    # sort
    df = df.sort_values(["city","year"]).reset_index(drop=True)
    return df
