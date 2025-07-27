num1=int(input("Enter first number: "))

print("Choose an operator ( +,- , *,/)")

print("for '+' enter = 1\n for '-' enter = 2\n for '*' enter = 3\n for '/' enter = 4\n")

operator=input("Enter operator: ")

num2=int(input("Enter second number: "))
sum = 0

if operator == "1":
    sum = num1+num2
if operator == "2":
    sum = num1-num2
if operator == "3":
    sum = num1*num2
if operator == "4":
    if num2 != 0:
        sum = num1/num2
    else:
        print("Cannot divide by zero")
        exit()


print(f"answer  = {sum}")
else:
    print("Invalid operator")
