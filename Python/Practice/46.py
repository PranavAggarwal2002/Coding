# Sum of digits of a number 
# Description: Compute the sum of all digits of a given integer. 
# Example: 1234 → 1+2+3+4=10 
def sum_digits(n): 
    return sum(int(d) for d in str(abs(n))) 
 
num = 1234 
print(sum_digits(num)) 