def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "Ok" # Function take a value and whichever variable ask give it to it

a = goodDay("Ram", "Thank You")
print(a)

def avg():
    a = int(input("Enter Your Number : "))
    b = int(input("Enter Your Number : "))
    c = int(input("Enter Your Number : "))

    average = (a+b+c)/3
    return average
a = avg()
print(a)