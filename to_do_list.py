tasks = []
while True:
    task = input("Enter a task (enter q to quit): ")
    if task.lower() == "q":
        break
    tasks.append(task)
print("Your To-Do List:")
for t in tasks:
    print(t)