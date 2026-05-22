'''
Write a program to find the maximum of the numbers in a list using the reduce function.
'''

from functools import reduce
a = [1,52,789,25,36,145,8,7,1212]

def greater(a, b):
    if(a > b):
        return a
    return b

print(reduce(greater, a))