# Abstraction simplifies complex systems by breaking them into smaller, more manageable parts. 
# It focuses on what an object does rather than how it does it.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
