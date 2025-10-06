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
    choice = input("Choose an option between 1-4:   ")
    if choice == '1':
        show_balance()
    elif choice == '2':
    balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid option, please choose a number between 1-4.")
print("Thank you for using the bank program. Goodbye!")

