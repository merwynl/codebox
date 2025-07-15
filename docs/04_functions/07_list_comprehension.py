"""
Comprehension = A concise way to create sets, lists & dictionaries in python
                Compact & easier to read than traditional loops
                [expression for value in iterable if condition]
"""

import random

# Standard for-loop for printing even numbers
doubles = []
for x in range(1,11):
    doubles.append(x * 2)
print(doubles)

# Using list comprehension to perform the above operation
doubles = [x * 2 for x in range(1,11)]
print(doubles)

# Using list comprehension to print out a list range of values with a multiplication factor of 3
triples = [y * 3 for y in range (1,11)]
print(triples)

# Using list comprehension to create a squares of values
suqares = [pow(z, 2) for z in range(1,11)]
print(suqares)

# Using list comprehension to create a cube of values
cubes = [z * z * z for z in range(1,11)]
print(cubes)

# Using list comprehension to create a cube of values using pow function
cubes = [pow(z, 3)for z in range(1,11)]
print(cubes)

# Using list comprehension to convert string values into uppercase
fruits = ['apple', 'orange', 'banana', 'coconut']
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

# Using list comprehension to capitalize string values
fruits = ['apple', 'orange', 'banana', 'coconut']
fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)

# Using list comprehension to store the first character of every string in a list.
fruits = ['apple', 'orange', 'banana', 'coconut']
fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)

# Returns a positive list of numbers
numbers = [1,-2,3,-4,5,-6]
positive_nums = [num for num in numbers if num>=0]
print(positive_nums)

# Returns a list of negative values using list comprehension
numbers = [1,-2,3,-4,5,-6]
negative_numbers = [num for num in numbers if num <=0]
print(negative_numbers)

# Checks to see if there are even numbers
numbers = [1,-2,3,-4,5,-6,-7, 8, 9, 12,-15]
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

# Checks to see if there are odd numbers
numbers = [1,-2,3,-4,5,-6,-7, 8, 9, 12,-15]
odd_nums = [num for num in numbers if num % 2 > 0]
print(odd_nums)

# Prints a list of passing grades if a grade value is above a certain condition.
grades = [82, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade > 50]
print(passing_grades)


# Using list comprehension to perform the above operation
doubles = [x * 2 for x in range(1,11)]
print(doubles)

# Using list comprehension to print out a list range of values with a multiplication factor of 3
triples = [y * 3 for y in range (1,11)]
print(triples)

# Using list comprehension to create a squares of values
suqares = [pow(z, 2) for z in range(1,11)]
print(suqares)

# Using list comprehension to create a cube of values
cubes = [z * z * z for z in range(1,11)]
print(cubes)

# Using list comprehension to create a cube of values using pow function
cubes = [pow(z, 3)for z in range(1,11)]
print(cubes)

# Using list comprehension to convert string values into uppercase
fruits = ['apple', 'orange', 'banana', 'coconut']
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

# Using list comprehension to capitalize string values
fruits = ['apple', 'orange', 'banana', 'coconut']
fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)

# Using list comprehension to store the first character of every string in a list.
fruits = ['apple', 'orange', 'banana', 'coconut']
fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)

# Returns a positive list of numbers
numbers = [1,-2,3,-4,5,-6]
positive_nums = [num for num in numbers if num>=0]
print(positive_nums)

# Returns a list of negative values using list comprehension
numbers = [1,-2,3,-4,5,-6]
negative_numbers = [num for num in numbers if num <=0]
print(negative_numbers)

# Checks to see if there are even numbers
numbers = [1,-2,3,-4,5,-6,-7, 8, 9, 12,-15]
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

# Checks to see if there are odd numbers
numbers = [1,-2,3,-4,5,-6,-7, 8, 9, 12,-15]
odd_nums = [num for num in numbers if num % 2 > 0]
print(odd_nums)

# Prints a list of passing grades if a grade value is above a certain condition.
grades = [82, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade > 50]
print(passing_grades)

'''
Set Comprehension
'''

# Using set comprehension to perform the above operation
doubles = {x * 2 for x in range(1, 11)}
print(doubles)

# Using set comprehension to print out a list range of values with a multiplication factor of 3
triples = {y * 3 for y in range(1, 11)}
print(triples)

# Using set comprehension to create a squares of values
suqares = {pow(z, 2) for z in range(1, 11)}
print(suqares)

# Using set comprehension to create a cube of values
cubes = {z * z * z for z in range(1, 11)}
print(cubes)

# Using set comprehension to create a cube of values using pow function
cubes = {pow(z, 3) for z in range(1, 11)}
print(cubes)

# Using set comprehension to convert string values into uppercase
fruits = {'apple', 'orange', 'banana', 'coconut'}
fruits = {fruit.upper() for fruit in fruits}
print(fruits)

# Using set comprehension to capitalize string values
fruits = {'apple', 'orange', 'banana', 'coconut'}
fruits = {fruit.capitalize() for fruit in fruits}
print(fruits)

# Using set comprehension to store the first character of every string in a list.
fruits = {'apple', 'orange', 'banana', 'coconut'}
fruit_char = {fruit[0] for fruit in fruits}
print(fruit_char)

# Returns a positive set of numbers.
numbers = {1, -2, 3, -4, 5, -6}
positive_nums = {num for num in numbers if num >= 0}
print(positive_nums)

# Returns a set of negative values using set comprehension
numbers = {1, -2, 3, -4, 5, -6}
negative_numbers = [num for num in numbers if num <=0]
print(negative_numbers)

# Checks to see if there are even numbers in a set.
numbers = {1, -2, 3, -4, 5, -6, -7, 8, 9, 12, -15}
even_nums = {num for num in numbers if num % 2 == 0}
print(even_nums)

# Checks to see if there are odd numbers in a set.
numbers = {1, -2, 3, -4, 5, -6, -7, 8, 9, 12, -15}
odd_nums = [num for num in numbers if num % 2 > 0]
print(odd_nums)

# Prints a set of passing grades if a grade value is above a certain condition.
grades = {82, 42, 79, 90, 56, 61, 30}
passing_grades = {grade for grade in grades if grade > 50}
print(passing_grades)

'''
Dictionary Comprehension
'''
# Using dictionary comprehension to print out even number
values = {x: x * 2 for x in range(1,11)}
print(values)

# Using dictionary comprehension to assign a random fruit to a person.
students = ["Spot", "John", "Ken", "Lisa"]
fruits = ['apple', 'orange', 'banana', 'coconut']
fruits = {student:random.choice(fruits) for student in students}
print(fruits)

# Using dictionary comprehension to assign a random number to a person.
students = ["Spot", "John", "Ken", "Lisa"]
number = {student: random.randint(1, len(students)) for student in students}
print(number)


