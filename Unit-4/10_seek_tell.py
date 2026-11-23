# Program to demonstrate seek() and tell()

f = open("sample.txt", "w")
f.write("Python Programming")
f.close()

f = open("sample.txt", "r")

# Display current position
print("Current position:", f.tell())

# Read first 6 characters
print("Data:", f.read(6))

# Display current position
print("Current position:", f.tell())

# Move pointer to position 0
f.seek(0)

# Read entire file
print("Full data:", f.read())

f.close()

OUTPUT

Current position: 0
Data: Python
Current position: 6
Full data: Python Programming
