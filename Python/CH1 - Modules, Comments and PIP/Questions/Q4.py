'''Write a python program to print the contents of a directory using the os module. 
Search online for the function which does that.'''

import os

# Specify the directory path
directory_path =  "/"  # replace this with the actual path

try:
    # Get list of files and subdirectories
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The specified directory does not exist.")
except PermissionError:
    print("Error: Permission denied accessing the directory.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
