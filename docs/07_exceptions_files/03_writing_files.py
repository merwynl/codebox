
'''

Writing Files (.txt, .json, .csv)

# With statement wraps some code around it, primarily for managing resources, files & iterators.
# Closes a file when we are done otherwise a .close() will be needed.
# Not closing a file can lead to unexpected behaviour.
# open (file, mode)
        # w = write. Opens a file for reading. Create the file if it does not exist.
        # a = append. Opens a file for appending. Create the file if it does not exist.
        # x = create. Errors if a file already exists.
        # r = read/opens a file. Error if the file does not exist.
'''

import json
import csv

txt_data = "I like Pizza! "
file_path = "files/output.txt"
absolute_file_path = "H:\\git-dev\\codebox\\docs\\07_exceptions_files\\files\\output.txt"
colors = ["blue", "red", "yellow", "black", 'white', "purple", "green"] # Lists can't be written directly


# Writing to a file with a relative path
with open(file=file_path, mode="w") as file:
    file.write(txt_data + "\n" )
    print(f"txt file '{file_path}' created.")

# Creating a file
try:
    with open(file=absolute_file_path, mode="x") as file:
        file.write(txt_data + "\n" )
        print(f"txt file '{file_path}' created.")
except FileExistsError:
    print("That file already exists!")

# Appending to a file/Edit file. Any new data will be added to that file.
try:
    with open(file=absolute_file_path, mode="a") as file:
        file.write(txt_data + "\n" ) # Appending a new line to text data
        print(f"txt file '{file_path}' appended.")
except FileExistsError:
    print("That file already exists!")

# Writing a collection to a file.
try:
    with open(file=absolute_file_path, mode="a") as file:
        for color in colors:
            file.write(color.capitalize() + "\n" ) # Appending a new line to text data
            print(f"{color.capitalize()} colour added to '{file_path}'.")
except FileExistsError:
    print("That file already exists!")

# Writing to a JSON file
student = {
        "name": "Adam",
        "age": 27,
        "year": 2024,
        "major": "Architecture",
        "gpa": 3.5,
        "is_on_probation": False,
}
file_path = "files/students.json"
try:
    with open(file=file_path, mode="w") as file:
        # Takes our dictionary data and passes it as a JSON string with indentation.
        json.dump(student, file, indent=4)
        print(f"JSON file created at'{file_path}'.")
except FileExistsError:
    print("That file already exists!")

# Writing to a CSV (Comma separated values) file
students = [["Name", "Age", "Year", "Major", "GPA", "On Probation"],
            ["Adam", 27, 2024, "Anthropology", 3.5, True],
            ["Ken", 22, 2022, "Computer Science", 4.0, False],
            ["Sara", 23, 2019, "Literature", 3.75, False]
            ]
file_path = "files/students.csv"

try:
    # Newline "" argument addded to prevent extra new line
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file) # Writing to a file

        # Iterating on rows of data to add to the file. Otherwise returns blank.
        for row in students:
            writer.writerow(row)
        print(f"CSV file created at'{file_path}'.")
except FileExistsError:
    print("That file already exists!")
