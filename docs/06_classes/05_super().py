'''

Super - A Function used in a child class to call methods from a parent class(superclass)
      - Allows you to extend the functionality of inherited methods。

'''

# Declaring a superclass of shape from which the subclasses will inherit the attributes of color & is_filled
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'Filled ' if self.is_filled else 'Not Filled'} ")

class Circle(Shape):
    def __init__(self, color, is_filled,radius):
        # Think of the super function as a reference to the parent class.
        super().__init__(color, is_filled)
        self.radius = radius

    # Method overwriting.Overwriting a parent class method
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius} ")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

# Constructing class objects that inherit attributes from a parent class
circle = Circle("Red", is_filled=True, radius = 5)
square = Square("Green", is_filled=False, width = 10)
triangle = Triangle("Blue", is_filled=True, width = 2, height=6)

# Printing the results of a circle object that inherits attributes
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

# Printing the results of a square object that inherits attributes
print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
'''

Super - A Function used in a child class to call methods from a parent class(superclass)
      - Allows you to extend the functionality of inherited methods。

'''

# Declaring a superclass of shape from which the subclasses will inherit the attributes of color & is_filled
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'Filled ' if self.is_filled else 'Not Filled'} ")

class Circle(Shape):
    def __init__(self, color, is_filled,radius):
        # Think of the super function as a reference to the parent class.
        super().__init__(color, is_filled)
        self.radius = radius

    # Method overwriting.Overwriting a parent class method
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2 ")

        # Extending the functionality of a super method
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    # Method overwriting.Overwriting a parent class method
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2 ")

        # Extending the functionality of a super method
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    # Method overwriting.Overwriting a parent class method
    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2 ")

        # Extending the functionality of a super method
        super().describe()

# Constructing class objects that inherit attributes from a parent class
circle = Circle("Red", is_filled=True, radius = 5)
square = Square("Green", is_filled=False, width = 10)
triangle = Triangle("Blue", is_filled=True, width = 2, height=6)

# Printing the results of a circle object that inherits attributes
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

# Printing the results of a square object that inherits attributes
print(square.color)
print(square.is_filled)
print(f"{square.width}cm")

# Printing the results of a triangle object that inherits attributes
print(triangle.color)
print(triangle.is_filled)
print(f"Width of {triangle.width}cm. Height of {triangle.height}cm.")

# Using a method inherited from a parent class
circle.describe()
# Printing the results of a triangle object that inherits attributes
print(triangle.color)
print(triangle.is_filled)
print(f"Width of {triangle.width}cm. Height of {triangle.height}cm.")

# Using a method inherited from a parent class
circle.describe()

# Using a method inherited from a parent class
square.describe()

# Using a method inherited from a parent class
triangle.describe()