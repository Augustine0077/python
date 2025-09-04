import random
lowest_number=1
highest_number =100
answer = random.randint(lowest_number,highest_number)
guesses = 0
is_running = True
print("---Python guessing game---")
print(f" Enter a number between {lowest_number} and the {highest_number}")

while is_running:
    guess=input(" Try to guess the number : ")
    
    if guess.isdigit():
        guess=int(guess)
        guesses +=1
        if guess < answer :
            print("**You are guessed too low !**")
            print("")
        elif guess > answer:
            print("**You are guessed too high !**")
            print("")
        else:
            print("**The answer is correct !**")
            print(f"**The number of guesses  : {guesses}**")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select number between{lowest_number} and {highest_number}")
