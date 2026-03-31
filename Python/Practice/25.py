# Maximum and Minimum digit in a number 
# Find the largest and smallest digit in a given integer. 
# Example 4825 → max=8, min=2 
def max_min(n):
    a = []
    n = abs(n)
    digit = 0
    if n == 0:
        return(0,0)
    
    while(n>0):
        digit = n%10
        n //= 10
        a.append(digit)
    return(max(a),min(a))
n = int(input("Enter Your Number : "))
print(max_min(n))
