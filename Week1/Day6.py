import math  # for using π (pi)

# Base class
class Shape:
    def area(self):
        # This method will be overridden in derived classes
        pass


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Override the base class method to calculate rectangle area
        return self.length * self.width


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Override the base class method to calculate circle area
        return math.pi * (self.radius ** 2)


# Example usage
rect = Rectangle(10, 5)
circle = Circle(7)

print("Area of Rectangle:", rect.area())
print("Area of Circle:", circle.area())
