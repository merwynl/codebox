"""
Generating random number using the random module

"""

import random

# Random module help guide
print (help(random))

# Prints a random int between 1 and 20
number = random.randint(1,20)
print(number)

# Using vars to specify a range
low = 1
high = 20
number = random.randint(low,high)
print(number)

# Prints a random float value
number = random.random()
print(number)

# Prints a random float value between 0-1
number = random.random()
print(number)

# Prints a random float value between 0-1
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

# Using the shuffle method to shuffle a list of items
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]
random.shuffle(cards)
print(cards)