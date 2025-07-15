"""
Iterables = An object/collection that can return its elements one at a time,
            allowing it to be iterated over a loop.
"""

#  A list is an iterable
numbers = [1,2,3,4,5]
for number in reversed(numbers):
    print(number, end="-")

# A tuple is also an iterable
numbers = (1,2,3,4,5)
for number in numbers:
    print(number)

#  A set is also an iterable. Sets can't be reversed.
fruits = {"apple", "orange", "banana", "coconut"}
for fruit in fruits:
    print(fruit)

#  A string is also technically a type of iterable.
name = "Some code"
for character in name:
    print(character, end=" ")

# A dictionary is also a type of iterable associated with a key-value pair. Printing the keys of a dictionary.
my_dict = {"A":1,"B":2, "C":3}
for key in my_dict:
    print(key)

# A dictionary is also a type of iterable associated with a key-value pair. Printing the values of a dictionary.
my_dict = {"A":1,"B":2, "C":3}
for values in my_dict.values():
    print(values)

# A dictionary is also a type of iterable associated with a key-value pair. Printing the key-value pair of a dict.
my_dict = {"A":1,"B":2, "C":3}
for key,value in my_dict.items():
    print(f"{key}: {value}")

