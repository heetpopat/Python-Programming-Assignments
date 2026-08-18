""" Program to demonstrate dictionary methods and iteration """

student = {
    "name": "Heet",
    "age": 22,
    "course": "MCA"
}

print("Original Dictionary:", student)


print("\nName:", student["name"])


student["city"] = "Ahmedabad"


student["age"] = 23

print("\nAfter Adding and Updating:")
print(student)

# Dictionary methods
print("\nDictionary Methods:")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


student.pop("city")

print("\nAfter Removing City:")
print(student)


print("\nDictionary Iteration:")
for key, value in student.items():
    print(key, ":", value)