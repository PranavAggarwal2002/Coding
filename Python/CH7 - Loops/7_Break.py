for i in range(100):
    if(i==34):
        break #Exit the loop right now
    print(i)

for i in range(100):
    print(i)
    if(i==34):
        break #Exit the loop right now

# While both may look the same their output is a bit different
# As above loop will only print from 1 to 33 
# While below loop will print form 1 to 34