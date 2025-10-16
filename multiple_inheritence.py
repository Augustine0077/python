class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} can eat")
    def sleep(self):
        print(f"{self.name} can sleep")
class Pray(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Pray):
    pass

class Hawk(Predator):
    pass

class Fish(Pray, Predator):
    pass

rabbit = Rabbit("Chinden")
hawk = Hawk("kurnari")
fish = Fish("Nemo")

# call on instances (correct)
rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()
print(fish.name)