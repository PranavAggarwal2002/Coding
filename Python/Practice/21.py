# Leap Year or not
# A leap year is divisible by 4 but not by 100, unless also divisible by 400.
# 2000 → true, 1900 → false, 2024 → true
def leap_year(n):
    if(n%100==0):
        if(n%400==0):
            return("Leap")
        else:
            return
    elif(n%4==0 and n%100!=0):
        return("Leap")
    
n = 2480
print(leap_year(n))