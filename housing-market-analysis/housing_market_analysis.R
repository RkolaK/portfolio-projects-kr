# Author: KR
# Date: 2023-06-30

# Load packages
library(readxl)
library(plyr)
library(ggplot2)
theme_set(theme_minimal())

# Set the working directory
setwd("/Users/kleberroncoletta/RStudio_Projects")

# Load the dataset to housing_df
housing_df <- read_excel("data/week-6-housing.xlsx", sheet = "Sheet2")

# Check how the dataset looks like
nrow(housing_df)
ncol(housing_df)
head(housing_df)

# 1. Use the apply function on a variable in your dataset.
# Calculate the average of the sq_ft_lot column
average_sq_ft_lot <- apply(housing_df["sq_ft_lot"], 2, mean)
average_sq_ft_lot

# 2. Use the aggregate function on a variable in your dataset.
# Rename column Sale Price to Sale_Price and calculate min, max and avg
names(housing_df)[2] <- "Sale_Price"
aggregate(Sale_Price ~ prop_type, data = housing_df, 
          FUN = function(x) c(min = min(x), max = max(x), average = mean(x)))

# 3. Use the plyr function on a variable in your dataset
# Split the data, modify Sale_Price and combine back together
modified_housing_df <- ddply(housing_df, .(prop_type), transform, 
                              Square_Feet_Modified = square_feet_total_living / 
                                  max(square_feet_total_living))
head(modified_housing_df)

# 4. Check distributions of the data.
# Filter the dataset for houses with 3 bedrooms
bedroom_3_df <- subset(housing_df, bedrooms == 3)

# Create a histogram
ggplot(bedroom_3_df, aes(x = Sale_Price)) +
    geom_histogram(bins = 20, fill = "steelblue", color = "white") +
    labs(title = "Sales Price for Houses with 3 Bedrooms", 
         x = "Sales Price", y = "Frequency")

# Create a scatterplot
ggplot(bedroom_3_df, aes(x = square_feet_total_living, y = Sale_Price)) +
    geom_point(color = "steelblue") + 
    labs(title = "Sales Price vs. Square Feet (3 Bedrooms)", 
         x = "Square Feet Total Living", y = "Sales Price")

# 5. Identify if there are any outliers.
# A: Yes. There are several outliers.

# 6. Create at least 2 new variables.
# Create a new variable called Total_Bathrooms
housing_df$Total_Bathrooms <- housing_df$bath_full_count + 
    housing_df$bath_half_count + housing_df$bath_3qtr_count

# Create a new variable called Price_Per_Sqft
housing_df$Price_Per_Sqft <- housing_df$Sale_Price / 
    housing_df$square_feet_total_living

# Check dataset with the new variables
str(housing_df)
head(housing_df)
