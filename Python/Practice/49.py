# Permutations in which N people can occupy R seats in a classroom
# Calculate the number of ways to arrange N people in R seats (order matters, R ≤ N).
# Formula: P(N, R) = N! / (N-R)! 
# N=5, R=3 → 5*4*3 = 60 
def factorial(a):
    fac = 1
    for i in range(1,a+1):
        fac *= i
    return fac

def permutation(n,r):
    if r > n:
        return "Invalid input"
    per = ((factorial(n)/(factorial(n-r))))
    return per

n = int(input("Enter Number of people : "))
r = int(input("Enter Number of seats : "))
print(permutation(n,r))