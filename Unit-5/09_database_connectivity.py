# Program to connect Python with database and execute SQL queries

import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    rollno INTEGER,
    name TEXT,
    marks INTEGER
)
""")

# Insert records
cursor.execute("INSERT INTO students VALUES (1, 'Amit', 78)")
cursor.execute("INSERT INTO students VALUES (2, 'Neha', 85)")
cursor.execute("INSERT INTO students VALUES (3, 'Rahul', 65)")

# Execute SQL query
cursor.execute("SELECT * FROM students")

# Display records
records = cursor.fetchall()

print("Student Records:")

for record in records:
    print(record)

# Save changes
conn.commit()

# Close connection
conn.close()



OUTPUT
Student Records:
(1, 'Amit', 78)
(2, 'Neha', 85)
(3, 'Rahul', 65)
