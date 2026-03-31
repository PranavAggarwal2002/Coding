# Greatest of two numbers
# Find the larger of two given numbers. 
# a=10, b=20 → 20
def greatest_two(a,b):
    if(a==b):
        return("Equal",a)
    elif(a>b):
        return("1st",a)
    return("2nd",b)

a = 20
b = 10
print(greatest_two(a,b))