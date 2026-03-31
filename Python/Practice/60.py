
# function to find gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# input
s = input().strip()   # example: "1/2 3/4"

f1, f2 = s.split()

a, b = map(int, f1.split('/'))
c, d = map(int, f2.split('/'))

# add fractions
num = a*d + b*c
den = b*d

# simplify
g = gcd(num, den)

num //= g
den //= g

print(str(num) + "/" + str(den))