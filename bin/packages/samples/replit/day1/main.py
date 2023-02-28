# Printing
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Debugging Practice & string concatenation
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n."))

# Input function
print(len(input("Hello " + "What is your name?")))

# Variables
name = input("What is your name?")
length = len(name)
print (length)

# Switching variables
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)


# Brand Name Generator
# 1. Create a greeting for your program
print("バンドな生成器へよこそ！")

# 2. Ask the user for the city that they grew up in
city = input("育った出町のお名前は？")
print(city+"\n")

# 3. Ask the user for the name of a pet.
pet = input("ペットというのお名前は？")
print(pet+"\n")

# 4. Combine the name of their city and pet and show them their band name.
print("おそらく君のバンドの名は" + city + pet )

# 5. Make sure the input cursor shows on a new line