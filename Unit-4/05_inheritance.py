# Program to demonstrate single, multilevel and multiple inheritance

# Single inheritance
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def display(self):
        print("Child class")

# Multilevel inheritance
class Grandchild(Child):
    def message(self):
        print("Grandchild class")

# Multiple inheritance
class Father:
    def father_method(self):
        print("Father class")

class Mother:
    def mother_method(self):
        print("Mother class")

class Son(Father, Mother):
    def son_method(self):
        print("Son class")

# Single inheritance
c = Child()
c.show()
c.display()

print()

# Multilevel inheritance
g = Grandchild()
g.show()
g.display()
g.message()

print()

# Multiple inheritance
s = Son()
s.father_method()
s.mother_method()
s.son_method()


OUTPUT
Parent class
Child class

Parent class
Child class
Grandchild class

Father class
Mother class
Son class
