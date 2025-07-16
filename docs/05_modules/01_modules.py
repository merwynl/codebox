"""
Module = A file containing code you want to include in your program
         Use 'import' to include a module (built-in or your own)
         Useful to break up a large program into reusable separate files.
Variable scope = where a variable is visible and accessible
Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-In

Main functions can be imported or run standalone
Functions and classes in this module can be reused without the main block executing.
Something you want to

if __name__ == '__main__':
    main()
"""

import sys
import math as m
from math import e
from math import pi

# Relative import of module using namespace
import ex_modules.main as tools

# Imports everything from ex_modules
from ex_modules.main import*

# Using the help function to print a list of built-in python modules.
print(help("modules"))

# Using the help function to get help wirth a specific module.
print(help("warnings"))

# Using the sys module to print a list of system paths to Python.
print(sys.path)

# Using assigned alias of a module to call on a function.
print(m.pi)

# Using the from [module] import [function] to import a specific function.
# Naming conflicts can sometimes occur when using the from declarative.
print(pi)

# Using imported module to print call on a statement
result = tools.pi
print(result)

# Using imported module to print call a function that prints the value of cube.
result = tools.cube(3)
print(result)

# Using imported module to print call a function that prints the square value of a given number.
result = tools.square(3)
print(result)

# Exercise 1: Calculating the circumference of a circle
# C = 2πr
def circumference():
    radius = float(input("Please enter a radius value: "))
    results = tools.circumference(radius)
    print(f"The circumference of a circle with a radius of {radius} rounded to two decimals = {round(results, 2)}cm.")

# Exercise 2: Calculating an area of a circle
# A = π𝒓²
def area():
    radius = float(input("Please enter a radius value: "))
    results = tools.area(radius)
    print(f"The area of a circle with a radius of {radius} rounded to two decimals = {round(results, 2)}cm².")

# Exercise 3: Hypotenuse of a triangle
# c = √(a² + b²)
def hypotenuse():
    side_a = float(input("Please enter a value for Side A: "))
    side_b = float(input("Please enter a value for Side B: "))
    results = tools.hypotenuse(side_a, side_b)
    print(f"The length of Side C with Side A length of {side_a}cm and Side B length of {side_b}cm = {round(results, 2)}cm.")

# Functions can't see inside other functions. This will error.
def function1():
    a = 1
    print(b)

def function2():
    b = 1
    print(a)

# Nesting functions. When calling function1, this will call the result of calling function2.
# as we've shifted focus to the enclosed scope
def function1():
    x = 1
    def function2():
        x = 2
        print(x)
    function2()

# Variable has been moved outside the function and is now in a global scope.
# There is no local or enclosed variable
# Calling both functions will print the same value.
x = 3
def function1():
    print(x)
def function2():
    print(x)

# Using the LEGB order, this will print our declared global var of e and not the imported module of e
def function1():
    print(e)
e = 3
function1()

# Printing out a list of modules and attributes such as __name__
print(dir())

# Printing out the value of __name__ relative to the current residing module.
# This script is being run directly
print(__name__)

# Imports everything from sample_main module
from sample_main import*


