'''

Inheritance - Allows a class to inherit attributes and methods from another class
              Helps with code reusability and extensibility
              class Child(Parent)

'''

# Creating a parent class
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# Creating a child class of type dog. This class will inherit all attributes from the parent class.
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    pass

dog = Dog("Rover")
cat = Cat("Tom")
mouse = Mouse("Jerry")

# Printing the results of an inherited value
print(dog.name)
print(dog.is_alive)

# Calling methods from an inherited class
cat.eat()
cat.sleep()

#  Calling different methods from child classes
dog.speak()
cat.speak()
