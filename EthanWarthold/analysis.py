#Steps 3-5: Descriptive statistics, confidence interval, two-sample t-test


import pandas as pd
from scipy import stats


def descriptive_stats(sample: pd.DataFrame) -> pd.DataFrame:
    return sample.groupby("age_group")["Save%"].agg(
        ["count", "mean", "median", "std", "min", "max"]
    )


def confidence_interval(sample: pd.DataFrame, confidence: float):
    values = sample["Save%"]
    n = len(values)
    mean = values.mean()
    sem = stats.sem(values)
    ci_low, ci_high = stats.t.interval(confidence, df=n - 1, loc=mean, scale=sem)
    return n, mean, (ci_low, ci_high)


def two_sample_ttest(sample: pd.DataFrame) -> dict:
    younger = sample.loc[sample["age_group"] == "younger", "Save%"]
    older = sample.loc[sample["age_group"] == "older", "Save%"]

    levene_stat, levene_p = stats.levene(younger, older)
    equal_var = levene_p > 0.05

    t_stat, p_val = stats.ttest_ind(younger, older, equal_var=equal_var)
    test_name = "Student's t-test" if equal_var else "Welch's t-test"

    return {
        "test_used": test_name,
        "levene_stat": levene_stat,
        "levene_p": levene_p,
        "younger_n": len(younger), "younger_mean": younger.mean(), "younger_sd": younger.std(),
        "older_n": len(older), "older_mean": older.mean(), "older_sd": older.std(),
        "t_stat": t_stat,
        "p_value": p_val,
        "significant": p_val < 0.05,
    }
