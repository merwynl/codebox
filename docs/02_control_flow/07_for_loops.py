"""
Executes a block of code a fixed amount times. Can iterate over a range, string sequence, etc.
"""

# Counts from numbers 1 and stops at 10, 11 is excluded.
for x in range(1,11):
    print(x)

# Reverse counting a range
for x in reversed(range(1,11)):
    print(x)
print("Begin! ")

# Using the step function to count backwards
for x in range(11,0,-1):
    print(x)
print("Times up!")

# Counts every 2nd number from 1 to 10
for x in range(1,11, 2):
    print(x)

# Counts every 3rd number from 1 to 10
for x in range(1,11, 3):
    print(x)

# Iterates over a string
credit_number = "1234-5678-9012-3456"
for x in credit_number:
    print(x)

# Skips over an iteration value of 13 then continues.
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)

# Breaks out of a loop when we reach a specified number. That number is not printed.
for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)

# Prints each character/letter in the given string
word = '東京市大学院'
for letter in word:
    print(letter)

# For each item in the list, that item gets printed out.
songs = ['ミラージュ', '劣等上等', 'サイサキ']
for music in songs:
    print(music)

# Prints each single numbered value up to a specific value index.
for index in range(10):
    print(index)

# Prints each single numbered value based on a given range
for i in range(3, 15):
    print('The value for i is ' + str(i))

# Prints out all the elements in that list based on its index value.
songs = ['ミラージュ', '劣等上等', 'サイサキ']
for index in range(len(songs)):
    print(songs[index])

# Prints out the index value of each item in the list.
songs = ['ミラージュ', '劣等上等', 'サイサキ']
for index in range(len(songs)):
    print(index)

# Prints out the index value of each item in the list.
songs = ['ミラージュ', '劣等上等', 'サイサキ']
for index in range(len(songs)):
    if index == 0:
        print('First Track = ' + str(songs[index]))
    elif index == 1:
        print('Second Track = ' + str(songs[index]))
    else:
        print('Unknown Track = ' + str(songs[index]))

# Lists contained within a list. Each new list can be treated as a row and column.
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# For each row in the list, gets each column and for each value in each column, prints out that element.
for row in number_grid:
    for column in row:
        print(column)

# Returns a tuple of the list which consists of the item & the item's index
letters = ['a', 'b', 'c']
for letter in enumerate(letters):
    print (letter)

# Getting a specific item from a tupled list by calling the index value
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print (index, letter)

