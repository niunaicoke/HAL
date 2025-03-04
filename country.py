import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = '/home/yulab/Desktop/HAL review paper.xlsx'

# Read the "Completed Reviews" sheet from the Excel file
df = pd.read_excel(file_path, sheet_name='Completed Reviews')

# Count the distribution of 'Region of majority author' values
country_distribution = df['Region of majority author'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(16, 16))
plt.pie(country_distribution, labels=country_distribution.index, autopct='%1.1f%%', startangle=250)
plt.title('Distribution of Papers by Region of Majority Author')

# Show the pie chart
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is a circle.
plt.show()

# Optionally, print the distribution with percentages
print("Country Distribution with Percentages:")
print(country_distribution)
