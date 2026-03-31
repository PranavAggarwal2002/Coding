# Original list
l = [10, 20, 30, 40]
print("Original list:", l)

# append()
l.append(50)
print("append(50) -> adds element at the end of the list:", l)

# insert()
l.insert(2, 25)
print("insert(2,25) -> inserts 25 at index 2:", l)

# extend()
l.extend([60, 70])
print("extend([60,70]) -> adds multiple elements at the end:", l)

# remove()
l.remove(30)
print("remove(30) -> removes the first occurrence of 30:", l)

# pop()
value = l.pop()
print("pop() -> removes last element and returns it:", value, "Updated list:", l)

# pop(index)
value = l.pop(1)
print("pop(1) -> removes element at index 1:", value, "Updated list:", l)

# index()
print("index(25) -> returns index of element 25:", l.index(25))

# count()
print("count(20) -> counts how many times 20 appears:", l.count(20))

# sort()
l2 = [5, 1, 8, 3]
print("Another list:", l2)
l2.sort()
print("sort() -> sorts the list in ascending order:", l2)

# reverse()
l2.reverse()
print("reverse() -> reverses the list order:", l2)

# copy()
l3 = l2.copy()
print("copy() -> creates a copy of list:", l3)

# clear()
l3.clear()
print("clear() -> removes all elements from list:", l3)

# len()
print("len(l) -> returns number of elements in list:", len(l))