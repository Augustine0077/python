balance = 0.0

def show_balance():
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: $"))

    if amount < 0:
        print("Deposit amount must be positive.")
        return 0
    else:
        return amount

def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: $"))

    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0.")
        return 0
    else:
        return amount

def main():
    global balance
    is_running = True
    while is_running:
        print("welcome to the bank program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option between 1-4: ")
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

if __name__ == "__main__":
    main()