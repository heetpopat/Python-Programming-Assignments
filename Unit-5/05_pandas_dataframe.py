# Program to perform basic data analysis using Pandas DataFrame

import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [78, 85, 65, 92]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())


OUTPUT
Student Data:
    Name  Age  Marks
0   Amit   20     78
1   Neha   21     85
2  Rahul   19     65
3  Priya   22     92

Average Marks:
80.0

Highest Marks:
92

Lowest Marks:
65
