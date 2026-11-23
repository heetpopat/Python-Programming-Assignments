# Program to demonstrate MRO and magic methods

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

# Creating object
obj = D()

obj.show()

# Display Method Resolution Order
print(D.mro())

# Magic method demonstration
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student Name: " + self.name

s1 = Student("Amit")

print(s1)

OUTPUT
Class B
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
Student Name: Amit
