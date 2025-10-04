def show_balance():
    print(f"Your current balance is: ${balance:.2f}")
def deposit():
    amount = float(input("Enter amount to deposit: $"))

    if balance < 0:
        print("The balance cannot be less than 0")
        return 0
    else:
        return amount
def withdraw():
    amount = float(input("Enter the amout to withdrw"))

    if amount > balance:
        print("Insufficent fund")

balance = 0
is_running = True
while is_running:
    print("welcome to the bank program")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option between 1-4:   ")
    if choice == '1':
        show_balance()
    elif choice == '2':
       balance += deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid option, please choose a number between 1-4.")
print("Thank you for using the bank program. Goodbye!")