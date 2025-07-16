'''

Multiple inheritance = inherit from more than one parent class
                       class C(A,B)


Multi level inheritance = Child can inherit from a parent which inherits from another parent
                          class C(B) <- class B(A) <- class A

'''

# Super class or grandparent class
class Animal:

    # Creating a constructor from which all subclasses will inherit from
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleeping(self):
        print(f"{self.name} is sleeping.")

# Will inherit everything the Animal class has
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing!")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# This inherits from both classes
class Fish(Prey, Predator):
    pass

# Setting up class objects
rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# This will return an error because the methods can't be found within the respective class they inherit from.
# rabbit.hunt()
# hawk.flee()

# This will work fine.
rabbit.flee()
hawk.hunt()

# This will work fine as the fish class inherits from both the Prey & Predator class.
fish.hunt()
fish.flee()

# Accessing the top level class method
rabbit.eat()
fish.sleeping()

