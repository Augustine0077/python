fruits = ['apple', 'banana', 'cherry']
vegetables = ['potato', 'carrot', 'broccoli']
meats = ['chicken', 'beef', 'pork']

grocery_list = [fruits, vegetables, meats]

for category in grocery_list:
    for item in category:
        print(item,end = " ,")