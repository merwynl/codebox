"""
One line shortcut for if-else statements
Print or assign one of two values based on a condition
Struct: x if condition else y
"""

# Prints a "Positive or negative based on a given value
num = float(input("Please enter a number"))
print ("Positive" if num > 0 else "Negative")

# Checks to see if a number is even or odd
num = float(input("Please enter a number"))
result = "EVEN" if num % 2 == 0 else 'ODD'
print(result)

# Checks to see find the min & max values
a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(f"Max num = {max_num}")
print(f"Min num = {min_num}")

# Check to see if an individual is an adult or child
age = 25
status = "Adult" if age >= 18 else "Child"
print (status)

# Check to see if the temperature is toasty or cool
temp = 30
weather = "TOASTY" if temp >= 30 else "COOL"
print (weather)

# Check if a user is admin
user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Access Denied"
print (access_level)