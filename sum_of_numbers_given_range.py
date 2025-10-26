num ,num2 = map(int, input("Enter two numbers separated by a space: ").split())
sum =  0
for i in range(num , num2 +1):
    sum += i
print("The sum of numbers from", num, "to", num2, "is:", sum)