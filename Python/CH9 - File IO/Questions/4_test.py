word = "Donkey"

with open("Test4.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("Test4.txt", "w") as t:
    t.write(contentNew)