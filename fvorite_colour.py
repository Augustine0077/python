colors = []
while True:
    color = input("Enter your favorite color (enter q to quit): ")
    if color.lower() == "q":
        break
    colors.append(color)
print("Favorite Colors:")
for c in colors:
    print(c)