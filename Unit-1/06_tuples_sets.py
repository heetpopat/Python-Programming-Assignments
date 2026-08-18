""" To write and execute a Python program to demonstrate the use of tuples and sets with basic operations. """

numbers = (10,20,30,40,50)

print("Tuple:",numbers)

print("\n Tuple Operations:")
print("First element:",numbers[0])
print("Last element:",numbers[-1])
print("Length of tuple:",len(numbers))

print("Tuple slicing:",numbers[1:4])

set1 = {10,20,30,40}
set2 = {30,40,50,60}

print("\nSet Operations:")
print("Set 1:",set1)
print("Set 2:",set2)

set1.add(70)
print("After adding 70:",set1)

set1.remove(20)
print("After removing 20:",set1)

print("Union:",set1.union(set2))

print("Intersection:",set1.intersection(set2))

print("Difference:",set1.difference(set2))


