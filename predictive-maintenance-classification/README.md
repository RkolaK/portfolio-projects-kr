
# Predictive Maintenance Classification Using Sensor Data

## Overview
This Python project builds a machine learning model to predict equipment failures using time-stamped sensor data. It addresses a common challenge in manufacturing and production: avoiding costly downtime through early failure prediction. A Random Forest classifier is trained and evaluated on labeled sensor data to classify whether equipment is likely to fail.

## Business Problem
Unexpected equipment failures can cause major interruptions in operations. Predictive maintenance uses real-time and historical sensor data to identify patterns leading to failure, enabling proactive maintenance strategies that save time, reduce costs, and improve safety.

## Objectives
- Load and inspect predictive maintenance sensor data
- Prepare and clean the dataset
- Train and evaluate a Random Forest classification model
- Assess model performance using accuracy, confusion matrix, and classification report
- Identify feature importance for better interpretability

## Dataset
- **File:** `predictive_maintenance.csv`
- **Key Variables:**
  - Sensor readings (`sensor_1`, `sensor_2`, ..., `sensor_n`)
  - `Failure` (binary classification target)

## Features
- Data cleaning and EDA with `pandas` and `seaborn`
- Model training using `RandomForestClassifier`
- Performance metrics: accuracy, precision, recall, F1-score
- Confusion matrix and classification report
- Feature importance visualization

## Technologies Used
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## How to Run
1. Ensure the dataset `predictive_maintenance.csv` is in your working directory.
2. Open the notebook `predictive_maintenance_classification.ipynb` in Jupyter.
3. Run each cell in order to explore, train, and evaluate the model.

## Author
KR  
Date: May 25, 2025
