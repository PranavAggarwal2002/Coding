def permutation(n, r):
    if r > n:
        return "Invalid input"
    
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    return result

n = int(input("Enter Number of people : "))
r = int(input("Enter Number of seats : "))
print(permutation(n, r))