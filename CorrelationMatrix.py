import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/mnt/data/Review500.xlsx'
data = pd.read_excel(file_path)

# Select relevant numerical columns for correlation analysis
numerical_data = data[['HelpfulnessNumerator', 'HelpfulnessDenominator', 'Score']]

# Calculate the correlation matrix
correlation_matrix = numerical_data.corr()

# Plotting the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Add titles and labels
plt.title('Correlation Matrix of Review Data', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Display the heatmap
plt.tight_layout()
plt.show()
