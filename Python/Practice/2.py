def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")