import math
import pandas as pd
import scipy.stats as st
import statsmodels.stats.weightstats as stm

def confidence_interval(sample: pd.DataFrame, C: float):
    alpha = 1 - C

    mean = sample.mean()
    s = sample.std()
    n = sample.size

    lower, upper = stm._zconfint_generic(
        mean, s / math.sqrt(n),
        alpha=alpha, alternative="two-sided"
    )

    half_interval = (upper - lower) / 2

    return lower, upper, half_interval

def t_test(sampleA: pd.DataFrame, sampleB: pd.DataFrame):
    meanA, meanB = sampleA.mean(), sampleB.mean()
    sA, sB = sampleA.std(), sampleB.std()
    nA, nB = sampleA.size, sampleB.size

    return st.ttest_ind_from_stats(
        meanA, sA, nA, meanB, sB, nB,
        equal_var=False, alternative="two-sided"
    )
