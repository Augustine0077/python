rows = int(input("Enter the number of rows: "))
for i in range(0,rows+1):
    for space in range(rows-i):
        print(" ",end = ' ')
    for star in range(i):
        print(" * ",end = ' ')
    print()