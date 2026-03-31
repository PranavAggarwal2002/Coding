list = ["Apple", "Orange", 5, 345.06, False, "Ram", "Shyam"]
print(list)

list.append("Banana") #append means join at end
print(list)

l1 = [1, 36, 31, 12, 5, 9, 11]
# print(l1), l1.reverse(), print(l1) , l1.sort(), print(l1), l1.reverse(), print(l1)
l1.insert(3, 333) #insert add item in between list we give index first and then item which need to be inserted
print(l1)
print(len(l1))

l1 = [1, 36, 31, 12, 5, 9, 11]
print(l1)
print(l1.pop(3))
print(l1)

l1 = [1, 36, 31, 12, 5, 9, 11]
print(l1)
value = l1.pop(3)
print(value, l1)

l1 = [1, 36, 31, 12, 5, 9, 11]
value = l1.remove(31)
print(l1, value)

l3 = l1
print(l3)