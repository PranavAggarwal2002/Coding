number = []
f1 = int(input("Enter 1st Number Here: "))
number.append(f1)
f2 = int(input("Enter 2nd Number Here: "))
number.append(f2)
f3 = int(input("Enter 3rd Number Here: "))
number.append(f3)
f4 = int(input("Enter 4th Number Here: "))
number.append(f4)

print(sum(number))
a = number[1] + number[2] + number[3] + number[0]
print(a)