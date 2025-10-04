def show_balance():
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("Deposit amount must be positive.")
        return 0
    else:
        return amount

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount < 0:
        print("Withdraw amount must be positive.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"${amount:.2f} withdrawn.")

balance = 0
is_running = True

while is_running:
    print("welcom to the bank program")
    print("1. Show Balance")
    print("2. Deposit") 
    print("3. Withdraw")
    print("4. Exit")

    try:
        Choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if Choice == 1:
        show_balance()
    elif Choice == 2:
        balance += deposit()
    elif Choice == 3:   
        withdraw()
    elif Choice == 4:   
        is_running = False
    else:
        print("That is not a valid choice. Please choose a number between 1 and 4.")
print("Thank you for using the bank program. Goodbye!")