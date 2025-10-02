# # age=int(input("Enter your age: "))
# # print("can vote") if age >=18 else print("cannot vote")
# def net_price(orginal_price,discount=-5,tax=50):
#     return(orginal_price + discount+tax)
# print( net_price(500))

import time

def timer(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done !",end =" " )

timer(0,5)