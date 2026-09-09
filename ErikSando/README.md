## HIT140_A2/ErikSando
  The python code written by Erik Sando for assessment 2 of HIT140 (2026).
### Python modules
  pandas, scipy, statsmodels
  Installation using pip:
  > pip install pandas scipy statsmodels
  
  Installation using conda:
  > conda install pandas scipy statsmodels
### Usage
  Run with
  > python src/main.py
### Dataset
  The population data is saved in **data/fifa-player-dist.csv**, values taken from https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics/player-statistics under the "Distribution" category.
### Python files
##### sampling.py
  Module for data wrangling, preparation and sampling of the population data CSV file. Saves a samples of passing accuracy data for a chosen player position to a new CSV files.
##### stats.py
  Module for calculating confidence intervals and performing an unequal variance two sample t-test.
##### main.py
  Uses sampling.py and stats.py to run the analysis and print out sample means, standard deviations, median, confidence intervals, t-statistic and p-value.