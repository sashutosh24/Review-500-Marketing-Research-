import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/Review500.xlsx'
data = pd.read_excel(file_path)

# Convert the Time column (UNIX timestamp) to a readable datetime format
data['Time'] = pd.to_datetime(data['Time'], unit='s')

# Extract the year and month for grouping
data['Year-Month'] = data['Time'].dt.to_period('M')

# Group by Year-Month and calculate the average Score
average_score_trend = data.groupby('Year-Month')['Score'].mean()

# Plotting the trend
plt.figure(figsize=(12, 6))
plt.plot(average_score_trend.index.astype(str), average_score_trend.values, marker='o', color='orange')

# Add titles and labels
plt.title('Trend of Average Review Scores Over Time', fontsize=14)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Average Review Score', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()
