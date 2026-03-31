a = int(input())
b = int(input())
c = int(input())
d = int(input())

num = a*d + b*c
den = b*d

# gcd
x, y = num, den
while y != 0:
    x, y = y, x % y

num //= x
den //= x

print(num, "/", den)