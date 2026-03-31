# Program to add two fractions 
# Description: Add two fractions a/b and c/d, and output the result in simplified form (numerator/denominator). 
# Example: 1/2 + 2/3 = 7/6 
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def add_fraction(a, b, c, d):
    num = a * d + b * c      # numerator
    den = b * d              # denominator

    g = gcd(num, den)        # simplify
    num = num // g
    den = den // g

    return num, den

a = int(input("Enter numerator 1: "))
b = int(input("Enter denominator 1: "))
c = int(input("Enter numerator 2: "))
d = int(input("Enter denominator 2: "))

n, d = add_fraction(a, b, c, d)
print(n, "/", d)