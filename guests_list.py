guests = []
while True:
    guest = input("Enter guest name (enter q to quit): ")
    if guest.lower() == "q":
        break
    guests.append(guest)
print("Guest List:")
for g in guests:
    print(g)