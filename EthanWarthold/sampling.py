#Step 2: Data preparation and sampling

import pandas as pd
import numpy as np


def prepare_and_sample(df: pd.DataFrame,
    sample_size_per_group: int,
    random_seed: int,
    ) -> tuple[pd.DataFrame, pd.DataFrame, float]:
    median_age = df["Age"].median()
    df = df.copy()
    df["age_group"] = np.where(df["Age"] < median_age, "younger", "older")

    parts = []
    for _, sub in df.groupby("age_group"):
        n = min(sample_size_per_group, len(sub))
        parts.append(sub.sample(n=n, random_state=random_seed))
    sample = pd.concat(parts).reset_index(drop=True)

    return df, sample, median_age
