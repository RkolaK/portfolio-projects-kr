
# Housing Market Analysis

## Overview
This R project analyzes a real estate dataset to explore relationships between house characteristics and sale prices. It demonstrates data aggregation, transformation, filtering, and the creation of new variables to enhance insights. Visualizations such as histograms and scatter plots are used to examine trends and detect outliers. Key functions such as `apply`, `aggregate`, and `ddply` highlight essential data manipulation skills in R.

## Objectives
- Calculate descriptive statistics (mean, min, max) on key variables
- Perform data aggregation by property type
- Create new engineered features (Total Bathrooms and Price Per Square Foot)
- Visualize distributions and relationships to detect trends and outliers
- Apply R functions for data manipulation (`apply`, `aggregate`, `ddply`)

## Dataset
- **File:** `week-6-housing.xlsx` (Sheet2)
- **Key Variables:**
  - `Sale Price`
  - `Bedrooms`
  - `Square Feet Total Living`
  - `Property Type`

## Features
- Average square footage lot size using `apply`
- Aggregated statistics of sales price by property type using `aggregate`
- Normalized square footage feature using `ddply`
- Histogram of sales price for 3-bedroom houses
- Scatter plot of living space versus sales price
- Creation of Total Bathrooms and Price Per Square Foot variables
- Outlier detection based on scatter plots

## Technologies Used
- R
- readxl
- plyr
- ggplot2

## How to Run
1. Ensure the dataset `week-6-housing.xlsx` is available in the `data/` folder.
2. Open the script `housing_market_analysis.R` in RStudio.
3. Run each block to perform data exploration, transformations, and visualizations.

## Author
KR  
Date: June 30, 2023
