# Check whether a given number is positive or negative
#  Determine if a number is positive, negative, or zero. 
def pnz(n):
    if n>0:
        print("Positive")
    elif n<0:
        print("Negative")
    else:
        print("Zero")

n = float(input("Enter Your Number : "))
pnz(n)