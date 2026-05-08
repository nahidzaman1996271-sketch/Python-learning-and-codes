# If elif else ladder

a = int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for you..")

elif(a==0):
    print("Zero is a invalid age, Retype again.")

elif(a<0):
    print("Negative age number is invalid, retype again.")

else:
    print("You are below the age of consent")    

    

print("End of the program")    