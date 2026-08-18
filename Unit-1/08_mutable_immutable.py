""" Program to demonstrate mutable and immutable objects """

numbers = [10, 20, 30]

print("Original List:", numbers)

numbers[0] = 100

print("Modified List:", numbers)

number = 10

print("\nOriginal Integer:", number)

number = number + 5

print("Modified Integer:", number)


name = "Python"

print("\nOriginal String:", name)

name = name + " Programming"

print("Modified String:", name)