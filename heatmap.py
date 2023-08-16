import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "./known_exploited_vulnerabilities.csv" # Replace with the path to your dataset
data = pd.read_csv(file_path)

# Convert date columns to datetime
data['dateAdded'] = pd.to_datetime(data['dateAdded'], errors='coerce')
data['dueDate'] = pd.to_datetime(data['dueDate'], errors='coerce')

# Analyzing the number of vulnerabilities per vendor/project
vendor_vulnerabilities = data['vendorProject'].value_counts()

# Analyzing the number of vulnerabilities per product
product_vulnerabilities = data['product'].value_counts()

# Create a pivot table of the frequency of vulnerabilities for each vendor/project and product
pivot_table = pd.pivot_table(data, values='cveID', index='vendorProject', columns='product', aggfunc='count', fill_value=0)

# Filter the pivot table to only include the top 20 vendors/projects and top 10 products with the most vulnerabilities
top_vendors = vendor_vulnerabilities.index[:20]
top_products = product_vulnerabilities.index[:20]
filtered_pivot_table = pivot_table.loc[top_vendors, top_products]

# Create the heatmap
plt.figure(figsize=(16, 8))
sns.heatmap(filtered_pivot_table, cmap='Blues', annot=True, fmt='d')
plt.title('Heatmap of Vulnerabilities by Vendor/Project and Product')
plt.xlabel('Product')
plt.ylabel('Vendor/Project')

# Save the plot as a PDF
output_path = "heatmap.pdf" # Replace with your desired output path
plt.savefig(output_path, format='pdf', bbox_inches='tight')

plt.show()
