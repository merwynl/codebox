import math

# Exercise 1: Calculating the circumference of a circle
# C = 2πr
radius = float(input("Please enter a radius value: "))
c = 2 * math.pi * radius
print (f"The circumference of a circle with a radius of {radius} rounded to two decimals = {round(c, 2)}cm.")

# Exercise 2: Calculating an area of a circle
# A = π𝒓²
radi = float(input("Please enter a radius value: "))
area = math.pi * (radi**2)
print (f"The area of a circle with a radius of {radi} rounded to two decimals = {round(area, 2)}cm².")

# Exercise 3: Hypotenuse of a triangle
# c = √(a² + b²)
side_a = float(input("Please enter a value for SideA: "))
side_b = float(input("Please enter a value for SideB: "))
h = math.sqrt((side_a**2) + (side_b ** 2))
print(f"The length of SideC with SideA length of {side_a}cm and SideB length of {side_b}cm = {round(h, 2)}cm.")