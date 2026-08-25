"""
FIFA World Cup 2026 — Assessment 2, Objective 1
Analytic question: On average, do teams eliminated in the group stage commit
more fouls per match than teams that reach the knockout stage?

This script covers:
  Step 3 — Data preparation & sampling
  Step 4 — Descriptive statistics

(Steps 5-6, confidence interval + two-sample t-test, come in a later script
once you've discussed the sampling approach with your tutor — see note below.)

Requirements: pandas, numpy  (both preinstalled in most environments)
Run:  python wc2026_analysis.py
"""

import pandas as pd
import numpy as np

RANDOM_SEED = 42  # fixed seed = reproducible sample every time this runs

# ---------------------------------------------------------------------------
# STEP 3a — Load the raw data (this is the ONLY step Excel was used for)
# ---------------------------------------------------------------------------
df = pd.read_excel("WC2026_Fouls_RawData.xlsx", sheet_name="Data")
df = df.dropna(subset=["Team_ID"])  # drops the legend rows at the bottom of the sheet
print(f"Loaded {len(df)} teams (population).")
print(df["Group (Advanced/Eliminated)"].value_counts(), "\n")

# ---------------------------------------------------------------------------
# STEP 3b — Define population vs sample
# ---------------------------------------------------------------------------
# POPULATION: all 48 teams that competed in the FIFA World Cup 2026.
#
# A note on "match-level" sampling: true match-by-match foul counts per team
# (each individual match, not season totals) exist only inside FIFA/fbref's
# individual match report pages — one per match, ~104 of them. Pulling all
# of those reliably wasn't feasible here, so instead of inventing per-match
# numbers, this script uses honest SIMPLE RANDOM SAMPLING of TEAMS from the
# population of 48 — a fully standard, legitimate sampling technique that
# satisfies the brief's "data preparation and sampling" requirement without
# fabricating data. Mention this reasoning explicitly in your presentation.
#
# SAMPLE: to keep the two groups comparable and avoid just re-analysing the
# whole population, we draw a simple random sample of 12 teams from EACH
# group (Advanced n=12 of 32, Eliminated n=12 of 16) without replacement.
# Using a FIXED random seed makes the sample reproducible for your teammates
# and marker.

SAMPLE_SIZE_PER_GROUP = 12

advanced_pop = df[df["Group (Advanced/Eliminated)"] == "Advanced"]
eliminated_pop = df[df["Group (Advanced/Eliminated)"] == "Eliminated"]

advanced_sample = advanced_pop.sample(n=SAMPLE_SIZE_PER_GROUP, random_state=RANDOM_SEED)
# Eliminated population is only 16 teams; sampling 12 of 16 still gives a
# genuine random subset (not the full population).
eliminated_sample = eliminated_pop.sample(n=SAMPLE_SIZE_PER_GROUP, random_state=RANDOM_SEED)

sample_df = pd.concat([advanced_sample, eliminated_sample]).reset_index(drop=True)

print(f"Drew a simple random sample of {SAMPLE_SIZE_PER_GROUP} teams from each group "
      f"(seed={RANDOM_SEED}).")
print("Sampled teams:")
print(sample_df[["Team", "Group (Advanced/Eliminated)", "Fouls_per_Match"]]
      .sort_values("Group (Advanced/Eliminated)").to_string(index=False), "\n")

# ---------------------------------------------------------------------------
# STEP 4 — Descriptive statistics (on the SAMPLE, as required by the brief)
# ---------------------------------------------------------------------------
def describe_group(sample, label):
    vals = sample["Fouls_per_Match"]
    stats = {
        "Group": label,
        "n": len(vals),
        "Mean": round(vals.mean(), 3),
        "Median": round(vals.median(), 3),
        "Std Dev (sample)": round(vals.std(ddof=1), 3),
        "Variance": round(vals.var(ddof=1), 3),
        "Min": vals.min(),
        "Max": vals.max(),
        "Range": round(vals.max() - vals.min(), 3),
    }
    return stats

adv_stats = describe_group(advanced_sample, "Advanced")
elim_stats = describe_group(eliminated_sample, "Eliminated")

summary = pd.DataFrame([adv_stats, elim_stats]).set_index("Group")
print("Descriptive statistics (sample):")
print(summary.to_string(), "\n")

# ---------------------------------------------------------------------------
# Save everything to one Excel file: sample used, and descriptive stats
# ---------------------------------------------------------------------------
with pd.ExcelWriter("WC2026_Sample_and_DescriptiveStats.xlsx", engine="openpyxl") as writer:
    sample_df.to_excel(writer, sheet_name="Sample_Used", index=False)
    summary.to_excel(writer, sheet_name="Descriptive_Stats")

print("Saved: WC2026_Sample_and_DescriptiveStats.xlsx")
print("\nNext steps (not yet in this script):")
print("  - Step 5: 95% confidence interval for each group's true mean fouls/match")
print("            (use scipy.stats.t.interval, or mean +/- t_crit * (sd/sqrt(n)))")
print("  - Step 6: two-sample t-test (scipy.stats.ttest_ind, equal_var=False)")
print("            comparing Advanced vs Eliminated sample means")
