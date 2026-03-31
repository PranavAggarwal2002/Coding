# Factors of a given number 
# Print all positive divisor of a number
def divisor(n):
    g = []
    for i in range(1,n+1):
        if n%i==0:
            g.append(i)
    return g
n = int(input("Enter the Number : "))
print(divisor(n))