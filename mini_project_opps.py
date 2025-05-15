class pet:
    def __init__(self,name,age,category):
        self.name = name
        self.age = age  
        self.category = category

    def show_details(self):
        print(f"{self.name} is a {self.age} year old {self.category}")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

pet1=pet("dog",5,"husky")
pet2=pet("cat",3,"persian")

pet1.show_details()
pet2.show_details()