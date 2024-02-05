from .shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius:float)->None:
        if radius < 0:
            raise ValueError("The radius cannot be negative")

        self.radius = radius

    def area(self) ->float:
        return math.pi * math.pow(self.radius, 2)