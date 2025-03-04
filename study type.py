import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = '/home/yulab/Desktop/HAL review paper.xlsx'

# Read the "Completed Reviews" sheet from the Excel file
df = pd.read_excel(file_path, sheet_name='Completed Reviews')

# Normalize the 'Journal' column to lowercase
df['study type: lab experiment, field observations, intervention (lab), intervention (field), retrospective data analysis, conceptual (no new data)'] = df['study type: lab experiment, field observations, intervention (lab), intervention (field), retrospective data analysis, conceptual (no new data)'].str.lower()

# Count the distribution of 'Journal' values
journal_distribution = df['study type: lab experiment, field observations, intervention (lab), intervention (field), retrospective data analysis, conceptual (no new data)'].value_counts()


list =['lab experiment', 'field observations', 'intervention (lab)', 'intervention (field)', 'retrospective data analysis', 'conceptual']





# Plotting the pie chart
plt.figure(figsize=(16, 16))
plt.pie(journal_distribution, labels=journal_distribution.index, autopct='%1.1f%%', startangle=250)
plt.title('Distribution of Papers by Journal')

# Show the pie chart
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is a circle.
plt.show()

# Optionally, print the distribution with percentages
print("Journal Distribution with Percentages:")
print(journal_distribution)
