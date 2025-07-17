'''

Properties - A decorator used to define a method as a property (it can be accessed like an attribute)
           - Add additional logic with read, write or delete attributes
           - Gives you getter, setter and deleter method

'''

class Rectangle:
    def __init__(self, width, height):

        # Underscores denote private attributes.
        # Private attributes are protected and internal. Should not be accessed outside the class.
        # Only meant to be used inside the class.
        self._width = width
        self._height = height

    # Anything within these methods will be returned.
    # Allows protected/private attributes to be used outside a class through a method.
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # Using a setter to add additional functionality to a property or protected attribute.
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    # Taking a property and doing something extra with it
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    # Taking a property and deleting a public reference to it.
    @width.deleter
    def width(self):
        del self._width
        print("Width property has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height property has been deleted")

# Creating a class instance/object
rectangle = Rectangle(3,4)

# Sets the values on exposed properties
rectangle.width = 5
rectangle.height = -1

# Calls and prints the associated property values
print(rectangle.width)
print(rectangle.height)

# Deleting a property
del rectangle.width
del rectangle.height

