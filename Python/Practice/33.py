# Print all prime factors of the given number
# List all prime factors (with multiplicity) of a number. 
# 60 → 2, 2, 3, 5
def prime_factors(n):
    factors = []
    
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    return factors

n = int(input("Enter the Number : "))
print(prime_factors(n))