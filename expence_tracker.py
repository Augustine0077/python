expenses = []
amounts = []
while True:
    expense = input("Enter expense name (enter q to quit): ")
    if expense.lower() == "q":
        break
    amount = float(input("Enter amount: "))
    expenses.append(expense)
    amounts.append(amount)
print("Expenses:")
total = 0
for i in range(len(expenses)):
    print(f"{expenses[i]}: {amounts[i]}")
    total += amounts[i]
print(f"Total spent: {total}")