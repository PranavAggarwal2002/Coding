# Check if a Number is Automorphic 
# An automorphic number is a number whose square ends with the number itself. 
#  5² = 25 → ends with 5 → true, 6² = 36 → ends with 6 → true, 7² = 49 → false 
def automorphic(n):
    dig = n**2
    z = n 
    count = 0
    while(z>0):
        z //= 10
        count += 1
    
    if dig % (10 ** count) == n:
        print("True")
    else:
        print("False")

n = int(input("Enter the Number : "))
automorphic(n)