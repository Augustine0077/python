
print("welcome to the tip calculator")
bill=int(input("what was the total bill?"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill?"))
tip_as_percentege=tip/100
total_tip_amount=bill*tip_as_percentege
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,3)
print(f"Each person should pay{final_amount}")
