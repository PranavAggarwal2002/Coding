def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))

print(lcm(a, b))