"""
Collections = single variable to store multiple values.
List = [] ordered and mutable. Duplicates OK.
Sets = {} unordered and immutable but Add/Remove OK. NO duplicates.
Tuples = () ordered and immutable. Duplicates OK. Faster.
Tuples should be used on data that you don't want changed/modified.

"""

# A single tuple
coordinates = (4,5)

# Using dir function to print the available functions for sets
singers = ('れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな')
print(dir(singers))

# Using help function to print ta help guide of available functions.
singers = ('れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな')
print(help(singers))

# A list of tuples
listCoordinates = [(4,5), (6,7), (80,34)]
print(coordinates[0])

singers = ('れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな')
numbers = (1,2,3,3,4)

# Printing the length of a tuple
singers = ('れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな')
print(len(singers))

#  Returns a boole if a value is within a tuple
singers = ('れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな')
print ("ミセカイ" in singers)

#  Prints the index of a value inside a tuple. The first occurrence is returned if there are multiples.
singers = ('れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな')
print (singers.index("みゆな"))

# Prints the number of occurrences an item appears inside a tuple.
singers = ('れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな')
print (singers.count("みゆな"))

#  Iterating over a tuple with a for loop
singers = ('れをる', 'みゆな', 'あいみょん', 'ミセカイ', 'みゆな')
for singer in singers:
    print(singer)

# Converts a list into a tuple
point = tuple([1,2])
print(point)

# Converts a string into a tuple
char = tuple('鈴木里奈')
print (char)

# Swapping variables
x = 10
y = 11
x, y = y, x
print ('x', x)
print ('y', y)

# Using the zip function to combine two lists into a tuple
list1 = [1,2,3]
list2 = [10,20,30]
combined = list(zip('abc', list1, list2))
x = [i for i in combined[0:2]]
print (combined)
print (x)
