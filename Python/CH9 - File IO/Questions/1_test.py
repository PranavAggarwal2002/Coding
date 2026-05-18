with open("poems.txt") as f:
    content = f.read()
    if("Twinkle" in content):
        print("The Word Twinkle is present")
    else:
        print("Word Twinkle is not present")