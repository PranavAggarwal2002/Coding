f = open("file3.txt")

line = f.readline()
while(line !=""):
    print(line)
    line = f.readline()

f.close()