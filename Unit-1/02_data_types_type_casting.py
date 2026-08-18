"""Program 02:- Write a Program to demonstrate different data types and type casting """
integer_value = 25 
float_value = 10.5
string_value = "50"
boolean_value = True

print("Integer value: ",integer_value)
print("Float Value: ", float_value)
print("String Value: ", string_value)
print("Boolean Value: ",boolean_value)

converted_integer = int(string_value)
converted_float = float(integer_value)
converted_string = str(integer_value)

print("\nAfter Type Casting: ")
print("String to Integer:", converted_integer)
print("Integer to Float:",converted_float)
print("Integer to String:",converted_string)