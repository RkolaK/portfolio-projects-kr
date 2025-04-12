# Author: KR
# Date: 2023-06-30

# Load packages
library(ggplot2)
theme_set(theme_minimal())

# Set the working directory
setwd("/Users/kleberroncoletta/RStudio_Projects")

# Load the dataset to scores_df
scores_df <- read.csv("data/scores.csv")

# 1. What are the observational units in this study? 
# A: 38 individual rows with student scores.
nrow(scores_df)
ncol(scores_df)

# 2.Identify the variables mentioned in the narrative paragraph and determine 
# which are categorical and quantitative?
# A: Count: Quantitative, Score: Quantitative, Section: Categorical
str(scores_df)

# 3.Create one variable to hold a subset of your data set that contains only the 
# Regular Section and one variable for the Sports Section.
regular_section <- subset(scores_df, Section == "Regular")
sports_section <- subset(scores_df, Section == "Sports")

# 4. Use the Plot function to plot each Sections scores and the number of students 
# achieving that score. Use additional Plot Arguments to label the graph and give 
# each axis an appropriate label. 
# Plot for Regular section
plot(regular_section$Score, regular_section$Count, 
     xlab = "Score", ylab = "Number of Students",
     main = "Students scores in Regular Section",
     pch = 16, col = "blue")

# Plot for Sports section
plot(sports_section$Score, sports_section$Count, 
     xlab = "Score", ylab = "Number of Students",
     main = "Students scores in Sports Section",
     pch = 16, col = "red")

# Once you have produced your Plots answer the following questions:
#    1. Comparing and contrasting the point distributions between the two section, 
#    looking at both tendency and consistency: Can you say that one section tended 
#    to score more points than the other? Justify and explain your answer.
#    A: The mean and the median scores of the Regular Section is higher than the 
#    mean and the median scores of the Sports Section. This suggests a tendency
#    for the Regular Section to have higher scores on average compared to the
#    Sports Section.
mean(regular_section$Score)
median(regular_section$Score)

mean(sports_section$Score)
median(sports_section$Score)

#    2. Did every student in one section score more points than every student in 
#    the other section? If not, explain what a statistical tendency means in this 
#    context.
#    A: No. In this context, statistical tendency means that on average, the scores
#    of the Regular Section tend to be higher than those of the Sports Section.
#    However we can see that there are some students who scored higher in the 
#    Sports Section.
combined_data <- rbind(data.frame(Section = "Regular", regular_section),
                       data.frame(Section = "Sports", sports_section))

ggplot(data = combined_data, aes(x = Section, y = Score)) +
    geom_boxplot() +
    labs(x = "Section", y = "Score",
         title = "Regular vs. Sports Sections")

#    3. What could be one additional variable that was not mentioned in the 
#    narrative that could be influencing the point distributions between the two 
#    sections?
#    A: I think "Study habits" could be one additional variable. Students with
#    more effective study habits might perform better regardless of the section
#    that they are in.
