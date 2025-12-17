from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
if __name__ == "__main__":
    c = Circle(5)
    r = Rectangle(4, 6)

    print("Circle Area:", c.area())
    print("Circle Perimeter:", c.perimeter())
    print("Rectangle Area:", r.area())
    print("Rectangle Perimeter:", r.perimeter())