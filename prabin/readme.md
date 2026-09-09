IMPACT OF GOALKEEPER IN WINNING WORLDCUP 2026

OVERVIEW
The analytical question "is there a significant difference in the average save percentage between goalkeepers whose teams advanced to the knockout stages and those whose teams were eliminated in the group stage?"
The main goal of this project is the find whether Goalkeeper palys an import part in winning games or not.

DATASET AND VARIABLES
Data for analysing was taken from "fbref https://fbref.com/en/comps/1/keepers/World-Cup-Stats".
csv file (sportsref_download_raw) file was downloaded and was cleaned using excel and saved as clean_sheet.csv.
Since all the data was not required only necessary variables were kept:
player and squad: basic information
min: total min played
mp: match played by a team
save%: total save % by a goalkeeper.

METHODOLOGY
Data cleaning and preparation
Data was loaded and only relevant columns was used
Players who played less than 90 minutes were filtered out to get concrete data.
Conveted save% to a numeric format and removed the missing value.

Splitting of data
Created new variable named stage
Those team who played more than 3 matched, that goalkeeper was labeled as Knockout stage
And Those team who played less than 3 matched, that goalkeeper was labeled as group stage

Sampling
Sample sizes: knockout stage (25), group stage (25)

Library used
math
statsmodels
pandas
numpy as
scipy

Installation done using PIP
pip install statsmodels pandas numpy scipy


RESULTS
This analysis shows the differnece betweeen two groups

Descriptive Statistics for Knockout Stage Keepers:
Count (n): 25
Mean:      65.14%
Std Dev:   17.82%
Minimum:   0.00%
Median:    69.20%
Maximum:   90.90%

Descriptive Statistics for Group Stage Keepers:
Count (n): 25
Mean:      53.71%
Std Dev:   19.98%
Minimum:   0.00%
Median:    57.10%
Maximum:   83.30%

Knockout Stage Keepers:
Confidence Interval of the mean: 58.16 to 72.13

Group Stage Keepers:
Confidence Interval of the mean: 45.88 to 61.54

Two-Sample t-Test Results:
t-statistic: 2.1350
p-value:     0.0380

CONCLUSION
The data shows a statistically significant difference, suggesting that advancing teams have goalkeepers with significantly higher save percentages