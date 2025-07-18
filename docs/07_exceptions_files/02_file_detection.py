
'''

File Detection

'''

# Import operating system module
import os

# File paths can be detected using relative or absolute paths.
# When working with string paths, use double-backslash or forward slash.
# Otherwise, Python will recognize it as escape sequences.
relative_file_path = "files/text.txt "
file_path = "files"
absolute_file_path = "H:\\git-dev\\codebox\\docs\\07_exceptions_files\\files\\text.txt"

# Checks to see if file from a relative file path exists.
if os.path.exists(relative_file_path):
    print(f"File exists in '{relative_file_path}'")
    if os.path.isfile(file_path):
        print(f"File exists in '{file_path}'")
    elif os.path.isdir(file_path):
        print(f"{file_path.capitalize() } is a directory not a file.")

else:
    print(f"File does not exist.")

# Checks to see if file from a relative file path exists.
if os.path.exists(absolute_file_path):
    print(f"File exists in '{absolute_file_path}'")
else:
    print(f"File does not exist.")