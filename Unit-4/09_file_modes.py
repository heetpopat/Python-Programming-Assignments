# Program to read and write data using different file modes

# Write mode
f = open("student.txt", "w")
f.write("Hello Python\n")
f.write("File handling practical\n")
f.close()

# Read mode
f = open("student.txt", "r")
print("File contents:")
print(f.read())
f.close()

# Append mode
f = open("student.txt", "a")
f.write("This is appended text\n")
f.close()

# Read updated file
f = open("student.txt", "r")
print("Updated contents:")
print(f.read())
f.close()

OUTPUT

File contents:
Hello Python
File handling practical

Updated contents:
Hello Python
File handling practical
This is appended text
