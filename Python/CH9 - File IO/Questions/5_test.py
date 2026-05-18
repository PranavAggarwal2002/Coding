words = ["Donkey", "Bad", "Poor"]

with open("Test5.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("Test5.txt", "w") as t:
    t.write(content)