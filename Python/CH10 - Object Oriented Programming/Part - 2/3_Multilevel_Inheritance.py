class Employee:
    a = 1
    
class Coder(Employee):
    b = 2

class Programmer(Coder):
    c = 3

o = Employee()
print(o.a)
# print(o.b)  will give error as no b in Employee
o = Coder()
print(o.a, o.b)
o = Programmer()
print(o.a, o.b, o.c)