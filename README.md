# EV-Charging-Data
In this project, I analyzed a dataset from Kaggle that contains electric vehicle (EV) charging data, exploring key factors such as energy consumption, battery capacity, and charging duration. The dataset was cleaned, missing values were handled, and visualizations were generated to identify patterns and relationships between various factors. 

Key Analyses and Findings:

Distribution of Energy Consumed:

A histogram of energy consumption showed that most EV charging sessions fall between 20 and 60 kWh, with a peak around 40 kWh. Sessions consuming more than 80 kWh were rare, indicating that typical energy consumption remains moderate for most charging events.

Scatter Plot Analysis:

Energy Consumed vs Battery Capacity: The scatter plot showed a weak positive correlation, where larger battery capacities tended to consume more energy, though the relationship was not very strong.

Charging Duration vs Energy Consumed: Longer charging sessions were generally associated with higher energy consumption, with most sessions lasting between 1 and 4 hours, though there were outliers.

Boxplot of Charging Cost by Vehicle Model:

The boxplot revealed that most vehicle models had a median charging cost between 20 and 30 USD. However, Hyundai Kona and Tesla Model 3 showed a wider range of costs, with some outliers reaching up to 70 USD, likely due to longer charging sessions or high energy consumption.

Correlation Heatmap:

The correlation heatmap demonstrated weak correlations between most variables, indicating that factors like battery capacity, vehicle age, and charging duration have only minor impacts on energy consumption and cost. Other factors not present in the dataset may influence charging behavior.



Conclusion:

This project provided valuable insights into typical EV charging behaviors, with moderate energy consumption being the norm across different vehicle models and charging sessions. While some outliers in charging costs and durations were observed, the overall pattern remains consistent. The weak correlations indicate that no single factor dominates the EV charging process, and further exploration of other variables may be necessary to deepen our understanding of EV charging behavior.
