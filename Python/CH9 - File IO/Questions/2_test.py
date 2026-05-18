import random
def game():
    print("Your are playing the game")
    score = random.randint(0, 1000)
    print(f"Your Score : {score}")
    
    with open("Hi-Score.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore= int(hiscore)
        else:
            hiscore = 0

    if(score>hiscore):
        with open("Hi-Score.txt", "w") as t:
            t.write(str(score))

game()