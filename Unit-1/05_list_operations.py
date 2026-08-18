""" Write a program to create and manipulate lists using indexing slicing and list comprehensions. """

numbers = [10,20,30,40,50]

print("Original List: ",numbers)

#inexing
print("\nIndexing:")
print("First element:",numbers[0])
print("Third element:",numbers[2])
print("Last element:",numbers[-1])

#slicing
print("\nSlicing:")
print("First three elements:",numbers[:3])
print("Elements from index 2: ",numbers[2:])
print("Elements from index 1 to 3:",numbers[1:4])

#Manipulating the list
numbers.append(60)
numbers.remove(20)

print("\nAfter Manipulation:")
print("List:",numbers)

squares = [i ** 2 for i in numbers]

print("\nList Comprehension:")
print("Squares:",squares)




