a = (1,45,342,3424,False,"Rohan","Shivam")
print(a)
no = a.count(45)
print(no)
a = (1,45,342,3424,False,45,"Rohan","Shivam")
no = a.count(45)
print(no)

i = a.index(3424)
print(i)
print(len(a))

my_tuple = (1,2,3)
a,b,c = my_tuple
print(a,b,c)