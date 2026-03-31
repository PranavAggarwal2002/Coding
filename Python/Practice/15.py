# Sum of first N natural numbers 
# Compute the sum 1 + 2 + ... + N
def sum(n):
    sum = 0
    if(n<=0):
        return
    else:
        for i in range(1,n+1):
            sum += i
        print(sum)

n = int(input("Enter The Natural Number : "))
sum(n)