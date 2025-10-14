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
print(f" my name is {student1.name}")
print(f" my age is {student2.age}")
print(f" I will graduate in {student1.Year_passout}")

print(f" I am graduating in {Students.Year_passout} and in my class there are {Students.number_of_students} students")