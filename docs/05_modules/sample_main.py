import os
import os.path as path

# Using a return statement to return the value of adding two numbers.
def add(x, y):
    z = x + y
    return z

# Prints something else
def favourite_food(food):
    print(f"Your favourite food is {food}")

# This will still run when imported
print('This is something else')
favourite_food("Pineapple")
print('Farewell')

# Main function will not run from other modules when imported
def main():
    print('This is script 1')
    favourite_food("sushi")
    print('Goodbye')

# Can be imported or run standalone
# Function and classes in this module can be reused without the main block of code executing.
if __name__ == '__main__':
    main()
