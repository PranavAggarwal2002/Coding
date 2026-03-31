# Check if a number is perfect number 
# A perfect number equals the sum of its proper positive divisors (excluding itself). 

def perfect_number(n):
    if(n<=1):
        return
    original = n
    rev = 0
    for i in range(1,n):
        if(n%i==0):
            rev += i
    print(rev==original)
a = int(input("Enter the Number : "))
perfect_number(a)