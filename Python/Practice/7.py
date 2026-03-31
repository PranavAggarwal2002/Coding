def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True


a = int(input("Enter starting number(L): "))
b = int(input("Enter ending number(R): "))

count = 0
n = []

for i in range(a, b + 1):
    if is_prime(i):
        n.append(i)
        count += 1

print("Total prime numbers:",n,count)