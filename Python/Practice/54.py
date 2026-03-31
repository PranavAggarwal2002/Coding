def replace_zeros(n): 
    if n == 0: 
        return 1 
    result = 0 
    place = 1 
    while n > 0: 
        digit = n % 10 
        if digit == 0: 
            digit = 1 
        result += digit * place 
        place *= 10 
        n //= 10 
    return result 

print(replace_zeros(1020))