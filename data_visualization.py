import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_excel('sales_data.xlsx', engine='openpyxl')
print(data)

# Data visualization tasks
# Add your code here

# Bar chart for sales by product
plt.figure(figsize=(10, 6))
sales_by_product = data.groupby('Product')['Quantity Sold'].sum().reset_index()
plt.bar(sales_by_product['Product'], sales_by_product['Quantity Sold'])
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.show()

# Histogram for unit price distribution
plt.figure(figsize=(10, 6))
plt.hist(data['Unit Price'], bins=10, color='skyblue', edgecolor='black')
plt.title('Unit Price Distribution')
plt.xlabel('Unit Price')
plt.ylabel('Frequency')
plt.show()