
# Global Energy Demand Forecasting and Trend Analysis

## Overview
This project explores historical energy consumption trends across 44 countries from 1990 to 2020 and uses time series forecasting to predict future demand. The analysis focuses on three major countries—United States, China, and India—and applies the ARIMA model to forecast their energy use over the next decade.

## Business Problem
Understanding energy consumption trends is critical for shaping energy policies, climate strategies, and infrastructure investments. As demand continues to rise in emerging economies and plateau in developed countries, forecasting future demand is essential for strategic planning.

## Features
- Cleans and preprocesses global energy data from Kaggle
- Performs EDA to uncover consumption patterns by country
- Case study comparison: U.S., China, and India
- Forecasts future energy consumption using ARIMA (2,1,2)
- Visualizes historical and projected trends with line charts

## How to Use
1. Open and run the notebook `global_energy_forecasting.ipynb`.
2. Ensure the dataset `Country_Consumption_TWH.csv` is in the same directory.
3. Review output visuals and forecasts in the notebook.

## Technologies Used
- Python 3.x
- Libraries: pandas, matplotlib, seaborn, statsmodels, numpy

## Example Outputs
- Bar charts of top energy-consuming countries
- Line plots showing trends for U.S., China, and India
- ARIMA forecast plots projecting energy use to 2030

## Limitations
- Uses only historical consumption data (no external variables)
- ARIMA assumes linear patterns and continuity
- Annual granularity limits short-term insights

## Author
KR  
Date: March 28, 2025
