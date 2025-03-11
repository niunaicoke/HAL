import pandas as pd
import matplotlib.pyplot as plt

# File path
file_path = "/Users/scottliu/Desktop/HAL review paper.xlsx"
sheet_name = "Completed Reviews"
column_name = "Year"

# Load the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Extract the "Year" column
years = df[column_name].dropna().astype(int)  # Remove NaNs and ensure integers

# Plot the histogram
plt.figure(figsize=(10, 5))
plt.hist(years, bins=range(1988, 2024), edgecolor='black', alpha=0.7)

# Labels and title
plt.xlabel("Year")
plt.ylabel("Number of papers")
plt.title("Histogram of papers by Year")
plt.xticks(range(1988, 2024), rotation=45)  # Ensure all years are labeled

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot as an image (PNG format)
image_path = "/Users/scottliu/Desktop/histogram.png"
plt.savefig(image_path, dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

print(f"Histogram saved as {image_path}")
