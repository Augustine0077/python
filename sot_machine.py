import random
def spin_row():
    symbols  =["1", "2", "3", "4", "5"]
    result = [ random.choice(symbols) for _ in range(3)]
    
def print_row():
    pritn(" | ".join(row))

def get_payout():
    pass

def main():
    balance = 100

    print("******************************")
    print("Welcome to the Slot Machine!")
    print("1--2--3--4--5")
    print("******************************")

    while balance > 0:
        print(f"your current balance is {balance}")
        bet = (input("Enter a bet amount : "))
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance")
            continue
        if bet <=0:
            print("Bet must be greater than zero")
            continue    
        balance -= bet

        row  = spin_row()
        print_row(row)
if __name__ == "__main__":
    main()
