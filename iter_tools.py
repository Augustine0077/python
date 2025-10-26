fruits = ['apple','banana','orange','grape','mango']

i = iter(fruits)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))  # This will raise StopIteration error since there are no more items to