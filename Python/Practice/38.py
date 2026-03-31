# GCD of two numbers 
# Find the greatest common divisor (GCD) of two integers.
# GCD(12, 18) = 6
def gcd(a, b):
    g = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            g = i
    return g

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(gcd(a, b))