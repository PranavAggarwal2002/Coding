with open("Log.txt") as f:
    content = f.read()

if("Python" in content):
    print("Yes Python is Present")
else:
    print("Yes Python is not Present")