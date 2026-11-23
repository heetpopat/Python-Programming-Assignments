# Program to demonstrate constructor and destructor

class Student:
    def __init__(self):
        print("Constructor called")
        print("Student object created")

    def __del__(self):
        print("Destructor called")
        print("Student object destroyed")

# Creating object
s1 = Student()

# Deleting object
del s1


OUTPUT
Constructor called
Student object created
Destructor called
Student object destroyed
