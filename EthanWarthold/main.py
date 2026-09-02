"""

Data source:
    FBref - Goalkeeping standard stats table for the World Cup 2026

For ease of marking this file is the "main" pipeline for:
    data_wrangling.py  -> Step 1: data wrangling
    sampling.py         -> Step 2: data preparation and sampling
    analysis.py          -> Steps 3-5: descriptives, CI, two-sample t-test

"""

from data_wrangling import load_and_wrangle
from sampling import prepare_and_sample
from analysis import descriptive_stats, confidence_interval, two_sample_ttest

RAW_FILE = "data/gk_stats.csv"
RANDOM_SEED = 42
SAMPLE_SIZE_PER_GROUP = 15
CONFIDENCE_LEVEL = 0.95


def main():
    print("=" * 70)
    print("STEP 1: DATA WRANGLING")
    print("=" * 70)
    population = load_and_wrangle(RAW_FILE)
    print(f"Population after filtering (MP>=1, faced a shot): {len(population)} goalkeepers")
    population.to_csv("gk_population_clean.csv", index=False)

    print("\n" + "=" * 70)
    print("STEP 2: DATA PREPARATION AND SAMPLING")
    print("=" * 70)
    population, sample, median_age = prepare_and_sample(
        population, SAMPLE_SIZE_PER_GROUP, RANDOM_SEED
    )
    print(f"Median age used as group split: {median_age}")
    print(population["age_group"].value_counts().rename("population count"))
    print(f"\nStratified random sample drawn (n={SAMPLE_SIZE_PER_GROUP} per group):")
    print(sample["age_group"].value_counts().rename("sample count"))
    sample.to_csv("gk_sample.csv", index=False)

    print("\n" + "=" * 70)
    print("STEP 3: DESCRIPTIVE STATISTICS")
    print("=" * 70)
    desc = descriptive_stats(sample)
    print(desc.round(2))

    print("\n" + "=" * 70)
    print("STEP 4: CONFIDENCE INTERVAL")
    print("=" * 70)
    n, mean, (ci_low, ci_high) = confidence_interval(sample, CONFIDENCE_LEVEL)
    print(f"n = {n}, sample mean Save% = {mean:.2f}")
    print(f"{int(CONFIDENCE_LEVEL*100)}% CI for population mean Save%: ({ci_low:.2f}, {ci_high:.2f})")

    print("\n" + "=" * 70)
    print("STEP 5: TWO-SAMPLE T-TEST")
    print("=" * 70)
    result = two_sample_ttest(sample)
    print(f"Levene's test: stat={result['levene_stat']:.3f}, p={result['levene_p']:.3f} "
          f"-> {'equal' if result['levene_p'] > 0.05 else 'unequal'} variances assumed")
    print(f"Test used: {result['test_used']}")
    print(f"Younger: n={result['younger_n']}, mean={result['younger_mean']:.2f}, sd={result['younger_sd']:.2f}")
    print(f"Older:   n={result['older_n']}, mean={result['older_mean']:.2f}, sd={result['older_sd']:.2f}")
    print(f"t = {result['t_stat']:.3f}, p = {result['p_value']:.4f}")
    if result["significant"]:
        print("-> Statistically significant difference at alpha = 0.05")
    else:
        print("-> No statistically significant difference at alpha = 0.05")


if __name__ == "__main__":
    main()
