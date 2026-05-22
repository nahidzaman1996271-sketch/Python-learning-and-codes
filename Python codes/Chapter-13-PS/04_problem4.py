def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,52,789,25,36,145,8,7,1212]

f = list(filter(divisible5, a))
print(f)