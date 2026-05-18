with open("Test10.txt", "w") as f:
    f.write("") # clear a file but 2 words answer is also present

open("Test10.txt", "w") # this alone will clear a file
'''
write mode automatically:
1) creates file if it does not exist
2) erases all old contents if file already exists

if we don't want 2) to happen we use append
''' 