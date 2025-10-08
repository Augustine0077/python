def spin_row():
    pass

def print_row():
    pass

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
        bet = input("Enter a bet amount : ")
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

if __name__ == "__main__":
    main()
