"""
FIFA World Cup 2026 -- Analytic Task
=====================================
Focus: Goalkeeper age vs. shot-stopping performance (save percentage)

Analytic question:
    Do older goalkeepers (31+) have a different save percentage than
    younger goalkeepers (under 31) at the FIFA World Cup 2026?
    Excludes goalkeepers who never appeared in a match or never faced
    a shot on target (save % undefined for them).

Data source:
    FBref - Goalkeeping standard stats table for the World Cup 2026
"""

import pandas as pd
import numpy as np
from scipy import stats

RAW_FILE = "gk_stats.csv"
RANDOM_SEED = 42
SAMPLE_SIZE_PER_GROUP = 15
CONFIDENCE_LEVEL = 0.95


# ---------------------------------------------------------------------------
# 1. DATA WRANGLING
# ---------------------------------------------------------------------------
def load_and_wrangle(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, skiprows=1)

    df["country"] = df["Squad"].str.split(" ", n=1).str[1]

    keep_cols = ["Player", "country", "Age", "Born", "MP", "Starts",
                 "Min", "90s", "GA", "GA90", "SoTA", "Saves", "Save%",
                 "CS", "CS%"]
    df = df[keep_cols].copy()

    df["MP"] = pd.to_numeric(df["MP"], errors="coerce")
    df = df[df["MP"].fillna(0) > 0]

    df["Save%"] = pd.to_numeric(df["Save%"], errors="coerce")
    df = df.dropna(subset=["Save%"])

    return df.reset_index(drop=True)
    
# ---------------------------------------------------------------------------
# 2. DATA PREPARATION AND SAMPLING
# ---------------------------------------------------------------------------
def prepare_and_sample(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, float]:
    median_age = df["Age"].median()
    df = df.copy()
    df["age_group"] = np.where(df["Age"] < median_age, "younger", "older")

    parts = []
    for _, sub in df.groupby("age_group"):
        n = min(SAMPLE_SIZE_PER_GROUP, len(sub))
        parts.append(sub.sample(n=n, random_state=RANDOM_SEED))
    sample = pd.concat(parts).reset_index(drop=True)

    return df, sample, median_age