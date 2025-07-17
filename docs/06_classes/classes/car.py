

# Creating a class object of type Car
class Car:

    # Constructor needed to create objects. Methods are functions within a class. Passing args to a method.
    def __init__(self, model, year, color, type, for_sale):
        # Assigning args to variables or instance attributes
        self.model = model.capitalize()
        self.year = year
        self.color = color
        self.type = type
        self._for_sale = for_sale

    def drive(self):
        # Self is referring to the object we're currently working with.
        print(f"You're driving the {self.color} {self.model} {self.type}.")

    def stop(self):
        print(f"You've stopped the {self.color} {self.model} {self.type}.")

    def purchase(self):
        if self._for_sale:
            print(f"The {self.year} {self.color} {self.model} {self.type} is for sale.")
        else:
            print(f"The {self.year} {self.color} {self.model} {self.type} is not for sale.")

