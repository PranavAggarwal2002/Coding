#  Determine if a given integer is even or odd
def even(n):
    if(n<0):
        print("Invalid Input")
        return
    if(n%2==0):
        print("even")
    else:
        print("odd")

n = int(input("Enter The Number : "))
even(n)
