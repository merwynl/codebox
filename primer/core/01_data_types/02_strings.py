"""
[Strings]
"""

# Strings are used to represent text
name = 'hiroyuki'
language = "日本語"
place = """日本"""

# Determining the length of a string
song_name = 'White Midnight'
print(len(song_name))

# Splitting a series of characters into a list
items = 'some,csv,values'
print(items.split(','))
# == ['some', 'csv', 'values']

# Printing quotations using backslash
phrase = "\"神様になった日\""
print(phrase)

# Printing normal backslash
phrase = "Σ/神様になった日"
print(phrase)

# String concatenation
phrase = "「神様になった日」"
print(phrase + "がかっこいい")

# String concatenation long method
phrase = "神様になった日"
feeling = "がかっこいい"
full = f"{phrase}{feeling}"
print(full)

# String slicing - prints the first index of a string
phrase = "White Midnight"
print(phrase[0])

# String slicing - prints the last index of a string
phrase = "White Midnight"
print(phrase[-1])

# String slicing - prints a range of index. The last index is not included.
phrase = "White Midnight"
print(phrase[0:5])

# String slicing - same as above, except without specifying a given start
phrase = "White Midnight"
print(phrase[:5])

# String slicing - prints from a specified index until the end
phrase = "White Midnight"
print(phrase[6:])

# Makes a string entirely upper case
phrase = "White midnight"
print(phrase.upper())

# Makes a string entirely lower case
phrase = "White Midnight"
print(phrase.lower())

# Capitalizes the first word
phrase = "white midnight"
print(phrase.capitalize())

# Capitalizes the first letter of every word
phrase = "white midnight"
print(phrase.title())

# Strips out any white spacing from the string
phrase = " white midnight "
print(phrase.strip())

# Strips out any white spacing from the left side of the string
phrase = " White midnight"
print(phrase.lstrip())

# Strips out any white spacing from the right side of the string
phrase = "White midnight "
print(phrase.rstrip())

# Find the index of the first given character or sequence of characters in the string
phrase = "White midnight"
print(phrase.find("mi"))

# Replaces the index of the first given character or sequence of characters in the string
phrase = "Black midnight"
print(phrase.replace("Black", "White"))

# Finds the given character or sequences of characters in a given string. Returns a boole value
phrase = "White midnight"
print("Apple" in phrase)

# Returns a boole value whether the supplied character or sequence of characters exists inside a given string
phrase = "White midnight"
print("midnight" not in phrase)

# Returns a boole if a string is entirely in the upper case or not
phrase = "White midnight"
print(phrase.isupper())

# Returns a boole if a string is entirely in the lower case or not
phrase = "White midnight"
print(phrase.islower())

# Makes a string entirely lower case then returns a boole whether a string is entirely in the upper case or not
phrase = "White Midnight"
print(phrase.upper().isupper())

# Printing the length of a string/how many characters
phrase = "\"神様になった日\""
print(len(phrase))

# Prints out the value/character based on the assigned index
phrase = "\"神様になった日\""
print(phrase[1])

# Returns the index value of the given supplied character
phrase = "\"神様になった日\""
print(phrase.index("日\""))

# Replaces an existing value with a different one. Takes two arguments, first bring the target & second being the target value
phrase = "\"神様になった日\""
print(phrase.replace("日", "月"))

#  Adding a double quote inside a string
phrase = 'Python \"Programming"'
print(phrase)

#  Adding a single quote inside a string
phrase = "Python \'Programming'"
print(phrase)

#  Adding a double slash inside a string
phrase = "Python \\\\ Programming"
print(phrase)

# Printing quotations using backslash
print("\"神様になった日\"")

# Printing normal backslash
print("Σ/神様になった日")

#  Checks of all the given characters are alphabetical letter
print("hello".isalpha())

# Checks if all the given characters are numerical value
print("123".isdigit())


