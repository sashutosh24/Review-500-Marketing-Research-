import pandas as pd

# Load the dataset
file_path = '/mnt/data/Review500.xlsx'
data = pd.read_excel(file_path)

# Calculate Content Analysis Metrics
content_analysis = pd.DataFrame({
    "ProfileName": data['ProfileName'],
    "Score": data['Score'],
    "Helpfulness": data['HelpfulnessNumerator'].astype(str) + "/" + data['HelpfulnessDenominator'].astype(str),
    "Text": data['Text']
})

# Save the Content Analysis results to a new Excel file
output_file_path = '/mnt/data/Content_Analysis.xlsx'
content_analysis.to_excel(output_file_path, index=False)

print(f"Content Analysis saved to: {output_file_path}")
