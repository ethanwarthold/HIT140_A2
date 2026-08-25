import pandas as pd

sample_mf = pd.read_csv("data/sample_mf.csv")
sample_fw = pd.read_csv("data/sample_fw.csv")

# Focus on passing accuracy data
sample_mf = sample_mf["Passing Accuracy (%)"]
sample_fw = sample_fw["Passing Accuracy (%)"]

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
