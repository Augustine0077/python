import time
<<<<<<< HEAD
my_time = int(input("Enter the time in seconds: "))
for i in range(my_time,0, -1):
    
    seconds= i % 60
    minites = int(i / 60) % 60
    hours = int(i / 3600)   
    
    print(f"{hours:02}:{minites:02}:{seconds:02}")
    time.sleep(1)
=======

t_ime= int(input("Enter the time in seconds: "))

for x in range(t_ime, 0, -1):
	seconds = x % 60
	minutes = (x // 60) % 60
	hours = x // 3600
	print(f"{hours:02}:{minutes:02}:{seconds:02}")
	time.sleep(1)
>>>>>>> 99f87dec88ad1c11b237380c6adf6b78c117815a
print("Time's up!")