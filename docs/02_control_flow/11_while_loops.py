"""
Executes code while some condition remains true. Be on the lookout for infinite loops, they can crash a programs.
while a condition is true or not true:
    execute code potentially forever
else:
    do something
"""

i = 1

# While i is less than the given variable, do the function
num = 100
while i <= num:
    print(i)
    i += 1

    # alternate method of incrementing
    # i = i +1

print('Done!')

# Keep prompting the user until name is provided
name = input("Enter your username: ")
while name == "":
    print("You did not enter anything!")
    name = input("Enter your username: ")
else:
    print(f"Hello {name}")

#  Keep prompting the user until a positive number indicating their age has been provided
age = int(input("Please enter your age: "))
while age < 0:
    print ("Age cannot be less than 0")
    age = int(input("Please enter your age: "))
else:
    print(f"You are {age} years old")

# Keep prompting and printing a users favourite food until q is entered
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print (f"You like {food}!")
    food = input("Enter a food you like (q to quit): ")
print("Bye!")

# Keeps prompting the user to enter a valid number between 1-10
num = int(input("Enter a # between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))
print (f"Your num is {num}.")