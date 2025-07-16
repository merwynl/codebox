"""
A block of reusable code
Functions are declared using the def signifier:
def function_name():
	some_code
function_name()
place () after the function name to invoke it.
Return = A statement used to end a function and send a result back to the caller.
"""

# Function for printing a hello statement
def hello(name):
	print(f'Hello {name}!')

# Passing in multiple arguments to a function. Order matters.
def greeting(name, age):
	print(f'Hello {name}! Happy {age} years old to you!')

# Function declaration to display the amount due on an invoice
def display_invoice(username, amount, due_date):
	print (f'Hello {username}!')
	print(f'Your bill of ${amount:.2f} is due: {due_date}')

# Simple function that takes in two inputs and adds them together.
def add_numbers(a, b):
	print(a + b)

# Using a return statement to return the value of adding two numbers.
def add(x, y):
	z = x + y
	return z
print(add(1,2))

# Using a return statement to return the value of subtracting two numbers.
def subtract(x, y):
	z = x - y
	return z
print(subtract(1,2))

# Using a return statement to return the value of multiplying two numbers.
def multiple(x, y):
	z = x * y
	return z
print(multiple(1,2))

# Using a return statement to return the value of dividing two numbers.
def divide(x, y):
	z = x / y
	return z
print(divide(1,2))

# Using a return statement to return the concatenation of two strings.
def create_name(first,last):
	first = first.capitalize()
	last = last.capitalize()
	return first + " " + last
print(create_name('some', 'name'))

# Print seperator
def print_range():
    print("1","2","3","4","5", sep="-")
    return 0
print_range()