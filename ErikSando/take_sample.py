import pandas as pd

df = pd.read_csv("data/fifa-player-dist.csv")

# Filter out players with <10 attempted passes
df = df[df["Passes"] >= 10]

# Only include relevant columns
df = df[["Player", "Position", "Passing Accuracy (%)"]]

df_mf = df[df["Position"] == "MF"] # Midfield players
df_fw = df[df["Position"] == "FW"] # Forward players

# Take random samples with n = 30
sample_mf = df_mf.sample(n=30, random_state=12345)
sample_fw = df_fw.sample(n=30, random_state=12345)

# Write samples to a CSV file
sample_mf.to_csv("data/sample_mf.csv", index=False)
sample_fw.to_csv("data/sample_fw.csv", index=False)

