from abc import ABC , abstractmethod 

class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
        def area(self):
            return self.side **2
class Triangle(Shape):
    def __init__(self , base , height):
        self.height = height
        self.base = base
    def area(self):
        return self.base * self.height *0.5

class Pizza(Shape):
    def __init__(self,topping,radius):
        self.topping = topping
        self.radius = radius
shapes = [Circle(4),Square(5), Triangle(6, 8),Pizza("Pepperoni", 7)]  
for shape in shapes:
    print(f"The area is: {shape.area()}")