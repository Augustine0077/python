students = []
grades = []
while True:
    name = input("Enter student name (enter q to quit): ")
    if name.lower() == "q":
        break
    grade = float(input("Enter grade: "))
    students.append(name)
    grades.append(grade)
print("Student Grades:")
for i in range(len(students)):
    print(f"{students[i]}: {grades[i]}")