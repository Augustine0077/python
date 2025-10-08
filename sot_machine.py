import random

def spin_row():
    symbols = ["1", "2", "3", "4", "5"]
    result = [random.choice(symbols) for _ in range(3)]
    return result

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row, bet):
    # three of a kind -> 10x, two of a kind -> 3x, else 0
    if row[0] == row[1] == row[2]:
        print("Jackpot! You win 10 times your bet!")
        return bet * 10
    if row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        print("You win 3 times your bet!")
        return bet * 3
    print("No win this time. Try again!")
    return 0

def main():
    balance = 100.0

    print("******************************")
    print("Welcome to the Slot Machine!")
    print("Symbols: 1 2 3 4 5")
    print("Type 'q' to quit anytime.")
    print("******************************")

    while balance > 0:
        print(f"Your current balance is ${balance:.2f}")
        bet_str = input("Enter a bet amount (or 'q' to quit): ").strip()
        if bet_str.lower() == 'q':
            break
        if not bet_str.isdigit():
            print("Please enter a valid positive whole number for the bet.")
            continue
        bet = int(bet_str)
        if bet <= 0:
            print("Bet must be greater than zero.")
            continue
        if bet > balance:
            print("Insufficient balance.")
            continue

        balance -= bet
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout:.2f}!")
            balance += payout
        else:
            print(f"You lost ${bet:.2f} this spin.")
        print()  # blank line between rounds

    print(f"Game over. Final balance: ${balance:.2f}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
