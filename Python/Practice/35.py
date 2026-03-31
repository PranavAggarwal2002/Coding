# Check if a number is a strong number or not
# A strong number is a number where the sum of the factorials of its digits equals the number itself.
# Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145 → true 
def factorial(n):
    fac = 1
    for i in range(2,n+1):
        fac *= i
    return fac

def strong_number(n):
    rev = 0
    z = n
    while(n>0):
        dig = n%10
        rev += factorial(dig)
        n //= 10
    if(rev==z):
        print("Strong Number")
    else:
        print("Not A Strong Number")

n = int(input("Enter The Number : "))
strong_number(n)

