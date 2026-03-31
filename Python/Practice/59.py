# Program to find roots of a Quadratic Equation 
# Description: Solve ax² + bx + c = 0. Compute discriminant D = b² - 4ac. 
# • If D > 0: two distinct real roots. 
# • If D = 0: one real root (double root). 
# • If D < 0: complex roots. 
# Example: a=1, b=-3, c=2 → roots: 2.0, 1.0 
def quadratic(a, b, c):
    D = b*b - 4*a*c   # discriminant

    if D > 0:
        root1 = (-b + (D**0.5)) / (2*a)
        root2 = (-b - (D**0.5)) / (2*a)
        print("Two real roots:", root1, root2)

    elif D == 0:
        root = -b / (2*a)
        print("One real root:", root)

    else:
        real = -b / (2*a)
        imag = ((-D)**0.5) / (2*a)
        print("Complex roots:", real, "+", imag, "i and", real, "-", imag, "i")


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

quadratic(a, b, c)