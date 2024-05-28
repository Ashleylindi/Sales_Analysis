import pandas as pd

# Load the data
data = pd.read_excel('sales_data.xlsx', engine='openpyxl')
print(data)

# Data processing tasks
# Add your code here

# Calculate total sales
data['Total Sales'] = data['Quantity Sold'] * data['Unit Price']

# Extract month and year from the date
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# Group by month and year to get monthly sales
monthly_sales = data.groupby(['Year', 'Month'])['Total Sales'].sum().reset_index()

# Get top-selling products
top_products = data.groupby('Product')['Total Sales'].sum().nlargest(10).reset_index()