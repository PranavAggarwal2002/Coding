def max_min_digit(n): 
    n = abs(n) 
    digits = [int(d) for d in str(n)] 
    print(f"Max: {max(digits)}, Min: {min(digits)}") 

num = 4825 
max_min_digit(num) 