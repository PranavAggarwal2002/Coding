# Original tuple
t = (10, 20, 30, 20, 40, 50)

print("Original tuple:", t)

# count()
print("count(20) -> counts how many times 20 appears in tuple:", t.count(20))

# index()
print("index(30) -> returns index of first occurrence of 30:", t.index(30))

# len()
print("len(t) -> returns number of elements in tuple:", len(t))

# max()
print("max(t) -> returns largest element in tuple:", max(t))

# min()
print("min(t) -> returns smallest element in tuple:", min(t))

# sum()
print("sum(t) -> returns sum of all elements:", sum(t))

# tuple concatenation
t2 = (60, 70)
print("t + t2 -> joins two tuples:", t + t2)

# tuple repetition
print("t * 2 -> repeats tuple two times:", t * 2)

# membership test
print("30 in t -> checks if element exists in tuple:", 30 in t)

# slicing
print("t[1:4] -> returns a slice of the tuple:", t[1:4])