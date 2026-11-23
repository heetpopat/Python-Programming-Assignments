# Program to handle missing data using dropna() and fillna()

import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya"],
    "Marks": [78, None, 65, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove missing values
print("\nAfter dropna():")
print(df.dropna())

# Fill missing values
print("\nAfter fillna():")
print(df.fillna(0))


OUTPUT

Original Data:
    Name  Marks
0   Amit   78.0
1   Neha    NaN
2  Rahul   65.0
3  Priya    NaN

After dropna():
    Name  Marks
0   Amit   78.0
2  Rahul   65.0

After fillna():
    Name  Marks
0   Amit   78.0
1   Neha    0.0
2  Rahul   65.0
3  Priya    0.0
