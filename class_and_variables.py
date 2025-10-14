class Students:

    Year_passout = 2026
    number_of_students = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Students.number_of_students += 1

student1 = Students("Augustine",22)
student2 = Students("John",23)
student3 = Students("Doe",24)
print(student1.name)
print(student2.age)
print(student1.Year_passout)
print(Students.number_of_students)