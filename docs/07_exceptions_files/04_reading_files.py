
'''

Reading Files (.txt, .json, .csv)

'''

import json
import csv

file_path = "files/input.txt"
abs_file_path = "H:\\git-dev\\codebox\\docs\\07_exceptions_files\\files\\inpur.txt"

# Reading a txt file from a relative file path. Using a Try/Except to catch if a file does not exist.
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"File read from {file_path}")
        print(content)
except FileNotFoundError:
    print("That file does not exists!")

# Reading a txt file from an absolute file path
try:
    with open(abs_file_path, 'r') as file:
        content = file.read()
        print(f"File read from {file_path}")
        print(content)
except FileNotFoundError:
    print("That file does not exists!")
except PermissionError:
    print("Permission to access that file denied!")

# Reading from a JSON file
file_path = "files/input.json"
try:
    with open(file_path, 'r') as file:
        content = json.load(file)
        print(f"File read from {file_path}")
        print(content["name"]) # Printing a specific key from a json file
        print(content.keys()) # Printing all the keys.
        print(content.values())  # Printing all the values.
except FileNotFoundError:
    print("That file does not exists!")
except PermissionError:
    print("Permission to access that file denied!")

# Reading from a CSV file
file_path = "files/input.csv"
try:
    with open(file_path, 'r') as file:
        content = csv.reader(file)
        print(f"File read from {file_path}")
        for line in content:
            # print(line) # Printing each line in a csv
            # print(line[4])  # Specifying an index to print a specific column
            print(line[1])  # Specifying an index to print a specific column

except FileNotFoundError:
    print("That file does not exists!")
except PermissionError:
    print("Permission to access that file denied!")