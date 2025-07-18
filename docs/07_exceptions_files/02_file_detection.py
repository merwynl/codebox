
'''

File Detection

'''

# Import operating system module
import os

# File paths can be detected using relative or absolute paths.
# When working with string paths, use double-backslash or forward slash.
# Otherwise, Python will recognize it as escape sequences.
relative_file_path = "files/text.txt"
file_path = "files"
absolute_file_path = "H:\\git-dev\\codebox\\docs\\07_exceptions_files\\files\\text.txt "

# Checks to see if file from a relative file path exists.
if os.path.exists(relative_file_path):
    print(f"Relative file path: File exists in '{relative_file_path}'")
else:
    print(f"Relative file path: File does not exist.")

# Checks to see if file from a relative file path exists.
if os.path.exists(absolute_file_path):
    print(f"Abs File Path: File exists in '{absolute_file_path}'")
else:
    print(f"Abs File Path: File does not exist.")

# Checks to see if a given string is a file or a directory
if os.path.exists(file_path):
    if os.path.isfile(file_path):
        print(f"Is file: File exists in '{file_path}'")
    elif os.path.isdir(file_path):
        print(f"Directory: {file_path.capitalize() } is a directory not a file.")
else:
    print(f"File does not exist.")