def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10          # get last digit
        reverse = reverse * 10 + digit
        n = n // 10             # remove last digit

    if original == reverse:
        return True
    else:
        return False


# Taking input
num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")