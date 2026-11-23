# Program to demonstrate try, except, else and finally

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")

else:
    print("Result:", result)

finally:
    print("Program completed")

OUTPUT

Enter first number: 10
Enter second number: 2
Result: 5.0
Program completed
