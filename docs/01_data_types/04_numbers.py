"""
[summary]
"""

# Imports native math module
import math
from operator import length_hint

# Prints a basic given number
print(-2.0987)

# Incrementing a number
friends = 0
friends = friends + 2
print ("Friends: " + str(friends))

# Incrementing a number using augmented assignments
days = 0
days += 2
print ("Days: " + str(days))

# Simple addition
# days += 1
print("Addition(+=): "+ str(2+2))

# Simple subtraction
# days -= 1
print("Subtraction(-=): "+ str(4-2))

# Simple multiplication
# days *= 2
print("Multiplication(*=): " + str(3 * 4))

# Simple division
# days /= 2
print("Division(/=): "+ str(12 / 3))

# Returns the result of an exponent. In this case, 10 to the power of 2
# days **= 2
print ("Exponent(**=): " + str(days **2))

# Divides two given values & returns the remainder. Useful to determine if a number is even or odd
# days %= 2
print("Modulus(%=): " + str(27 % 4))

# Order of operations
print("3 * 4 + 5: " + str(3 * 4 + 5))
print("3 * (4 + 5): " + str(3 * (4 + 5)))

x = 3.142
y = 4
z = 7
a = -17

# Rounds a value either up or down. .5 values gets rounded up instead of down
print("round(3.142): " + str(round(x)))

# Returns the absolute value of a given number. Turns any negative number into a positive
# Removes the negative symbol.
print("abs(-17): " + str(abs(a)))

# Returns the power of a value by another value. Requires a (base, exponent)
# Pow, math.pow() and ** perform the same operation with some slight differences in compile speed and float semantics
# https://stackoverflow.com/questions/20969773/exponentials-in-python-xy-vs-math-powx-y
print("pow(4, 3): " + str(pow(4, 3)))

# Returns the larger of the given numbers that have been passed.
print("max(3.142, 4, 7, -17): " + str(max(x, y, z, a)))

# Returns the smallest of the given numbers that have been passed
print("min(3.142, 4, 7, -17): " + str(min(x, y, z, a)))

# Divides the first value by the 2nd and rounds the number down to the nearest integer
print("10 // 3: " + str(10 // 3))

# Returns the value of Pi
print("math.pi: " + str(math.pi))

# Returns the value of e or exponential constant
print("math.e: " + str(math.e))

# Returns the square root of a given number
print("math.sqrt(8): " + str(math.sqrt(8)))

# Rounds a number down to the nearest integer regardless if the decimal number being less than 5.
print("math.floor(3.142): " + str(math.floor(x)))

# Rounds a number up to the nearest integer regardless if the decimal number being less than 5.
print("math.ceil(3.142): " + str(math.ceil(x)))

# Exercise 1: Calculating the circumference of a circle
# C = 2πr
# radius = float(input("Please enter a radius value: "))
# c = 2 * math.pi * radius
# print (f"The circumference of a circle with a radius of {radius} rounded to two decimals = {round(c, 2)}cm.")
#
# # Exercise 2: Calculating an area of a circle
# # A = π𝒓²
# radi = float(input("Please enter a radius value: "))
# area = math.pi * (radi**2)
# print (f"The area of a circle with a radius of {radi} rounded to two decimals = {round(area, 2)}cm².")

# Exercise 3: Hypotenuse of a triangle
# c = √(a² + b²)
side_a = float(input("Please enter a value for SideA: "))
side_b = float(input("Please enter a value for SideB: "))
h = math.sqrt((side_a**2) + (side_b ** 2))
print(f"The length of SideC with SideA length of {side_a}cm and SideB length of {side_b}cm = {round(h, 2)}cm.")
