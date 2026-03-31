# Print Fibonacci upto Nth Term 
# Generate Fibonacci sequence up to N terms (starting from 0, 1). 
# Example: N=7 → 0, 1, 1, 2, 3, 5, 8

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a,b = b, a+b
n = int(input("Enter The value till where : "))
fibonacci(n)