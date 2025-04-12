
# Exploratory Analysis of High School Education Data from ACS

## Overview
This R project analyzes high school educational attainment data from the American Community Survey (ACS), focusing on the percentage of individuals with a high school degree across U.S. counties. The project examines the distribution of this variable to determine how closely it follows a normal distribution and what that implies for future modeling and interpretation.

## Objectives
- Visualize the distribution of high school attainment (HSDegree)
- Evaluate normality using histograms, normal curves, and probability plots
- Calculate and interpret skewness, kurtosis, and z-scores
- Discuss implications for analysis and modeling

## Dataset
- **Source:** American Community Survey (ACS) 1-Year Estimates (2014)
- **File:** `acs-14-1yr-s0201.csv`
- **Key Variable:** `HSDegree` – percentage of individuals with a high school degree

## Features
- Histogram of `HSDegree` with normal curve overlay
- Probability plot (QQ plot)
- Summary statistics using `stat.desc()` from the `pastecs` package
- Discussion of normality, skewness, kurtosis, and z-scores

## Technologies Used
- R
- ggplot2
- pastecs

## Key Insights
- The `HSDegree` variable is **not normally distributed**
- Distribution is **negatively skewed** with heavy tails
- Normal models may not be suitable for this variable

## How to Run
1. Make sure the dataset `acs-14-1yr-s0201.csv` is in the `data/` folder.
2. Open the script `acs_education_analysis.R` in RStudio.
3. Run each block to generate visualizations and outputs.
4. Review the statistical summaries and plots.

## Author
KR  
Date: June 24, 2023
