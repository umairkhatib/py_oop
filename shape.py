from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    """
    Shape is an abstract base class that defines the structure for all shapes.
    Any subclass must implement the area() method.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass


# Concrete class: Rectangle
class Rectangle(Shape):
    """
    Rectangle class inherits from Shape and implements the area() method.
    """

    def __init__(self, width, height):
        """
        Constructor to initialize width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height


# Example usage
rect = Rectangle(5, 3)
print("Area of rectangle:", rect.area())
