name = "Harry"
nameshort = name[-4:-1] # start form index 0 all thw ay till 3 (excluding 3)
print(nameshort)
print(name[-4: -1])
print(name[1: 4]) 
# both above and below will ave same answer as we can convert negative slicing to positive by changing number to positve and by changing their positions
print(name[:4]) # is smae as print(name[0:4])
print(name[1:]) # is smae as print(name[1:5])
print(name[1:5])