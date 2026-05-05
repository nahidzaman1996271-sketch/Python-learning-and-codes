# Write a program to accept mark of 6 students and display them in a sorted manner.

# Write a program to store seven marks in a list entered by the marks here
marks = []

f1 = int(input("Enter the marks here 1: "))
marks.append(f1)
f2 = int(input("Enter the marks here 2: "))
marks.append(f2)
f3 = int(input("Enter the marks here 3: "))
marks.append(f3)
f4 = int(input("Enter the marks here 4: "))
marks.append(f4)
f5 = int(input("Enter the marks here 5: "))
marks.append(f5)
f6 = int(input("Enter the marks here 6: "))
marks.append(f6)
marks.sort()
print("The list of marks is:", marks)