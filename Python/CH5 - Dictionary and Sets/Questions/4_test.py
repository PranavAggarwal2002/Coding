s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s)) #len of s
print(s)
# in this case len came as two as even though their type are different 
# their numeric is same