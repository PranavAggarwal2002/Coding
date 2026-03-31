# Original dictionary
d = {"name": "Pranav", "age": 20, "city": "Delhi"}

print("Original dictionary:", d)
# len()
print("len() -> returns all keys in dictionary:", len(d))

# keys()
print("keys() -> returns all keys in dictionary:", d.keys())

# values()
print("values() -> returns all values in dictionary:", d.values())

# items()
print("items() -> returns key-value pairs as tuples:", d.items())

# get()
print("get('name') -> returns value of key 'name':", d.get("name"))

# update()
d.update({"age": 21})
print("update({'age':21}) -> updates value of existing key:", d)

# adding new key using update
d.update({"country": "India"})
print("update({'country':'India'}) -> adds new key-value pair:", d)

# pop()
value = d.pop("city")
print("pop('city') -> removes key 'city' and returns its value:", value)
print("Dictionary after pop:", d)

# popitem()
item = d.popitem()
print("popitem() -> removes and returns last inserted key-value pair:", item)
print("Dictionary after popitem:", d)

# setdefault()
d.setdefault("state", "Haryana")
print("setdefault('state','Haryana') -> adds key if it does not exist:", d)

# copy()
d2 = d.copy()
print("copy() -> creates a copy of dictionary:", d2)

# clear()
d2.clear()
print("clear() -> removes all items from dictionary:", d2)

# len()
print("len(d) -> returns number of key-value pairs:", len(d))