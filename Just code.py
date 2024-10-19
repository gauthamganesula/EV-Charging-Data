import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path_new = '/mnt/data/ev_charging_patterns.csv'
data_check_new = pd.read_csv(file_path_new)

# 1. Histogram of Energy Consumed (kWh)
plt.figure(figsize=(10, 6))
plt.hist(data_check_new['Energy Consumed (kWh)'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Energy Consumed (kWh)')
plt.xlabel('Energy Consumed (kWh)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 2. Scatter plot of Energy Consumed vs Battery Capacity
plt.figure(figsize=(10, 6))
plt.scatter(data_check_new['Battery Capacity (kWh)'], data_check_new['Energy Consumed (kWh)'], color='green', alpha=0.6)
plt.title('Energy Consumed vs Battery Capacity (kWh)')
plt.xlabel('Battery Capacity (kWh)')
plt.ylabel('Energy Consumed (kWh)')
plt.grid(True)
plt.show()

# 3. Scatter plot of Charging Duration vs Energy Consumed
plt.figure(figsize=(10, 6))
plt.scatter(data_check_new['Charging Duration (hours)'], data_check_new['Energy Consumed (kWh)'], color='green', alpha=0.6)
plt.title('Energy Consumed vs Charging Duration (hours)')
plt.xlabel('Charging Duration (hours)')
plt.ylabel('Energy Consumed (kWh)')
plt.grid(True)
plt.show()

# 4. Boxplot of Charging Cost by Vehicle Model (if Vehicle Model exists)
if 'Vehicle Model' in data_check_new.columns:
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Vehicle Model', y='Charging Cost (USD)', data=data_check_new)
    plt.title('Charging Cost by Vehicle Model')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# 5. Correlation heatmap for numerical features
numeric_data_check_new = data_check_new.select_dtypes(include=[np.number])
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_data_check_new.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
