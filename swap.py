#This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.
# There are two variables, a and b from input
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

temp = a
a = b
b = temp

print("After swapping:")
print("a: " + a)
print("b: " + b)
