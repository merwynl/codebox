'''

Polymorphism - Greek word that means to have "many forms or faces":
               Poly = Many
               Morphe = form

               Two ways to achieve Polymorhism
               1. Inheritance - An object could be treated of as the same type as a parent class.
               2. "Duck Typing" - Objects must have necessary attributes/methods
'''

from abc import ABC, abstractmethod

# Defining an abstract class
# An abstract class cannot be instantiated on its own and is designed to be scaffolding for other classes.
class Shape:

    # Method within an abstract class. A method within an abstract class.
    @abstractmethod
    def area(self):
        pass

# A subclass that is inherited from an abstract class
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    # Providing an implementation of an abstract method
    def area(self):
        return 3.14 * self.radius ** 2

# A subclass that is inherited from an abstract class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    # Providing an implementation of an abstract method
    def area(self):
        return self.side ** 2

# A subclass that is inherited from an abstract class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # Providing an implementation of an abstract method
    def area(self):
        return self.base * self.height * 0.5

# Inheriting from the Circle class, which inherits from the Shape class. Giving us access to methods in both classes.
class Pizza(Circle):
    def __init__(self, topping, radius):
        # self.radius = radius
        # Instead of declaring a local class variable of self.radius, try calling on the superclass
        # This gives you access to the abstract method.
        super().__init__(radius)
        self.topping = topping

# This object inherits from both the Circle and Shape class but not from Square or Triangle.
circle = Circle(4)

# This object inherits from both the Square and Shape class but not from Circle or Triangle.
square = Square(5)

# This object inherits from both the Triangle and Shape class but not from Circle or Circle.
triangle = Triangle(6,7)

# Instantiating a list of objects that are inherited from a parent shape class
shapes = [Circle(4), Square(5), Triangle(6,7),Pizza("Peperoni", 15)]

# Without inhering from another class, the Pizza object will return an attribute error.
for shape in shapes:
    print(f"{shape.area()}cm^2")