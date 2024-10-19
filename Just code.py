import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = 'ev_charging_patterns.csv'
data = pd.read_csv(file_path) 

# 1. Histogram of Energy Consumed (kWh)
plt.figure(figsize=(10, 6))
plt.hist(data['Energy Consumed (kWh)'], bins=20, color='skyblue', edgecolor='black')  
plt.title('Distribution Of Energy Consumed (kWh)')
plt.xlabel('Energy Consumed (kWh)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 2. Scatter plot of Energy Consumed vs Battery Capacity
plt.figure(figsize=(10, 6))
plt.scatter(data['Battery Capacity (kWh)'], data['Energy Consumed (kWh)'], color='green', alpha=0.6)  
plt.title('Energy Consumed vs Battery Capacity (kWh)')
plt.xlabel('Battery Capacity (kWh)')
plt.ylabel('Energy Consumed (kWh)')
plt.grid(True)
plt.show()

# 3. Scatter plot of Charging Duration vs Energy Consumed
plt.figure(figsize=(10,6))
plt.scatter(data['Charging Duration (hours)'], data['Energy Consumed (kWh)'],color='green',alpha=0.6)
plt.title('Charging Duration (hours)')
plt.grid(True)
plt.show()

# 4. Boxplot of Charging Cost by Vehicle Model (if Vehicle Model exists)
if'Vehicle Model' in data.columns:
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Vehicle Model', y='Charging Cost (USD)', data=data)  
    plt.title('Charging Cost by Vehicle Model')
    plt.xticks(rotation=45)  
    plt.grid(True)
    plt.show()

# 5. Correlation heatmap for numerical features
numeric_data = data.select_dtypes(include=[np.number])
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
