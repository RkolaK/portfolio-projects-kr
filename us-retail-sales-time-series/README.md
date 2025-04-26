
# Time Series Modeling of U.S. Monthly Retail Sales

## Overview
This Python project analyzes U.S. monthly retail sales data from January 1992 to June 2021. It reshapes and transforms the dataset into a time series format using pandas, enabling trend analysis, seasonality detection, and preparation for forecasting. The project demonstrates fundamental time series operations such as resampling, frequency setting, and visualization to better understand long-term growth trends in the retail sector.

## Objectives
- Reshape raw sales data into a time-indexed series
- Visualize retail sales trends over time
- Set the appropriate datetime index and frequency
- Identify long-term trends and seasonal patterns
- Prepare data for future time series modeling

## Dataset
- **File:** `us_retail_sales.csv`
- **Key Variables:**
  - `YEAR`
  - `MONTH`
  - `SALES`

## Features
- Data reshaping using `melt()` to create a time-indexed format
- Setting monthly frequency (`MS`) for time series
- Line plot of retail sales trends over the full date range
- Observations of overall growth and possible seasonality

## Technologies Used
- Python 3.x
- pandas
- matplotlib
- NumPy

## How to Run
1. Ensure the dataset `us_retail_sales.csv` is available in the working directory.
2. Open and run the notebook `us_retail_sales_time_series.ipynb` using Jupyter Notebook or JupyterLab.
3. Review the generated time series plots and insights.

## Author
KR  
Date: July 27, 2024
