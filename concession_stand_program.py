# menu = {
#     "coca_cola": 1.50,
#     "pepsi": 1.50,
#     "water": 1.00,
#     "popcorn": 2.00,
#     "candy": 1.25,
#     "nachos": 3.00
# }

# cart = []
# total =0
# print("-----------------------")
# print("--------------MENU--------------")
# print("-----------------------")
# for key,value in menu.items():
#     print(f"{key}: ${value:.2f}")
# print("-----------------------")

# while True:
#     food=input("What would you like to order? (Type 'Q' to finish): ").lower()
#     if food == 'q':
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
# for food in cart:
#     total += menu[food]
# print(f"Your total is: ${total:.2f}")

menu = {
    "coca_cola": 1.50,
    "pepsi": 1.50,
    "water": 1.00,
    "popcorn": 2.00,
    "candy": 1.25,
    "nachos": 3.00
}
cart = []
total = 0
for key,value in menu.items():
    print(f"{key}:${value:.2f}")
while True:
        food =input("What would you like to order? (Type 'q' to quit): ").lower()
        if food == 'q':
         break
        elif menu.get(food) is not None:
           cart.append(food)
for food in cart:
   total +=menu[food]
print(f"Your total is: ${total:.2f}")