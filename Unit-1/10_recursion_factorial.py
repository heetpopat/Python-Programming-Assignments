""" Program to demonstrate recursion using factorial """

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5

result = factorial(number)

print("Number:", number)
print("Factorial:", result)