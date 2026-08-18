""" Program to demonstrate user-defined functionswith different types of arguments """

def add(a, b):
    return a + b

print("Addition:", add(10, 20))


def greet(name="Student"):
    print("Hello,", name)

greet()
greet("Heet")


def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=22, name="Heet")


def total(*numbers):
    return sum(numbers)

print("Total:", total(10, 20, 30, 40))