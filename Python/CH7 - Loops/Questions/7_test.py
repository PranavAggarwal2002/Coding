n = int(input("Enter how much big start pattern you need : "))
'''
For n = 3
  *
 ***
*****
'''
# 3 ways to do same problem Harry Bhai, Mine and Chatgpt
for i in range(1, n+1):
    print(" "*(n-i), end="") #python default print as print("hello", end="\n") which make next print go to new line
    print("*"*(2*i-1), end="") #since we don't need to go to new line we put a end here
    print("")

# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1))

# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*(2*i-1))