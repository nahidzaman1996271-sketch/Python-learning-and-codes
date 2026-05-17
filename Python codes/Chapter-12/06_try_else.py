a = int(input("Enter a numebr: "))
b = int(input("Enter second numebr: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")