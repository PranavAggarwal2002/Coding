# Calculate the area of circle 
# Description: Given radius r, compute area of circle: πr². 
# Example: r=5 → area ≈ 78.54
def area_circle(r):
    pi = 3.14159
    return pi * r * r

r = float(input("Enter radius: "))
print(area_circle(r))