'''

Decorators - A function that extends the behaviour of another function
           - w/o modifying the base function
           - Pass the base function as an argument to the decorator
           - Think of decorators as additional dressing on top of a salad
           @add_sprinkles
           get_ice_cream("vanilla")
'''

# Creating a decorator
def add_sprinkles(func):
    # Without a wrapper function, both add_sprinkles() & get_ice_cream() will be instantly called when decorator is applied.
    def wrapper(*args, **kwargs):
        print("*Sprinkles added 🎊")
        func(*args, **kwargs)
    return wrapper # Returning a whole function.

def add_fudge(func):
    # If the main function takes in arguments, pass in args & kwargs to take in any number of arguments.
    # Type error will occur if this is not done.
    def wrapper(*args, **kwargs):
        print("*You have added fudge 🍫")
        func(*args, **kwargs) # Referencing a function requires the same number of args & kwargs as the wrapper.
    return wrapper

# Invoking the decorator. You can apply more than one decorator to a function
@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream 🍨")

# Calling on a function that has two decorators applied
get_ice_cream("Chocolate")

# Showcasing the use of a decorator without a wrapper.
def add_decorator(func):
    print ("This is from the decorator")
    func()

@add_decorator
def main ():
    print("This is the main function body")