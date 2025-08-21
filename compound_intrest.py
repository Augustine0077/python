principle_amount = int(input("Enter the principal amount: "))

while principle_amount <= 0:
    print("Please enter a valid principal amount greater than zero.")
    principle_amount = int(input("Enter the principal amount: "))

annual_rate = float(input("Enter the annual interest rate (in %): "))
num_years = int(input("Enter the time in years: "))
compounds_per_year = int(input("Enter the number of times interest is compounded per year: "))

final_amount = principle_amount * (1 + annual_rate / 100 / compounds_per_year) ** (compounds_per_year * num_years)

print(f"The final amount after {num_years} years is: {final_amount:.2f}")