items = []
while True:
    item = input("Enter item to buy (enter q to quit): ")
    if item.lower() == "q":
        break
    items.append(item)
print("Shopping List:")
for i in items:
    print(i)