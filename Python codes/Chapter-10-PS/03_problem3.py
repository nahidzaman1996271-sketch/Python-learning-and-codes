'''
Create a class with a class attribute a; create an object from it and set 'a'
directly using object.a = o. Does this change the class attribute?
'''
class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is set
print(Demo.a) # Prints the class attribute

# And the final answer is no it doesn't change the class attribute
