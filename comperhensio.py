#comperhension
# normal way
mark = [50,60,30,20,10,70,80,90,100]
passed = []
for i in mark:
    if i>=60:
        passed.append(i)
print("Passed marks are:", passed)

# # using comprehension
# mark = [50,60,30,20,10,70,80,90,100]
# passed = [i for i in mark if i>=60]
# print("Passed marks are:", passed)