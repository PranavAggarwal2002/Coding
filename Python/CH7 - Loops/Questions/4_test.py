Num = int(input("Enter Your Number : "))

for i in range(2, Num):
    if(Num%i) == 0:
        print("Number is not prime")
        break

else:
    print("Number is Prime")