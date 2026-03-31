def automorphic(n):
    if str(n*n).endswith(str(n)):
        print("True")
    else:
        print("False")

n = int(input("Enter the Number : "))
automorphic(n)