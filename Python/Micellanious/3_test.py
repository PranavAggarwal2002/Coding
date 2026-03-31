f = input("Enter Your Choice Stone or Paper or Sciccor : ")

n = "Stone" or "Paper" or "Sciccor"

if(n==f):
    print("Draw")
elif(f=="Stone" and n=="Sciccor" or f=="Paper" and n=="Stone" or f=="Scissor" and n=="Paper"):
    print("You Win")
else:
    print("You Lose")