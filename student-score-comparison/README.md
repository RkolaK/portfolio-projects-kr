
# Comparative Analysis of Student Test Scores by Section Type

## Overview
This R project analyzes student test scores from two classroom sections: Regular and Sports. It explores performance distributions through subsetting, visual analysis, and summary statistics. The analysis highlights differences in central tendency and spread between the two groups and offers possible interpretations for observed performance patterns.

## Objectives
- Compare average and median scores between Regular and Sports sections
- Visualize score distributions using scatter plots and boxplots
- Interpret statistical tendencies and identify influencing factors

## Dataset
- **File:** `scores.csv`
- **Key Variables:**
  - `Score` – test score (quantitative)
  - `Count` – number of students earning each score
  - `Section` – either "Regular" or "Sports" (categorical)

## Features
- Subsetting data by section type
- Scatter plots showing score distributions by section
- Calculation of mean and median for each group
- Boxplot comparing overall score distributions
- Interpretation of score trends and influencing factors

## Technologies Used
- R
- Base R plotting
- ggplot2

## Key Insight
The Regular Section shows slightly higher mean and median scores compared to the Sports Section. However, individual variations exist, and other factors such as study habits could contribute to the differences observed.

## How to Run
1. Make sure the dataset `scores.csv` is located in a `data/` folder.
2. Open the script `student_scores_by_section.R` in RStudio.
3. Run the script to generate visualizations and summary statistics.

## Author
KR  
Date: June 30, 2023
