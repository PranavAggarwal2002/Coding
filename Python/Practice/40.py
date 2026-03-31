# LCM of two numbers 
# Description: Find the least common multiple (LCM) of two integers. 
# Example: LCM(12, 18) = 36 
def lcm(a,b):
    g = 0
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            g = i
    return((a*b)/g)
a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))

print(int(lcm(a,b)))