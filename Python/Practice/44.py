# Check if the number is abundant number or not 
# An abundant number is less than the sum of its proper divisors (excluding itself).
# 12 → proper divisors: 1,2,3,4,6 → sum=16 > 12 → true, 8 → divisors: 1,2,4 → sum=7 < 8 → false

def divisor_sum(n):
    total = 0
    for i in range(1,n):
        if(n%i==0):
            total += i
    return total

def compare(n):
    d = divisor_sum(n)
    if(d>n):
        print("true")
    else:
        print("false")

n = int(input("Enter Your Number : "))
compare(n)