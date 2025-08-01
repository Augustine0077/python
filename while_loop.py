#exicute a stament while a condition is true
name = input("Enter your name :")
#while name == "":
if name == "":
    print("You entered a blank name. Please try again.")
    name = input("Enter your name :") 
print(f"Hello, {name}!")  # Output: Hello, [name]   