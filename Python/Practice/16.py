# Find Sum of AP Series 
# Sum of arithmetic progression series with first term a, common difference d, and  number of terms n.
# Formula: S = n/2 * (2a + (n-1)d) 
def AP(a,n,d):
    S = n*(2*a + (n-1)*d)/2
    return S

a,d,n = 2,3,4
print(AP(a,n,d))

