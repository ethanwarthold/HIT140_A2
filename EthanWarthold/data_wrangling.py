#Step 1: Data wrangling


import pandas as pd


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
