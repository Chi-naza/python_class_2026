import os

# Check if we're in the right directory
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the 'analysis_with_python' folder!")




# Working With Files
import pandas as pd
import json
import os

# Read the CSV file
df = pd.read_csv('data/sales.csv')
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Create output directory
os.makedirs('output', exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
df.to_json('output/sales_data.json', orient='records', indent=2)

# 2. Excel format (good for sharing)
df.to_excel('output/sales_data.xlsx', index=False)

# 3. Updated CSV (with our new total column)
df.to_csv('output/sales_with_totals.csv', index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")



# Loading different File Types
# CSV
df_csv = pd.read_csv('output/sales_with_totals.csv')
print("Loaded CSV Data:")
print(df_csv)

# JSON
df_json = pd.read_json('output/sales_data.json')
print("Loaded JSON Data:")
print(df_json)

# or for simple JSON:
with open('output/sales_data.json', 'r') as f:
    data = json.load(f)
print("Loaded JSON Data 2:")
print(data)

# Excel
df_excel = pd.read_excel('output/sales_data.xlsx')
print("Loaded Excel Data:")
print(df_excel)

# Text files
with open('output/test_file.txt', 'r') as f:
    text = f.read()

print("Loaded Text Data:")  
print(text)