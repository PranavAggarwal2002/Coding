def divisor(n):
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            print(i)
            if i != n // i:
                print(n // i)

n = int(input("Enter the Number : "))
divisor(n)

def divisor(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

n = int(input("Enter the Number : "))
print(divisor(n))