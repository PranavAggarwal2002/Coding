# Replace all 0s with 1s in a given integer 
# Description: Replace every digit 0 in a number with 1. 
# Example: 1020 → 1121
def replace_zero(n):
    if n == 0:
        return 1

    result = 0
    place = 1

    while n > 0:
        digit = n % 10
        
        if digit == 0:
            digit = 1
        
        result = digit * place + result
        place *= 10
        n //= 10

    return result