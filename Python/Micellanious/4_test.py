def is_palindrome(n): 
    if n < 0: 
        return False 
    original = n 
    reversed_num = 0 
    while n > 0: 
        reversed_num = reversed_num * 10 + n % 10 
        n //= 10 
    return original == reversed_num 
num = int(input("Enter your number: "))
print(is_palindrome(num)) 