# input() - Prompts the user to enter some data and returns it as a string.
import math

# Asking the user’s name
name = input("Greetings, please enter your name: ")

# Asking the user’s age. Input value has to be type converted before incrementing else it will be treated as a str.
# Inout values is enclosed in qa typecast to remove an extra line.
age = int(input("What is your age: "))
age += 1

# Asking the user’s location
place = input("Please enter your current location: ")

# Requesting today’s date through user input
date = input("Please enter today's date: ")
print(f"Greetings {name}. You are {age} years of age as of today. It is, {date} -3 celsius in {place}")

# Exercise 1: Calculating the area of a rectangle
# Area = width * length
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width
print(f"The area of this rectangle is {area}cm²")
print(f"This rectangle is {width}cm in width * {length}cm in width.")

# Exercise 2: Shopping Cart Program
item = input("Please enter an item: ")
price = float(input("Please enter the current price: "))
quantity = int(input("Please enter the quantity of that item: "))
total = math.ceil(price * quantity)
print(f"You have purchased {quantity} {item.lower()}'s for {math.ceil(price)}円 each.")
print(f"Your total is: {total}円")

# Exercise 3 — Mad-libs game
# Word game where you create a story by filling in the blanks with random words.
adjective1 = input("Please enter an adjective (description): ")
adjective2 = input("Please enter an adjective (description): ")
adjective3 = input("Please enter an adjective (description): ")
noun1= input("Please enter a noun (place/person/object): ")
verb1 = input("Please enter a verb (action): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In one particular exhibit, I saw an {noun1}.")
print(f"{noun1} was rather {adjective2} while {verb1}.")
print(f"I was rather {adjective3}.")