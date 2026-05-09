# Write a program to find out whether the given post is talking about "Harry" or not?

post = input("Enter the name: ")

if("Harry".lower() in post.lower()):
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")   