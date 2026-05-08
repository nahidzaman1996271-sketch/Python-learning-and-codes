a = int(input("Enter your age: "))

# If statement no:1
if(a%2==0):
    print("a is even")

# End of end statement no:2

# If statement no: 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you..")

elif(a<0):
    print("Negative age number is invalid, retype again.")

else:
    print("You are below the age of consent")    

# End of if statement number 2    

print("End of the program")    