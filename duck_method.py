class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Car:
    def speak(self):
        print("Honk")

animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    