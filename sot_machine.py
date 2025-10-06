def spin_row():
    pass
def print_row():
    pass
def get_payout():
    pass

def main():
    balance = 100.0


    print("Welcome to the Slot Machine!")
    print("*************")
    print("Symbols: A, B, C, D")
    print("**************")
    while  balance > 0:
        print(f"Your balance is: ${balance:.2f}")
        bet = input("Enter your bet amount")

        if not bet.isdegit():



if __name__ == "__main__":
    main()