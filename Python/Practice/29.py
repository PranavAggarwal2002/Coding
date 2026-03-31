# Power of a number
# Compute base raised to exponent (positive integer exponent). 
# 2^3 = 8 
def power(n,a):
    return n**a
n, a = map(int, input("Enter N and A : ").split())
print(power(n,a))