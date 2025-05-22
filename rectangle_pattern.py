rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
#
'''Whatever is in the outer loop = number of lines
Whatever is in the inner loop = number of stars per line''''''