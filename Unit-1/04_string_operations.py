""" Write a program to demonstrate string operations including slicing formatting and build-in string functions. """

text = "Python Programming"

#string slicing
print("Original String:",text)
print("First 6 Characters:",text[:6])
print("Characters from index 7:",text[7:])
print("Characters from index 0 to 5:",text[0:6])

#string formatting
name = "Heet"
language = "Python"
age = 21
city = "Rajkot"

print("\nString Formatting:")
print("My name is {} and I am learning {}.".format(name, language))
print("\n I am Learning {} because ahead i want to contribute in ai ml project in gsoc".format(language))
print("\n I am {} years old and i live in {}".format(age,city))

#Build-in string functions
print("\nBuild-in String Functions:")
print("Length:",len(text))
print("Uppercase:",text.upper())
print("Lowercase:",text.lower())
print("Replace:",text.replace("Python","Java"))
print("Find 'Programming':", text.find("Programming"))
print("Count of 'm':",text.count("m"))
print("count of 'p':",text.count("p"))
