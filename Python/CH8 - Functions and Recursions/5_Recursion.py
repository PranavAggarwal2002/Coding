# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# n = int(input("Enter Your Number : "))
# print(f"the facotiral of {n} is : {factorial(n)}")

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)
n = int(input("Enter Your Number : "))
print(f"the facotiral of {n} is : {factorial(n)}")

# Below code is wrongg as this function willcwall it self infinitely in negative  
# def factorial(n):
#     return n*factorial(n-1)
# n = int(input("Enter Your Number : "))
# print(f"the facotiral of {n} is : {factorial(n)}")