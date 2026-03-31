def sum_digit(n):
    z = n
    total = 0
    while z > 0:
        total += z % 10
        z //= 10
    return total

def harshad_number(n):
    if n == 0:
        return False
    
    s = sum_digit(n)
    return n % s == 0

n = int(input("Enter the Number : "))

if harshad_number(n):
    print("true")
else:
    print("false")