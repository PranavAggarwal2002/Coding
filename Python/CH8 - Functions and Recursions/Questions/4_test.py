def sum(n):
    if(n==1):
        return 1
    s = n + sum(n-1)
    return s
n = int(input("Enter the number : "))
print(f"Sum is {sum(n)}")

#Harry Bhai
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4))