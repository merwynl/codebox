"""
Collections = single variable to store multiple values.
List = [] ordered and mutable. Duplicates OK.
Sets = {} unordered and immutable but Add/Remove OK. NO duplicates.
Tuples = () ordered and immutable. Duplicates OK. Faster.
"""

#  Manually creating a set
singers = {'れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな'}
print (singers)

# Using dir function to print the available functions for sets
fruits = {'apple', 'orange', 'banana', 'coconut'}
print (dir(fruits))

# Using help function to print a help guide of available functions.
fruits = {'apple', 'orange', 'banana', 'coconut'}
print (help(fruits))

# Using the set function to turn a list into a set.
numbers = [1,1,2,3,4]
row = set(numbers)
column = {1,5}

# Prints the length of a set
print(len(row))

# A standard set command that gets only the unique items from a list 
print (row)

# Adding an item to a set
column.add(6)
print (column)

# Removing an item to a set
column.add(7)
column.remove(6)
print (column)

# Pops the first element of a set
column.pop()
print(column)

# Clears a set of all elements
column.clear()
print(column)

# Getting the length of a set
print (len(column))

# Joins the values of two sets into a new set
print (row | column)

# Returns the values that exists in both sets
print (row & column)

# Returns the difference between two sets
print (row - column)

# Return the values that exist in all sets but not both.
print (row ^ column)

#  Sets do not support indexing; therefore, this will error.
print(row[0])

# Sets do not support indexing, therefore, run it through a loop if you need to look for an item.
if 3 in row:
    print ('yes')

# Using List comprehension to count the amount occurrences, an item appears in a set.
x = 3
yes = [x for x in row]
print (yes.count(x))

# A simple set comprehension returns a range of 5 values & multiplies them by 2 
values = {x * 2 for x in range(5)}
print (values)