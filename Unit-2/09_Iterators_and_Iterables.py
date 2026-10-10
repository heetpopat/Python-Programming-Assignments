
# Demonstrate iterables and iterators

numbers = [10, 20, 30, 40]

# A list is an iterable
print("Iterable:", numbers)

# Create an iterator
iterator = iter(numbers)

# Retrieve values using next()
print("Iterator values:")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Iterate using a for loop
print("Using for loop:")
for number in numbers:
    print(number)
