weight=float(input("enter your wegiht "))
unit = input("enter unit (kg or lb) ")
if unit.lower()=="kg":
    converted_weight=weight * 2.20462
    print(f"Your weight in pounds is {converted_weight:.2f} lbs")

elif unit.lower()=="lb":
    converted_weight = weight / 2.20462
    print(f"Your weight in kilograms is {converted_weight:.2f} kg")

else:
    print("Invalid unit. Please enter 'kg' or 'lb'.")
