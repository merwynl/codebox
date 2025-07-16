"""
Default arguments = a default value for a certain parameters
default is used when that argument is ommitted when you invoke your functions
make your functions more flexible, reduces # of args
1. positional
2. DEFAULT
3. keyword
4. arbitrary
"""
import time

# Function for calculating the net price of a certain item using default args.
def net_price(list_price, discount = 0, tax=0.05):
	return list_price * (1 - discount) * (1 + tax)
print(net_price(500,0.1))  # arg values can be overwritten or omitted when a function is invoked.

# Counter starts at 0 and counts and increments up to 10.
def count(start=0,end=10):
	for x in range(start, end+1):
		print(x)
		time.sleep(1)
	return "DONE!"
print(count())

# Default arguments must come after positional arguments
def count(end, start=0):
	for x in range(start, end+1):
		print(x)
		time.sleep(1)
	return "DONE!"
print(count(10))
print(count(30,15))

# Counter starts at 10 and counts down but 1 every second until 0.
def countdown(start=0, end=10):
	for x in reversed(range(start, end+1)):
		print(x)
		time.sleep(1)
	return "DONE!"
print(countdown(0, 10))

# Using a range step value to count down
def countdown(start, end=0):
	for x in range(start, end, -1):
		print(x)
		time.sleep(1)
	return "DONE!"
print(countdown(10))