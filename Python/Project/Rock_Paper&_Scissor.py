import random
'''
r for rock
p for paper
s for scissor
'''
computer = random.choice(["r","p","s"])
you = input("Enter your choice [r for rock, p for paper and s for sciccor] : ")

print(f"You choose {you} amd computer choose {computer}")

if(computer==you):
    print("Draw")

elif(computer== "r" and you == "s"):
    print("Computer won")

elif(computer== "r" and you == "p"):
    print("You won")

elif(computer== "p" and you == "r"):
    print("Computer won")

elif(computer== "p" and you == "s"):
    print("You won")

elif(computer== "s" and you == "p"):
    print("Computer won")

elif(computer== "s" and you == "r"):
    print("You won")

else:
    print("Something Went Wrong")