"""
args = arbitrary arguments, allows you to pass multiple non-key args
kwargs = keyword arbitrary arguments, allows you to pass multiple keyword args
*unpacking operator
1. positional
2. DEFAULT
3. keyword
4. arbitrary
"""
from tkinter.font import names


# Using args to pass in a non-defined number of args and add those values together
def add(*args):
	total = 0
	for arg in args:
		total += arg
	return total

print(add(1, 2,3))
print(add(1))
print(add(1, 2,3),4,5)

# Changing the name of the arg but performs the same functionality as the above.
def add(*nums):
	total = 0
	for num in nums:
		total += num
	return total
print(add(1, 2,3))

# Using *args to print out a name
def display_names(*args):
	for arg in args:
		print(arg.capitalize(), end= " ")

display_names('jack', 'h', 'thorn')

# Using kwargs to pass multiple keyword args
def print_address(**kwargs):
	for key,value in kwargs.items():
		print(f"{key}: {value}")
print_address(prefecture="東京都",
			  ward="中央区",
			  street="１－２３－４",
			  building="中央ビル1階")

# Printing out values of kwargs
def print_address(**kwargs):
	for value in kwargs.values():
		print(f"{value}", end="")
	print()
print_address(prefecture="東京都",
			  ward="中央区",
			  street="１－２３－４",
			  building="中央ビル1階")

# Printing out keys of kwargs
def print_address(**kwargs):
	for key in kwargs.keys():
		print(f"{key}")
print_address(prefecture="東京都",
			  ward="中央区",
			  street="１－２３－４",
			  building="中央ビル1階")

# Using both args & kwargs. Args always comes before kwargs
def shipping_label(*args, **kwargs):
	for arg in args:
		print(arg, end=" ")
	print()
	for value in kwargs.values():
		print(value, end="")

shipping_label("Dr.", "Ken", "Watanabe",
			   prefecture="東京都",
			   ward="中央区",
			   street="１－２３－４",
			   building="中央ビル1階")

# Using both args & kwargs to print out an address and verify if certain args exist.
def shipping_label(*args, **kwargs):
	print(f"{kwargs.get('zip')}")
	print(f"{kwargs.get('prefecture')}{kwargs.get('ward')}{kwargs.get('street')}")
	if "building" in kwargs:
		print(f"{kwargs.get('building')} {kwargs.get('apt')}")
	elif "pobox" in kwargs:
		print(f"PO Box {kwargs.get('pobox')}")
	else:
		print(f"{kwargs.get('apt')}")
	for arg in args:
		print(arg, end=" ")
	print()
shipping_label("Dr.", "Ken", "Watanabe",
			   zip="123-1234",
			   pobox="1234",
			   prefecture="東京都",
			   ward="中央区",
			   street="１－２３－４",
			   building="Sakura Mansion",
			   apt="中央ビル1階")