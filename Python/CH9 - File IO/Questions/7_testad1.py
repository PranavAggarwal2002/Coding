with open("Log.txt") as f:

    count = 1

    while True:
        content = f.readline()

        if content == "":
            break

        if "Python" in content:
            print(f"Python is present in line {count}")
        else:
            print(f"Python is not present in line {count}")

        count += 1

with open("Log.txt") as f:

    count = 1

    while True:
        content = f.readline()

        if content == "":
            break

        if content.strip() == "":
            count += 1
            continue

        if "Python" in content:
            print(f"Python is present in line {count}")

        count += 1