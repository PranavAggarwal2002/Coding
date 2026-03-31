def goodDay(name, ending = "Thank You"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Ram")
goodDay("Rohan", "Thanks")

''' 
If we don't give value take default value
if we give value take ours
'''
# Good Day, Ram
# Thank You
# Good Day, Rohan
# Thanks

def greet(name = "Stranger"):
    print(f"Hello {name}")
greet()
greet("Ram")
