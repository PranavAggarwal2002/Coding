# Original set
s = {10, 20, 30, 40}

print("Original set:", s)

# add()
s.add(50)
print("add(50) -> adds element to the set:", s)

# update()
s.update([60, 70])
print("update([60,70]) -> adds multiple elements to the set:", s)

# remove()
s.remove(20)
print("remove(20) -> removes element 20 from the set:", s)

# discard()
s.discard(100)
print("discard(100) -> removes element if present (no error if not found):", s)

# pop()
value = s.pop()
print("pop() -> removes a random element from the set:", value)
print("Set after pop:", s)

# copy()
s2 = s.copy()
print("copy() -> creates a copy of set:", s2)

# clear()
s2.clear()
print("clear() -> removes all elements from set:", s2)

# union()
a = {1, 2, 3}
b = {3, 4, 5}
print("a:", a)
print("b:", b)
print("union() -> combines elements of both sets:", a.union(b))

# intersection()
print("intersection() -> common elements in both sets:", a.intersection(b))

# difference()
print("difference() -> elements in a but not in b:", a.difference(b))

# symmetric_difference()
print("symmetric_difference() -> elements in either set but not both:", a.symmetric_difference(b))

# subset check
print("issubset() -> checks if set is subset:", {1,2}.issubset(a))

# superset check
print("issuperset() -> checks if set is superset:", a.issuperset({1,2}))

# disjoint check
print("isdisjoint() -> checks if sets have no common elements:", a.isdisjoint({7,8}))

# len()
print("len(a) -> returns number of elements in set:", len(a))