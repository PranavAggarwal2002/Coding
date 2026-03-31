d = {} #empty dictionary
marks = {
    "Pranav": 100,
    "Pratham":75,
    "Rahul": 34
}
print(marks, type(marks))
print(marks["Pranav"]) #Will tell marks corresponding to Pranav

# print(marks[0]) will give error over here as it doesn't have index
# Dictioanry makes look up easy in large data
# We can also use approach marks = [["Pranav",100],["Pratham",75]]
# From above you can see, we can make list of list in pyhton so why no?
# Computationally expensive as complex logic and Pranav & 100 will not be linked to Pranav directly

marks = {
    "Pranav": 100,
    "Pratham": 75,
    "Rahul": 34,
    0: "Totum",
    "Pratham": 85
}

print(marks)