def is_palindrome(n): 
    if n < 0: 
        return False 
    original = n 
    reversed_num = 0 
    while n > 0: 
        reversed_num = reversed_num * 10 + n % 10 
        n //= 10 
    return original == reversed_num 
 
num = 121 
print(is_palindrome(num))

def is_palindrome(n):
    if n < 0:
        return False

    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return original == reverse