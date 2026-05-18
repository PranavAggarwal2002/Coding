with open("Test8.txt") as f:
    data = f.read()

with open("Test8p.txt") as t:
    data1 = t.read()

    if data == data1 :
        print("true, file identical")
    else:
        print("false, file not identical")