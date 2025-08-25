num_pad=((1,2,3),
        (4,5,6),
        (7,8,9),
        ("*",0,"#"))
for row in num_pad:
    for nums in row:
        print(nums,end = " ")
    print()