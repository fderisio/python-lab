import math

class Shape:
    def __init__(self, x, y):
      self.center = (x, y)

    def get_area(self):
      # empty shape does not have an area -> return 0
      return 0


class Triangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def get_area(self):
        return (self.width * self.height) / 2


class Rectangle(Shape, Triangle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        super().__init__(width, height)

    def get_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)
