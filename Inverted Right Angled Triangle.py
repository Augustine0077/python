rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):  # Start from rows, go to 1
    for j in range(i):       # Print i stars in each row
        print("*", end=" ")
    print()  # Move to next line
