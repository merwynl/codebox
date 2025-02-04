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


