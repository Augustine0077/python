class Animal:
    def eat(self):
        print("This Animal can eat")
    def sleep(self):
        print("This animal can sleep")
class Pray(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")
        

class Rabbit(Pray):
    pass

class Hawk(Predator):
    pass

class Fish(Pray, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# call on instances (correct)
rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
rabbit.eat()  # This will raise an AttributeError since Rabbit does not inherit from Animal
rabbit.sleep()  # This will raise an AttributeError since Rabbit does not inherit from Animal
fish.eat()  # This will raise an AttributeError since Fish does not inherit from Animal
fish.sleep()  # This will raise an AttributeError since Fish does not inherit from Animal