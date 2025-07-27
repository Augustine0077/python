num1 = int(input("Enter first number: "))

print("Choose an operator ( +,- , *,/)")
print("for '+' enter = 1\n for '-' enter = 2\n for '*' enter = 3\n for '/' enter = 4\n")

operator = input("Enter operator: ")
num2 = int(input("Enter second number: "))

if operator == "1":
    result = num1 + num2
    print(f"answer  = {result}")
elif operator == "2":
    result = num1 - num2
    print(f"answer  = {result}")
elif operator == "3":
    result = num1 * num2
    print(f"answer  = {result}")
elif operator == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"answer  = {result}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
