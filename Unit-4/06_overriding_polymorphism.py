# Program to demonstrate method overriding and polymorphism

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Creating objects
a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()

OUTPUT
Animal makes sound
Dog barks
Cat meows
