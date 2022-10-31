# input("enter the number :")
num1 = input("enter the number :")
num2 = input("enter the second number :")
print(type(num1), type(num2)) # any inputs provided at the console are considered as strings-hence addition will concanete the values
#there by convert the input values by function int, which will firt take the  string data and then int function convert and store  it in to the num1 as int value datatype

# print(num1, num2)
# print(num1+num2)
tot = int(num1) + int(num2) # convert the string to int
print(tot)
print(type(tot))

##### approach 2 : both are strings

