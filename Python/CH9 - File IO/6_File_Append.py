st = " Beauxbatons and Durmstrang"

f = open("file4.txt", "a")
# This will add the line again & again and one time for every time we excecute the code

f.write(st)
f.close()

f = open("file5.txt", "w") 
# This will only write once and even if we excecute code how mnay time

f.write(st)
f.close()