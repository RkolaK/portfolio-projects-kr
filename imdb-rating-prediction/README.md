
# IMDb Rating Prediction

This project explores the factors that influence IMDb movie ratings and builds a basic predictive model using the IMDb Top 1000 Movies dataset from Kaggle.

## Project Overview

- Analyze the relationship between movie metadata (runtime, genre, director, votes, gross earnings) and IMDb ratings.
- Perform Exploratory Data Analysis (EDA) with visualizations.
- Build and evaluate a simple Linear Regression model to predict IMDb ratings.

## Dataset

- **Source**: [IMDb Top 1000 Dataset](https://www.kaggle.com/datasets/emanchauhdary/imdb-top-1000-dataset)
- **Features Used**: Runtime, Meta Score, Number of Votes, Gross Earnings, Genre (top 10 genres), Director.

## Methods

- Data Cleaning (handling types, missing values)
- Feature Engineering (genre extraction, numeric features)
- Exploratory Data Analysis (histograms, scatterplots, bar charts)
- Modeling (Linear Regression using scikit-learn)
- Evaluation Metrics: R² Score and RMSE

## Results

- **R² Score**: 0.616
- **RMSE**: 0.198
- The model explains approximately 62% of the variance in IMDb ratings among top-rated films.

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- scikit-learn
- Jupyter Notebook

## Author
KR  
Date: April 26, 2025
