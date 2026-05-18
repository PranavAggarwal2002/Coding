with open("Log.txt") as f:

    count = 1

    for line in f:
        if "Python" in line:
            print(f"Python is present in line {count}")
        else:
            print(f"Python is not present in line {count}")

        count += 1

with open("Log.txt") as f:

    count = 1

    for line in f:
        if "Python" in line:
            print(f"Python found in line {count}")
            print(line)

        count += 1