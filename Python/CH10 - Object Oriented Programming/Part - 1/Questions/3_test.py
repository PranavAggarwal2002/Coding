class Demo:
    a = 4

o = Demo()
print(o.a) # Print class attribute because instance is not present
o.a = 0 # Instance attribute is set
print(o.a)  # Print instance attribute because instance is present
print(Demo.a) # Class atrribute is not changed