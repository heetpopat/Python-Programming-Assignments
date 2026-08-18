""" Program to demonstrate recursion using Fibonacci series """

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


terms = 7

print("Fibonacci Series:")

for i in range(terms):
    print(fibonacci(i), end=" ")