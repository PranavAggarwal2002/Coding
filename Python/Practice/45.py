def is_abundant(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total > n

n = int(input("Enter Your Number : "))
print(is_abundant(n))