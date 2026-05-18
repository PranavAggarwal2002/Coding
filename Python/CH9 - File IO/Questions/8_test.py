with open("Test8.txt") as f:
    
    with open("TestCopy.txt", "w") as t:

        for line in f:
            t.write(line)

with open("Test8.txt") as f:
    data = f.read()

with open("TestCopy2.txt", "w") as t:
    t.write(data)