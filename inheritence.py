class Animal:

    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass
class Cat(Animal):
    pass

class Fish(Animal):
    pass


dog = Dog("Tommy")
cat = Cat("Kitty")
fish = Fish("Nemo")

print(fish.name)
print(fish.is_alive)


