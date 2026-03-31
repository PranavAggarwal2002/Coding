s = {1,2,3,4,5,"Pranav",22.3}
print(s,type(s))
s.add(566)
print(s)

s = {1,2,4}
d = {1,2,4}
print(s,type({1}),"Lenght of set s:",len(s))

print(s != d,"\n",s==d)

s = {1,2,3,4,5,"Pranav",22.3}
print(s)
s.remove(1)
print("After using s.remove(1)",s)

s = {1,2,3,4,5,"Pranav",22.3}
print(s)
a = s.pop()
print("After using s.pop(), remove random element from set",s,a)

s = {1,2,3,4,5,"Pranav",22.3}
print(s)
s.clear()
print("After using s.clear(), empty your set")
print(s)
