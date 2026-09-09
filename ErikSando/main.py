import os
import pandas as pd
import sampling, stats

n = 30
RANDOM_STATE = 12345

if not os.path.exists("data/sample_mf.csv"):
    print("No midfield player sample found, taking sample")
    sampling.take_sample("data/fifa-player-dist.csv", "data/sample_mf.csv", "MF", n, RANDOM_STATE)

if not os.path.exists("data/sample_fw.csv"):
    print("No forward player sample found, taking sample")
    sampling.take_sample("data/fifa-player-dist.csv", "data/sample_fw.csv", "FW", n, RANDOM_STATE)

sample_mf = pd.read_csv("data/sample_mf.csv")
sample_fw = pd.read_csv("data/sample_fw.csv")

# Focus on passing accuracy data
sample_mf = sample_mf["Passing Accuracy (%)"]
sample_fw = sample_fw["Passing Accuracy (%)"]

# Descriptive statistics:
# Find mean, median, variance, and standard deviation from the samples

print("\n=== Sample Descriptive Statistics ===")

print("\nMidfielder data:")
print(f"Mean:        {sample_mf.mean():.2f}")
print(f"Median:      {sample_mf.median():.1f}")
print(f"Std. Dev:    {sample_mf.std():.2f}")
print(f"Total (n):   {sample_mf.size}")

print("\nForward data:")
print(f"Mean:        {sample_fw.mean():.2f}")
print(f"Median:      {sample_fw.median():.1f}")
print(f"Std. Dev:    {sample_fw.std():.2f}")
print(f"Total (n):   {sample_fw.size}")

# Inferential statistics: confidence intervals

C = 0.95

ci_mf_lower, ci_mf_upper, half_interval_mf = stats.confidence_interval(sample_mf, C)
ci_fw_lower, ci_fw_upper, half_interval_fw = stats.confidence_interval(sample_fw, C)

print("\n=== Confidence Intervals ===\n")
print(f"Midfielders  {C * 100:.0f}% CI:  {sample_mf.mean():.2f} ± {half_interval_mf:.2f}  :  {ci_mf_lower:.2f} to {ci_mf_upper:.2f}")
print(f"Forwards     {C * 100:.0f}% CI:  {sample_fw.mean():.2f} ± {half_interval_fw:.2f}  :  {ci_fw_lower:.2f} to {ci_fw_upper:.2f}")

# Inferential statistics: two sample t-test
# Null hypothesis: same accuracy between mf and fw, mean_mf = mean_fw
# Alternative hypothesis: mean_mf != mean_fw (two sided test)

print("\n=== Two Sample t-Test ===\n")

t_stats, p_value = stats.t_test(sample_mf, sample_fw)

print(f"t* = {t_stats:.4f}\np = {p_value:.4f}\n")

if p_value < 0.05:
    print("Null hypothesis is rejected, there is a statisically significant difference.")

else:
    print("Null hypothesis can not be rejected, there is not a statistically significant difference.")
