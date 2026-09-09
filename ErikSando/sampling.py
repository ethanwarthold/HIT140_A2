import pandas as pd

# Data wrangling, preparation, and sampling

def take_sample(population_path: str, output_path: str, player_position: str, n: int, random_state: int):
    df = pd.read_csv(population_path)

    # Filter out players with <10 attempted passes
    df = df[df["Passes"] >= 10]

    # Only include relevant columns
    df = df[["Player", "Position", "Passing Accuracy (%)"]]

    # Filter for the chosen player position
    df = df[df["Position"] == player_position]

    # Take random sample with n = 30
    sample = df.sample(n=n, random_state=random_state)

    # Write samples to a CSV file
    sample.to_csv(output_path, index=False)