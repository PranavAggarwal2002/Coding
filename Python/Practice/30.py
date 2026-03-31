def power(base, exp): 
    result = 1 
    for _ in range(exp):
        result *= base
    return result

base, exp = 12, 3 
print(power(base, exp))