# function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# function to find nth prime
def nth_prime(n):
    count = 0
    num = 1
    
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
            
    return num

# input
x, y = map(int, input().split())

# find primes
A = nth_prime(x)
B = nth_prime(y)

# result
C = (A + B) - 1

print(C)