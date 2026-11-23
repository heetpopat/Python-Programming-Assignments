# Program to demonstrate user-defined exception

class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("You must be 18 or older")

    print("You are eligible")

except AgeError as e:
    print("Error:", e)

OUTPUT

Enter your age: 16
Error: You must be 18 or older
