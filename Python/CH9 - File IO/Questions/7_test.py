with open("Log.txt") as f:
    content = f.readline()
    if("Python" in content):
        print("Yes Python is Present in Line 1")
    else:
        print("Yes Python is not Present in Line 1")

    count = 2

    while(content != ""):
        content = f.readline()
        if("Python" in content):
            print(f"Yes Python is Present in Line {count}")
        else:
            print(f"Yes Python is not Present in Line {count}")
        count += 1