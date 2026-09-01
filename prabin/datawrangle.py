import pandas as pd
import numpy as np

# 1. Load the data
df = pd.read_csv("clean_sheet", sep="|")

# 2. Keep only the columns we actually care about
df = df[['Player', 'Squad', 'MP', 'Min', 'Save%']].copy()

# 3. Clean the Save Percentage column
df['Save%'] = pd.to_numeric(df['Save%'], errors='coerce') # Force it to be a number
df = df.dropna(subset=['Save%'])                          # Delete empty rows

# 4. Filter for players who played at least a full match (90 mins)
df = df[df['Min'] >= 90]

# 5. Label the teams as Knockout or Group Stage
# First, find the maximum matches played by each squad
df['Team_Max_Matches'] = df.groupby('Squad')['MP'].transform('max')

# Next, label them based on that max number
df['Stage'] = np.where(df['Team_Max_Matches'] > 3, 'Knockout', 'Group Stage')

# Look at the first 5 rows to make sure it worked perfectly!
display(df)