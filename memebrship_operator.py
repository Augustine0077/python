grades={'Alice': 85, 'Bob': 90, 'Charlie': 78}
student= input("Enter student name: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not found in the records")