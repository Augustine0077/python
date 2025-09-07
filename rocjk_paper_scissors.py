import random

options = ("rock", "paper", "scissors")

running = True
while running:
    # ask player choice
    player = None
    while player not in options:
        player = input("Choose your option ('rock', 'paper', 'scissors'): ").lower()

    # computer choice
    computer = random.choice(options)

    print(f"Player choice : {player}")
    print(f"Computer choice : {computer}")

    # game rules
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("Computer wins! You lose --")

    # 👇 this must come immediately after one round is finished
    choice = input("Do you want to continue? (y/n): ").lower()
    if choice != "y":
        running = False

print("---- Thanks for Playing ----")
