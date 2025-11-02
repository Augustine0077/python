# fruits = ['apple','banana','orange','grape','mango']

# i = iter(fruits)

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))  # This will raise StopIteration error since there are no more items to



def calculate():
    number  =  2
    while True:
        yield number
        num = number * number


gen = calculate()
print(next(gen))
print(next(gen))
print(next(gen))