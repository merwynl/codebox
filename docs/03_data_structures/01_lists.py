"""
Collections = single variable to store multiple values.
List = [] ordered and mutable. Duplicates OK.
Sets = {} unordered and immutable but Add/Remove OK. NO duplicates.
Tuples = () ordered and immutable. Duplicates OK. Faster.
"""

# Creating a list and printing that list. Index of 0
fruits = ['apple', 'orange', 'banana', 'coconut']
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']

# Lists can take in more than one data type
combined = ['れをる', str(2), True, str(1.256)]
print (combined)

# Prints the entire list values
print(singers)

# Prints the index value from the list
print(fruits[0])

# Prints the last index value from the list, or the first item from the end of the list.
print(singers[-1])

# Prints the values from the list starting with the given index.
print(singers[2:])

# Prints from a range of index values in a given list.
print(singers[1:3])

# Prints a list in reverse order
print(singers[::-1])

# The :: indicates a step, and this therefore prints out every second item in the list starting from the first item.
number = list(range(20))
print(number[::2])

#  Using for loops to iterate on a list. Prints each item in a list.
fruits = ['apple', 'orange', 'banana', 'coconut']
for fruit in fruits:
    print(fruit)

# Lists the available attributes and methods of a given object.
fruits = ['apple', 'orange', 'banana', 'coconut']
print(dir(fruits))

# Prints out an avialble help guide on available functions
fruits = ['apple', 'orange', 'banana', 'coconut']
print(help(fruits))

# Prints the length of a given list, or the amount elements.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
print(len(singers))

# Returns a boolean if a given value is inside a list
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
print('れをる' in singers)

# This will print False because it is looking for a string.
numbers = [0,1,2,3,4,5]
print ('1' in numbers)

# Unpacking & packing a lists by assigning multiple variables & using the * designator
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, third, *other= number
print (other)

# Replaces the index value with another value
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
singers[1] = '鈴木里奈'
print(singers[1])

# Extends a list by adding another list to the existing
combined = ['れをる', str(2), True, str(1.256)]
singers.extend(combined)
print(singers)

# Appends a single item to the end of an existing list.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
singers.append('げん')
print(singers)

# Inserts a single list item into a specified index.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
singers.insert(0, 'まみ佐崎')
print(singers)

# Removes a single item from a list
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
singers.remove('ミセカイ')
print(singers)

# Removes a single item from a list using the del designator based on the index value.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
del singers[1]
print (singers)

# Removes a range if items from a list using the del designator based on the index value.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
del singers[2:3]
print (singers)

# Removes/pops the last element of a list.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
singers.pop()
print(singers)

# Checks to see if a certain item is within a list.
# If there are more than one instance, it prints out the first occurrence.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
print(singers.index('みゆな'))

# Counts the amount of instance in a specified value appears inside a list.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
print(singers.count('みゆな'))

# Sorts a list in ascending order. Does not work if the list contains more than one datatype.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
singers.sort()
print(singers)

# Sorts the list in reverse order
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
singers.sort(reverse=True)
print(singers)

# Reverses the order of a list
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
singers.reverse()
print(singers)

# Uses the built-in sort function to sort a list in ascending order into a new list. Does not modify the original.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
print(sorted(singers))

# Uses the built-in sort function to sort a list in reverse order into a new list. Does not modify the original.
singers = ['れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな']
print(sorted(singers, reverse=True))

# Sorting a list of tuples based on a tuple index
items = [
    ('Products 3', 10),
    ('Products 7', 9),
    ('Products 1', 12)
]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print (items)

# Using lambda/anonymous one line function that we can pass into other 03_functions. This is much better than the above method
# The syntax is as such (key=lambda parameters:expression)
items = [
    ('Products 3', 10),
    ('Products 7', 9),
    ('Products 1', 12)
]
print (items)
items.sort(key=lambda item:item[1])
print (items)

# Appending items to a new empty list & printing out that list
items = [
    ('Products 1', 10),
    ('Products 2', 9),
    ('Products 3', 12)
]
prices = []
for item in items:
    prices.append(item[1])
print(prices)

# Creates a copy of a list
singers2 = singers.copy()
singers2.extend(singers)
print(singers2)

# Clears and empties an entire list a list.
singers.clear()
print(singers)

# Prints a range of numbers starting from an index of 0 using the list and range function.
rang = list(range(20))
print (rang)

# Use multiplication to quickly print out a long list of the same item.
zeroes = [0] * 100
print (zeroes)

# Prints all the characters from a list
chars = list('Hello')
print (chars)

# Returns a tuple of the list, which consists of the item & the item’s index. Use the enumerate function if you need
# the index.
letters = ['a', 'b', 'c']
for letter in enumerate(letters):
    print (letter)

# Getting a specific item from a tuple list by calling the index value.
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print (index, letter)


# Querying & fixing stacks
item = []
item.append(1)
item.append(2)
item.append(3)
print (str(item) + '   >>>>>>>>>> This is a list of all the items')
last = item.pop()
print (str(last) + '   >>>>>>>>>> We remove the last item')
print (str(item) + '   >>>>>>>>>> We check the updated list')
print (str(item[-1]) + '   >>>>>>>>>> We check the last item in the list') 
if not item:
    item[-1]
    