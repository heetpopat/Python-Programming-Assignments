
# Demonstrate list, dictionary, and set comprehensions

# List comprehension: squares of numbers
squares = [x ** 2 for x in range(1, 6)]
print("List comprehension:", squares)

# Dictionary comprehension: number and its square
square_dict = {x: x ** 2 for x in range(1, 6)}
print("Dictionary comprehension:", square_dict)

# Set comprehension: unique squares
square_set = {x ** 2 for x in range(1, 6)}
print("Set comprehension:", square_set)
