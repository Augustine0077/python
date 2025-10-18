class Shape:
    def __init__(self,colour,is_filled):
        self.colour = colour
        self.is_filled = is_filled
class Circle:
    def __init__(self,colour,radius,is_filled):
        super().__init__(colour,is_filled)
        self.radius = radius
        
class Square:
    def __init__(self,colour,width,is_filled):
        super().__init__(colour,is_filled)
        self.width = width
        
class Triangle:
    def __init__(self,colour,width,height,is_filled):
        super().__init__(colour,is_filled)
        self.width = width
        self.height = height
       