'''

Duck typing - Another way to achieve polymorphism besides Inheritance
              Objects must have a minimum necessary attributes/methods
              If it looks like a duck and quacks like a duck, then it must be a duck.

'''

# Setting up a parent class with a class attribute of alive.
class Animal:
    alive = True

# Class that inherits from the Animal class
class Dog(Animal):
    def speak(self):
        print("Woof!")

# Class that inherits from the Animal class
class Cat(Animal):
    def speak(self):
        print("Meow!")

# A separate class that does not inherit from Animal class and contains its own class attribute of 'alive'.
class Car:
    alive = False
    def speak(self):
        print("Honk!")

# Even though Car() does not inherit from the animal class, it contains a method found in that class.
# Car object contains its own class attribute of 'alive' therefore, there will be no attribute error.
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)