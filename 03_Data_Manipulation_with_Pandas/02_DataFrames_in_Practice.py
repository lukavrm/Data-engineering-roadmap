import pandas as pd

# WHAT IS A DATAFRAME?

""" Think of a dataframe as a spreadsheet in memory:
- Rows and columns
- Column labels
- Data types in each column """

# CREATING DATAFRAMES MANUALLY

customer_data = {
    "name": ["Ana", "Bruno", "Carlos"],
    "age": [25, 30, 22],
    "city": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"],
}

df_customers = pd.DataFrame(customer_data)

print("Customer dataframe created manually:")
print(df_customers)

# It is also possible to create one from a list of dictionaries:

product_data = [
    {"Product": "Laptop", "price": 3500.0},
    {"Product": "Mouse", "price": 80.0},
    {"Product": "Keyboard", "price": 150.0},
]

df_products = pd.DataFrame(product_data)

print("\nProduct DataFrame (list of dictionaries):")
print(df_products)

# READING DATA FROM FILES (CSV / EXCEL)

print("\nReading CSV file:")
df_csv = pd.read_csv("02.1_Lista.csv") # Make sure the CSV file is in the same directory as this script or provide the full path.
print("\nFirst rows of the CSV:")
print(df_csv.head())

df_excel = pd.read_excel("pessoas_50.xlsx") # Make sure the Excel file is in the same directory as this script or provide the full path.
print("\nFirst rows of the Excel file:")
print(df_excel.head())