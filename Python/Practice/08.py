def armstrong(n):
    b = n
    power = len(str(n))
    if(n<0):
        return
    ln = 0
    while(n>0):
        a = n%10
        ln = ln + (a**power)
        n = n//10
    if(b==ln):
        print(b)

n = int(input("Enter Your Number : "))
armstrong(n)
