"""
Membership operators = Used to test whether a value is found in a collection
                       (string, list, tuple, set, dictionary)
                       1. In
                       2. Not in
"""
# Checks if a letter is in a word
word = "APPLE"
letter = input("Guess a letter in the secret word: ")
if letter.upper() in word:
    print(f"{letter} was found!")
else:
    print(f"{letter} was not found!")

# Checks is a letter is not in a word
word = "APPLE"
letter = input("Guess a letter in the secret word: ")
if letter.upper() not in word:
    print(f"{letter} was not found!")
else:
    print(f"{letter} was found!")

#  Checks for a string of characters within a set
students = {"Spot", "John", "Ken", "Lisa"}
student = input("Enter student's name: ")
if student in students:
    print(f"{student.capitalize()} is a registered student")
else:
    print(f"{student.capitalize()} was not found")

#  Checks id a string of characters is not within a set.
students = {"Spot", "John", "Ken", "Lisa"}
student = input("Enter student's name: ")
if student.capitalize() not in students:
    print(f"{student.capitalize()} was not found")
else:
    print(f"{student.capitalize()} is a registered student")

# Checks if an item is within a dictionary
grades = {"Lisa": "A",
          "John": "C",
          "Ken": "A+",
          "Spot": "B"}

student = input("Enter student's name: ")
if student.capitalize() in grades:
    print(f"{student}'s grader is {grades[student]}")
else:
    print(f"{student.capitalize()} was not found")

# Checks if an email address is valid
email = "mail@fakemail.com"
if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address")