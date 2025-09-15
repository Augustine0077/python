import time

def count(end,start=0):
    for i in range(start,end+1):
        print(i)
        time.sleep(.5)
    print("Done")
count(10)
