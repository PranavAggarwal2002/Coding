with open("Log.txt") as f:
    count = 1
    for line in f:
        if "Python" in line:
            print(f"Python present in line {count}")
            break
        count = count + 1

    else:
        ("Python not present in any of the line")