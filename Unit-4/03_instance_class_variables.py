# Program to demonstrate instance and class variables

class Student:
    college = "Marwadi University"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("College:", Student.college)

s1 = Student("Amit", 1)
s2 = Student("Neha", 2)

s1.display()
print()

s2.display()

OUTPUT
Name: Amit
Roll Number: 1
College: Marwadi University

Name: Neha
Roll Number: 2
College: Marwadi University
