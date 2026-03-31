l = ["Pranav", "Rohan", "Divyanshu", "Pratham", "Rahul"]

name = input("Enter your name: ")
name = name.capitalize()

if(name in l):
    print("Your name is in the list")
else:
    print("Your anme is not in the list")