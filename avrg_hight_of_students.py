# Ask the user to input a list of student heights separated by spaces
student_heights = input("Input a list of student heights separated by spaces: ").split()

# Convert each height from string to integer
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Calculate the total height of all students
total_height = 0
for height in student_heights:
    total_height += height

# Calculate the number of students
number_of_students = len(student_heights)

# Calculate the average height of the students
average_height = round(total_height / number_of_students)

# Print the results
print(f"Total height = {total_height}")
print(f"Number of students = {number_of_students}")
print(f"Average height = {average_height}")
