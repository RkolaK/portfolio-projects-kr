# Author: KR
# Date: 2023-06-24

# Load packages
library(ggplot2)
library(pastecs)
theme_set(theme_minimal())

# Set the working directory
setwd("/Users/kleberroncoletta/RStudio_Projects")

# Load the dataset to survey_df
survey_df <- read.csv("data/acs-14-1yr-s0201.csv")

# Provide the following:
# 1. What are the elements in your data?
#    Id: Unique identifier. Data type: Character
#    Id2: Unique identifier. Data type: Integer
#    Geography: Name of the county and state. Data type: Character
#    PopGroupID: Identifier for the population group. Data type: Integer
#    POPGROUP.display.label: Label for population group. Data type: Character
#    RacesReported: Number of races reported. Data type: Integer
#    HSDegree: % of individuals with a high school degree. Data type: Numeric
#    BachDegree: % of individuals with a bachelor's degree. Data type: Numeric
head(survey_df)

# 2. Please provide the output from the following functions: str(); nrow(); ncol()
str(survey_df)
nrow(survey_df)
ncol(survey_df)

# 3. Create a Histogram of the HSDegree variable using the ggplot2 package.
#   1. Set a bin size for the Histogram.
#   2. Include a Title and appropriate X/Y axis labels on your Histogram Plot.
ggplot(survey_df, aes(x = HSDegree)) + geom_histogram(binwidth = 5) +
    ggtitle("High School Degrees") + xlab("Percentage of High School Degrees") + 
    ylab("Frequency")

# 4. Answer the following questions based on the Histogram produced:
#   1. Based on what you see, is the data distribution unimodal? A: Yes.
#   2. Is it approximately symmetrical? A: No.
#   3. Is it approximately bell-shaped? A: No.
#   4. Is it approximately normal? A: No.
#   5. If not normal, is the distribution skewed? If so, in which direction? A:
#   It is a negatively skewed distribution.
#   6. Include a normal curve to the Histogram that you plotted. A: See below.
#   7. Explain whether a normal distribution can accurately be used as a model
#   for this data. A: No. If the histogram shows a negatively distribution, it
#   suggests that the data is not normally distributed and in this case, it's 
#   more appropriate to have another model that better capture the characteristics
#   of the data.
#  Adding a normal curve (Question 4.6):
mean_hs <- mean(survey_df$HSDegree)
sd_hs <- sd(survey_df$HSDegree)

ggplot(survey_df, aes(x = HSDegree)) + geom_histogram(
    aes(y = ..density..), fill = "blue", color = "white", alpha = 0.5) +
    stat_function(fun = dnorm, args = list(mean = mean_hs, sd = sd_hs),
    color = "black", linetype = "dashed", size = 1) +
    ggtitle("High School Degrees") + xlab("HSDegree") + ylab("Density")

# 5. Create a Probability Plot of the HSDegree variable.
ggplot(survey_df, aes(sample = HSDegree)) + stat_qq() + stat_qq_line(color = "red") +
    labs(title = "Probability Plot - HSDegree",
         x = "Theoretical Quantiles", y = "Sample Quantiles")

# 6. Answer the following questions based on the Probability Plot:
#    1. Based on what you see in this probability plot, is the distribution 
#    approximately normal? Explain how you know. A: No. The curvature suggests
#    the distribution is not normal. Also, it is easy to see outliers showing 
#    the presence of unusual data. 
#    2. If not normal, is the distribution skewed? If so, in which direction? 
#    Explain how you know. A: It is a negatively skewed distribution. The
#    Probability plot show a downward curvature away from the reference line
#    towards the lower values.

# 7. Now that you have looked at this data visually for normality, you will now 
#    quantify normality with numbers using the stat.desc() function. Include a 
#    screen capture of the results produced.
stat.desc(survey_df$HSDegree, basic=TRUE, desc=TRUE, norm=TRUE, p=0.95)
# z_scores <- scale(survey_df$HSDegree)
# z_scores

# 8. In several sentences provide an explanation of the result produced for skew, 
#    kurtosis, and z-scores. In addition, explain how a change in the sample size 
#    may change your explanation?
#    A: A skewness value close to zero suggests approximate symmetry. In this case,
#    a skewness of -1.67 indicates a moderately strong negative skew in the
#    distribution. It suggests that the majority of the data points are concentrated
#    towards the higher values.
#    Kurtosis measures the shape of the distribution's tails. Positive kurtosis
#    indicates heavy tails and negative kurtosis suggests lighter tails. A
#    kurtosis value of zero corresponds to the normal distribution. In our example,
#    the kurtosis value of 4.35 indicates that the distribution has a relatively 
#    high degree of peakedness and heavy tails compared to a normal distribution.
#    The z-scores represent the standardized values of each data point in relation 
#    to the mean and standard deviation of the distribution. A positive z-score 
#    indicates that a data point is above the mean, while a negative z-score 
#    indicates it is below the mean.
#    Regarding the sample size, a change in the sample size may influence the 
#    interpretation of these results. A larger sample size generally provides more 
#    reliable estimates of skewness, kurtosis, and z-scores, reducing the impact of 
#    sampling variability. 
