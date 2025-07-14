"""
A block of resuable code
Functions are declared using the def signifier:
def function_name():
	some_code
function_name()
place () after the function name to invoke it.
"""

# Simple function that takes in two inputs and adds them together
def add_numbers(a, b):
	print(a + b)

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

# 