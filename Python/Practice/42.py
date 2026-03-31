# Check if a number is Harshad number 
# A Harshad (or Niven) number is divisible by the sum of its digits. 
# 18 → sum=9, 18%9=0 → true, 19 → sum=10, 19%10≠0 → false 

def sum_digit(n):
    z = n
    total = 0
    while(z>0):
        total = total + z%10
        z //= 10
    return total
def harshad_number(n):
    y = sum_digit(n)
    if(n%y==0):
        print("true")
    else:
        print("false")

n = int(input("Enter the Number : "))
harshad_number(n)