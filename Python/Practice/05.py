def prime(n):
    if(n<=1):
        return
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return
    print(n)

a = int(input("Enter starting number(L) of range : "))
b = int(input("Enter Ending number(R) of range : "))

for i in range(a,b+1):
    prime(i)