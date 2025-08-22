foods = []
prices = []
total = 0


while True:
    food = input("Enter the food item ( enter q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of food: "))
        prices.append(price)
        foods.append(food)

print("---ITEMS IN YOUR CART---")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print()
print(f"Total bill {total} price")

