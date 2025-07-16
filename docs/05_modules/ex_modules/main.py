
import math
pi = 3.14159

# Function for returning the square value of a given number
def square(x):
    return x ** 2

# Function for returning the cube value of a given number
def cube(x):
    return pow(x, 3)

# Simple function that takes in two inputs and adds them together.
def add_numbers(a, b):
    return a + b

# Using a return statement to return the value of adding two numbers.
def add(x, y):
    z = x + y
    return z

# Using a return statement to return the value of subtracting two numbers.
def subtract(x, y):
    z = x - y
    return z

# Using a return statement to return the value of multiplying two numbers.
def multiple(x, y):
    z = x * y
    return z

# Exercise 1: Calculating the circumference of a circle
# C = 2πr
def circumference(radius):
    return 2 * math.pi * radius

# Exercise 2: Calculating an area of a circle
# A = π𝒓²
def area(radius):
    return math.pi * (radius**2)

# Exercise 3: Hypotenuse of a triangle
# c = √(a² + b²)
def hypotenuse(a, b):
    return math.sqrt((a**2) + (b ** 2))