# Arithmetic operators: +, -, *, / etc.
a=34
b=7
c=a+b
d=a*b
print(c)
# Assignment operators:  =, +=, -= etc. 
e=4-2 #Assign 4-2 to e
f=5
f+=3
print(e, f)
# Comparison operators: ==, >, >=, <,  != etc. 

g = 5 < 4 
print(g) #False
h = 5 > 4
print(h) #True
g = 5 <= 5
print(g) #True
g = 5 != 7
print(g) #True
g = 5 == 5
print(g) #True
g = 5 != 5
print(g) #False
# Logical operators: and, or, not. 

i = True or False
print(i)
i = True and False
print(i)

print('-----')

#Truth Table of 'or'
print("True or False is", True or False)
print("True or True is", True or True)
print("False or True is", False or True)
print("False or False is", False or False)

#Truth Table of 'and'
print("True and False is", True and False)
print("True and True is", True and True)
print("False and True is", False and True)
print("False and False is", False and False)

print(not(True))