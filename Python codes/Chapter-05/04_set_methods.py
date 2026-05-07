# set cannot have duplicate values.

s = {1,5,32,5,1,2,3,4,4,4}

print(s,type(s))
s.add(100)

print(s,type(s))
s.remove(1)
print(s,type(s))
