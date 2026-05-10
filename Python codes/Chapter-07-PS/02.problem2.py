'''
Write a program to greet all the person names stored in a list 'l' and which starts
with S.
l = ["Harry","Soham"","Rahul"]
'''

l = ["Harry","Soham","Rahul","Sachin"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")