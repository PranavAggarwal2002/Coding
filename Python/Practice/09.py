

def palindrome(n):
    if(n<0):
        return
    original = n
    reverse_original = 0
    while(n>0):
        a = n%10
        reverse_original = (reverse_original*10) + a
        n = n//10
    if(original==reverse_original):
        print(original)

a = int(input("Enter First Number(L) of The Range : "))
b = int(input("Enter Last Number(R) of The Range : "))

for i in range(a, b+1):
    palindrome(i)