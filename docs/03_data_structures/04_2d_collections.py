"""
Collections = single variable to store multiple values.
List = [] ordered and mutable. Duplicates OK.
Sets = {} unordered and immutable but Add/Remove OK. NO duplicates.
Tuples = () ordered and immutable. Duplicates OK. Faster.
Tuples should be used on data that you don't want changed/modified.
2dLists = A list containing other lists.
"""

# Each category of food can be considered a row with each item inside a list representing a column
fruits =     ['apple', 'orange', 'banana', 'coconut']
vegetables = ['brocoli', 'lettuce', 'carrots', 'celery']
meats =      ['fish', 'turkey', 'chicken', 'beef']

#  Manually creating a 2d list
groceries = [fruits, vegetables, meats]
# print(groceries)

# Uses a 2nd indices to print the 2nd element of the first list
print(groceries[0][2])

#  Prints the last element of the last list
print(groceries[2][3])

#  Prints the 2nd element of the 2nd list
print(groceries[1][1])

# Alternate way of writing a list. Separate each list through a comma
groceries = [['apple', 'orange', 'banana', 'coconut'],
             ['brocoli', 'lettuce', 'carrots', 'celery'],
             ['fish', 'turkey', 'chicken', 'beef']]

#  Using a for loop to print the outer list
for collection in groceries:
    print(collection)

# Prints every single element within a 2dlist
groceries = [['apple', 'orange', 'banana', 'coconut'],
             ['brocoli', 'lettuce', 'carrots', 'celery'],
             ['fish', 'turkey', 'chicken', 'beef']]

for collection in groceries:
    for food in collection:
        print(food)

# Prints every single element within a 2dlist in a grid
groceries = [['apple', 'orange', 'banana', 'coconut'],
             ['brocoli', 'lettuce', 'carrots', 'celery'],
             ['fish', 'turkey', 'chicken', 'beef']]

for collection in groceries:
    for food in collection:
        print(food.capitalize(), end=" ")
    print()

# A 2d tuple made up of separate lists
groceries = (['apple', 'orange', 'banana', 'coconut'],
             ['brocoli', 'lettuce', 'carrots', 'celery'],
             ['fish', 'turkey', 'chicken', 'beef'])

for collection in groceries:
    for food in collection:
        print(food.capitalize(), end=" ")
    print()

# A 2d tuple made up of separate sets
groceries = ({'apple', 'orange', 'banana', 'coconut'},
             {'brocoli', 'lettuce', 'carrots', 'celery'},
             {'fish', 'turkey', 'chicken', 'beef'})

for collection in groceries:
    for food in collection:
        print(food.capitalize(), end=" ")
    print()

# Printing every row in a 2d tuple
numpad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*",0,"#") )
for row in numpad:
    print(row)

# Printing a numpad grid
numpad = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"))
for row in numpad:
    for num in row:
        print(num, end=" ")
    print()