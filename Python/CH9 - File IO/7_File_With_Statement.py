f = open("file6.txt")
print(f.read())
f.close()

# The same can be wriiten using with statement

with open("file6.txt") as v:
    print(v.read()) #You don't have to now add close in extra