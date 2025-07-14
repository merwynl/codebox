"""
Nested loops: A loop within another loop (outer, inner)
for x in y:
    for a in b:

"""

# Repeats the inner loop 3 times
for x in range(3):
    for y in range(1,10):
        print(y, end=" ")  # Printing all the results of x on the same line

# Repeats the inner loop 3 times. Adds an empty print to the outer loop as a linebreak
for x in range(3):
    for y in range(1,10):
        print(y, end=" ")  # Printing all the results of x on the same line
    print()

# Repeats the inner loop 3 times. Prints each character on an individual line/
for x in range(3):
    for y in range(1,10):
        print(y, end="\n")  # Printing all the results of x on the same line

#  Prints a specified amount of column and row of symbols.
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")  # Printing all the results of x on the same line
    print()

# Lists contained within a list. Each new list can be treated as a row and column
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# For each row in the list, gets each column and for each value in each column, prints out that element
for row in number_grid:
    for column in row:
        print(column)
