'''
***
* *    for n = 3
*** 
'''



n = int(input("Enter how many line of star pattern you need : "))
for i in range(1,n+1):
    if i%2 != 0:
        print("***")
    else:
        print("* *")