with open("Test11.txt") as f:
    data = f.read()

with open("Test11_remnamed_by_python.txt", "w") as f:
    f.write("data")

import os

old_name = "oldfile.txt"
new_name = "newfile.txt"

os.rename(old_name, new_name)

print("File renamed successfully")

import os

old_name = "Test.txt"
new_name = "Python.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed successfully")
else:
    print("File does not exist")

'''
shutil is mainly for:

copying files
moving files
deleting directory trees

However, shutil.move() can also rename a file.
'''
import shutil

old_name = "Test.txt"
new_name = "Python.txt"

shutil.move(old_name, new_name)

print("File renamed successfully")


import shutil
import os

if os.path.exists("Test.txt"):
    shutil.move("Test.txt", "Python.txt")
    print("Renamed")
else:
    print("File not found")