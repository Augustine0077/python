class Students:

    Year_passout = 2026
    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = Students("Augustine",22)
student2 = Students("John",23)

print(student1.name)
print(student2.age)
print(student1.Year_passout)
print(student2.Year_passout)