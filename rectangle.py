rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))  
symbol = input("Enter symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end=' ')
    print()  # Print a newline after each inner loop completes