import math


class Circle:

    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be non-negative.")
    
    @staticmethod
    def pi():
        return math.pi 

    @property
    def area(self):
        return self.pi() * self.radius ** 2
    
    def cylinder_vol(self,height):
        return self.area * height

    

