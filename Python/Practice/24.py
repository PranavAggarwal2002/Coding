def reverse_number(n): 
    rev = 0 
    sign = -1 if n < 0 else 1 
    n = abs(n) 
    while n > 0: 
        rev = rev * 10 + n % 10 
        n //= 10 
    return sign * rev 
num = 0 
print(reverse_number(num)) 