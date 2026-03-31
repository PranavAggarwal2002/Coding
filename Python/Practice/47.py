# Sum of numbers in the given range 
# Compute the sum of all integers between L and R inclusive. 
# L=5, R=10 → 5+6+7+8+9+10=45 
def sum(L,R):
    sum = 0
    for i in range(L,R+1):
        sum += i
    return sum
l = int(input("Enter L : "))
r = int(input("Enter R : "))
print(sum(l,r))