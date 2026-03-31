# Factorial of a number
# Compute factorial of a non-negative integer n (n!). 
# 5! = 120
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

n = int(input("Enter The Number : "))
print(factorial(n))

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n*factorial(n-1)
# n = int(input("Enter Your Number : "))
# print(f"the facotiral of {n} is : {factorial(n)}")