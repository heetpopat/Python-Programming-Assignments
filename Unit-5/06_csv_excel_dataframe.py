# Program to create DataFrame from CSV and Excel files

import pandas as pd

# Reading CSV file
df_csv = pd.read_csv("students.csv")

print("CSV Data:")
print(df_csv)

# Reading Excel file
df_excel = pd.read_excel("students.xlsx")

print("\nExcel Data:")
print(df_excel)
