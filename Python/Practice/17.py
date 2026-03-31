# Program to find sum of GP Series
# Sum of geometric progression series with first term a, common ratio r, and number of terms n.
# Formula: S = a*(r^n - 1)/(r-1) for r≠1; if r=1, S = a*n.
def gp(a,n,r):
    if(r==1):
        S = a*n
    else:
        S = (a*((r**n) - 1)/(r-1))
    return S
a,n,r = 2,4,3
print(gp(a,n,r))