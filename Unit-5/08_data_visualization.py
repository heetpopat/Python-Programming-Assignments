# Program to plot line, bar, histogram and pie charts

import matplotlib.pyplot as plt

names = ["Amit", "Neha", "Rahul", "Priya"]
marks = [78, 85, 65, 92]

# Line Chart
plt.plot(names, marks, marker="o")
plt.title("Student Marks - Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.bar(names, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Histogram
plt.hist(marks, bins=5)
plt.title("Marks Distribution - Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Pie Chart
plt.pie(marks, labels=names, autopct="%1.1f%%")
plt.title("Student Marks - Pie Chart")
plt.show()
