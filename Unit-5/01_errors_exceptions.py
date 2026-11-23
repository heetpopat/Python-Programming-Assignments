# Program to demonstrate different errors and exceptions

# ZeroDivisionError
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# ValueError
try:
    num = int("abc")
except ValueError:
    print("Invalid value")

# TypeError
try:
    result = 10 + "Hello"
except TypeError:
    print("Cannot add integer and string")

# IndexError
try:
    arr = [10, 20, 30]
    print(arr[5])
except IndexError:
    print("Index out of range")

OUTPUT

Cannot divide by zero
Invalid value
Cannot add integer and string
Index out of range
