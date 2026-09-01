import math
import pandas as pd
import scipy.stats as st
import statsmodels.stats.weightstats as stm

sample_mf = pd.read_csv("data/sample_mf.csv")
sample_fw = pd.read_csv("data/sample_fw.csv")

# Focus on passing accuracy data
sample_mf = sample_mf["Passing Accuracy (%)"]
sample_fw = sample_fw["Passing Accuracy (%)"]

# Descriptive statistics:
# Find mean, median, variance, and standard deviation from the samples
mean_mf = sample_mf.mean()
median_mf = sample_mf.median()
stddev_mf = sample_mf.std()
n_mf = sample_mf.size

mean_fw = sample_fw.mean()
median_fw = sample_fw.median()
stddev_fw = sample_fw.std()
n_fw = sample_fw.size

print("\n=== SAMPLE DATA ===")

print("\nMidfielder data:")
print(f"Mean:        {mean_mf:.2f}")
print(f"Median:      {median_mf:.1f}")
print(f"Std. Dev:    {stddev_mf:.2f}")
print(f"Total (n):   {n_mf}")

print("\nForward data:")
print(f"Mean:        {mean_fw:.2f}")
print(f"Median:      {median_fw:.1f}")
print(f"Std. Dev:    {stddev_fw:.2f}")
print(f"Total (n):   {n_fw}")

# Inferential statistics: confidence intervals

C = 95
alpha = (100 - C) / 100

ci_mf_lower, ci_mf_upper = stm._zconfint_generic(
    mean_mf, stddev_mf / math.sqrt(n_mf),
    alpha=alpha, alternative="two-sided"
)

ci_fw_lower, ci_fw_upper = stm._zconfint_generic(
    mean_fw, stddev_fw / math.sqrt(n_fw),
    alpha=alpha, alternative="two-sided"
)

mean_mf_pop = (ci_mf_lower + ci_mf_upper) / 2
half_interval_mf = (ci_mf_upper - ci_mf_lower) / 2

mean_fw_pop = (ci_fw_lower + ci_fw_upper) / 2
half_interval_fw = (ci_fw_upper - ci_fw_lower) / 2

print()
print(f"Midfielders  {C}% CI:  {mean_mf_pop:.2f} ± {half_interval_mf:.2f}  :  {ci_mf_lower:.2f} to {ci_mf_upper:.2f}")
print(f"Forwards     {C}% CI:  {mean_fw_pop:.2f} ± {half_interval_fw:.2f}  :  {ci_fw_lower:.2f} to {ci_fw_upper:.2f}")

# Inferential statistics: two sample t-test
# Null hypothesis: same accuracy between mf and fw, mean_mf = mean_fw
# Alternative hypothesis: mean_mf != mean_fw (two sided test)

t_stats, p_value = st.ttest_ind_from_stats(
    mean_mf, stddev_mf, n_mf, mean_fw, stddev_fw, n_fw,
    equal_var=False, alternative="two-sided"
)

print(f"\nt* = {t_stats:.4f}\np = {p_value:.4f}")

if p_value < 0.05:
    print("\nNull hypothesis is rejected, there is a statisically significant difference.")

else:
    print("\nNull hypothesis can not be rejected, there is not a statistically significant difference.")
