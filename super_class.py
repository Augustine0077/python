class Shape:
    def __init__(self,colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled
    def describe(self):
        print(f"it is {self.colour} and {'filled' if self.is_filled else 'not filled'}")
class Circle(Shape):
    def __init__(self, colour, radius, is_filled):
        super().__init__(colour, is_filled)
        self.radius = radius
        
class Square(Shape):
    def __init__(self, colour, width, is_filled):
        super().__init__(colour, is_filled)
        self.width = width
        
class Triangle(Shape):
    def __init__(self, colour, width, height, is_filled):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

circle = Circle("Red", 5, True)
square = Square("Blue", 4, False)
triangle = Triangle("Green", 3, 4, True)
print(circle.colour)
print(square.width)
print(triangle.height)

triangle.describe()