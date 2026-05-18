# import os

# current_dir = os.path.dirname(__file__)
# file_path = os.path.join(current_dir, "file.txt")

# with open(file_path, "r") as f:
#     data = f.read()

# print(data)

f = open("file.txt") 
# while it should be written as f = open("file.txt", "r") and f = open("file.txt", "w") for reading and writing 
# but since default mode of open is already read so f = open("file.txt") works for read but for writing f = open("file.txt", "w")
data = f.read()
print(data)
f.close() # close the file if this file is accessedby some other program, it's data is not changes
# while it is not necessary to add f.close() but still recommended