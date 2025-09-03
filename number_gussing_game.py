import random


num1=1
num2=5
number = random.randint(num1,num2)
print(number)
while True:
    guess =int(input(f"Guess a number between {num1} and {num2}: "))
    if number == guess:
        print("You got it right!")
        break
    else:
        print(f"Sorry, the correct number was {number}.")