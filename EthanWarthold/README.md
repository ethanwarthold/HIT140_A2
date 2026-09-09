# FIFA World Cup 2026 - Goalkeeper Age vs. Save Percentage

# requirements
Python 3.10+

# install dependencies
```
pip install pandas numpy scipy
```

# or if using anaconda prompt
```
conda install pandas numpy scipy
```

# project structure
```
├── main.py            
├── data_wrangling.py  
├── sampling.py         
├── analysis.py        
└── data/
	├── FBref_raw_goalkeeping_stats.csv
    ├── gk_sample.csv
    └── gk_stats.csv
```

# Data source:
    FBref Goalkeeping Standard Stats for FIFA World Cup '26
	`FBref_raw_goalkeeping_stats.csv`

# python main.py

The script prints each step's results to the console, and writes two output files:
	`gk_population_clean.csv`
	`gk_sample.csv`
	
For ease of marking this file is the main pipeline for:
```
    data_wrangling.py  -> Step 1: data wrangling
    sampling.py         -> Step 2: data preparation and sampling
    analysis.py          -> Steps 3-5: descriptives, CI, two-sample t-test
```
