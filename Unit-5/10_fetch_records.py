# Program to retrieve records using fetchone, fetchmany and fetchall

import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    rollno INTEGER,
    name TEXT,
    marks INTEGER
)
""")

# Insert data only if table is empty
cursor.execute("SELECT COUNT(*) FROM students")

if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO students VALUES (1, 'Amit', 78)")
    cursor.execute("INSERT INTO students VALUES (2, 'Neha', 85)")
    cursor.execute("INSERT INTO students VALUES (3, 'Rahul', 65)")
    cursor.execute("INSERT INTO students VALUES (4, 'Priya', 92)")
    cursor.execute("INSERT INTO students VALUES (5, 'Karan', 55)")

conn.commit()

# fetchone()
cursor.execute("SELECT * FROM students")

print("Using fetchone():")
print(cursor.fetchone())

# fetchmany()
cursor.execute("SELECT * FROM students")

print("\nUsing fetchmany():")
print(cursor.fetchmany(2))

# fetchall()
cursor.execute("SELECT * FROM students")

print("\nUsing fetchall():")
print(cursor.fetchall())

conn.close()


OUTPUT
Using fetchone():
(1, 'Amit', 78)

Using fetchmany():
[(1, 'Amit', 78), (2, 'Neha', 85)]

Using fetchall():
[(1, 'Amit', 78), (2, 'Neha', 85), (3, 'Rahul', 65), (4, 'Priya', 92), (5, 'Karan', 55)]
