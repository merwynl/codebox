"""
Object = A bundle of related attributes (variables) and methods (functions)
         Ex. A cup, phone, book
         You need a class to create many objects

Class = Blueprint used to design the structure and layout of an object
"""

from classes.car import Car

# Invoking a class object & assigning some value to the parameters
car1 = Car("toyota", "2025", "silver", "sedan", False)
car2 = Car("honda", "2013", "black", "hatchback", True)
car3 = Car("nissan", "2003", "white", "sedan", False)
car4 = Car("lexus", "2023", "blue", "suv", True)
car5 = Car("mitsubishi", "2022", "red", "kei", False)

# Printing the memory address of a class object
print(car1)

# Printing a specific class attribute. The . signifies an attribute access operator.
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.type)
print(car1._for_sale)

# Accessing class methods
car1.drive()

# Accessing a different class method with a different object
car2.stop()

# Accessing a class method that determines if an object is available
car1.purchase()
car2.purchase()












