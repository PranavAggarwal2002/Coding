f = open("poems.txt")
content = f.read()
if("Twinkle" in content):
    print("The Word Twinfle is present")
else:
    print("Word Twinkle is not present")
f.close()