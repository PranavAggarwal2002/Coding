def prime(n):
    if(n<=0):
        print("Invalid Input")
    else:
        for i in range(2,n):
            if(n%i==0):
                print("Number is not prime")
                break
            else:
                print("Number is prime")
                break
n = int(input("Enter The number : "))
prime(n)