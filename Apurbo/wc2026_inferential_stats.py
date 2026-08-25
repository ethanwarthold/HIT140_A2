"""
FIFA World Cup 2026 — Assessment 2, Objective 1
Analytic question: On average, do teams eliminated in the group stage commit
more fouls per match than teams that reach the knockout stage?

This script covers:
  Step 5 — Inferential statistics: Confidence Interval
  Step 6 — Inferential statistics: Two-sample t-test

Run this AFTER wc2026_analysis.py (it reuses the same sample, same seed,
so the numbers line up with your Step 3/4 results).

Requirements: pandas, numpy, scipy
Run:  python wc2026_inferential_stats.py
"""

import pandas as pd
import numpy as np
from scipy import stats

RANDOM_SEED = 42
SAMPLE_SIZE_PER_GROUP = 12

# ---------------------------------------------------------------------------
# Reload the same population and redraw the SAME sample (same seed = same
# 24 teams as in wc2026_analysis.py)
# ---------------------------------------------------------------------------
df = pd.read_excel("WC2026_Fouls_RawData.xlsx", sheet_name="Data")
df = df.dropna(subset=["Team_ID"])

advanced_pop = df[df["Group (Advanced/Eliminated)"] == "Advanced"]
eliminated_pop = df[df["Group (Advanced/Eliminated)"] == "Eliminated"]

advanced_sample = advanced_pop.sample(n=SAMPLE_SIZE_PER_GROUP, random_state=RANDOM_SEED)
eliminated_sample = eliminated_pop.sample(n=SAMPLE_SIZE_PER_GROUP, random_state=RANDOM_SEED)

adv_vals = advanced_sample["Fouls_per_Match"].values
elim_vals = eliminated_sample["Fouls_per_Match"].values

# ---------------------------------------------------------------------------
# STEP 5 — 95% Confidence Interval for each group's TRUE mean fouls/match
# ---------------------------------------------------------------------------
def confidence_interval(values, confidence=0.95):
    n = len(values)
    mean = np.mean(values)
    sem = stats.sem(values)          # standard error of the mean
    t_crit = stats.t.ppf((1 + confidence) / 2, df=n - 1)
    margin = t_crit * sem
    return mean, mean - margin, mean + margin, margin

results = []
for label, vals in [("Advanced", adv_vals), ("Eliminated", elim_vals)]:
    mean, lo, hi, margin = confidence_interval(vals)
    results.append({
        "Group": label,
        "n": len(vals),
        "Sample Mean": round(mean, 3),
        "95% CI Lower": round(lo, 3),
        "95% CI Upper": round(hi, 3),
        "Margin of Error": round(margin, 3),
    })
    print(f"{label}: mean = {mean:.3f} fouls/match, "
          f"95% CI = [{lo:.3f}, {hi:.3f}]")

ci_df = pd.DataFrame(results).set_index("Group")
print()
print("Interpretation: we are 95% confident the TRUE average fouls-per-match")
print("for the whole population of that group falls within its interval above.\n")

# ---------------------------------------------------------------------------
# STEP 6 — Two-sample t-test (Welch's, unequal variances assumed)
# ---------------------------------------------------------------------------
# H0 (null hypothesis): mean fouls/match is the SAME for Advanced and Eliminated teams
# H1 (alternative):      mean fouls/match is DIFFERENT between the two groups
ALPHA = 0.05

t_stat, p_value = stats.ttest_ind(elim_vals, adv_vals, equal_var=False)

print("Two-sample t-test (Welch's, Eliminated vs Advanced):")
print(f"  t-statistic = {t_stat:.3f}")
print(f"  p-value     = {p_value:.4f}")

if p_value < ALPHA:
    conclusion = (f"p-value ({p_value:.4f}) < alpha ({ALPHA}) -> REJECT the null hypothesis. "
                  f"There IS a statistically significant difference in fouls/match "
                  f"between the two groups.")
else:
    conclusion = (f"p-value ({p_value:.4f}) >= alpha ({ALPHA}) -> FAIL TO REJECT the null "
                  f"hypothesis. We do NOT have enough evidence to say fouls/match differs "
                  f"between Advanced and Eliminated teams.")
print(f"  Conclusion: {conclusion}\n")

ttest_df = pd.DataFrame([{
    "Comparison": "Eliminated vs Advanced",
    "t-statistic": round(t_stat, 4),
    "p-value": round(p_value, 4),
    "alpha": ALPHA,
    "Significant at 5%?": "Yes" if p_value < ALPHA else "No",
    "Conclusion": conclusion,
}])

# ---------------------------------------------------------------------------
# Save results
# ---------------------------------------------------------------------------
with pd.ExcelWriter("WC2026_Inferential_Stats.xlsx", engine="openpyxl") as writer:
    ci_df.to_excel(writer, sheet_name="Confidence_Intervals")
    ttest_df.to_excel(writer, sheet_name="Two_Sample_TTest", index=False)

print("Saved: WC2026_Inferential_Stats.xlsx")
print("\nAll 6 steps of Objective 1 are now complete for this question:")
print("  1. Question formulated")
print("  2. Data wrangled (raw dataset)")
print("  3. Sample drawn from population")
print("  4. Descriptive statistics computed")
print("  5. Confidence interval computed")
print("  6. Two-sample t-test run")
