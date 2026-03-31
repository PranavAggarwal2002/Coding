# mine
def greatest():
    a = int(input("Enter Your Number a : "))
    b = int(input("Enter Your Number b : "))
    c = int(input("Enter Your Number c : "))
    if(a>b and a>c):
        return(f"a is greatest {a}")
    elif(b>a and b>c):
        return(f"b is greatest {b}")
    elif(c>a and c>b):
        return(f"c is greatest {c}")
    else:
        return(f"All number are equal {a}")
    
print(greatest())

# Harry Bhai Code
def greatest(a,b,c):
    if(a>b and a>c):
        return(f"a is greatest {a}")
    elif(b>a and b>c):
        return(f"b is greatest {b}")
    if(c>a and c>b):
        return(f"c is greatest {c}")
    
a = int(input("Enter Your Number a : "))
b = int(input("Enter Your Number b : "))
c = int(input("Enter Your Number c : "))
print(greatest(a,b,c))