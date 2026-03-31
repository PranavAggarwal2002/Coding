# Reverse digits of a number 
# Reverse the digits of an integer. Handle negative numbers by preserving the sign. 
#  123 → 321, -456 → -654 
def rev(n):
    reverse_number = 0
    digit = 0
    if(n==0):
        return reverse_number
    elif(n<0):
        n = -n
        while(n>0):
            digit = n % 10
            reverse_number = (reverse_number*10) + digit
            n = n // 10
        return(-reverse_number)
    else:
        while(n>0):
            digit = n % 10
            reverse_number = (reverse_number*10) + digit
            n = n // 10
        return reverse_number
    
n = int(input("Enter tHe Number : "))
print(rev(n))