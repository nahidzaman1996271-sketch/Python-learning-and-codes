import random

'''
1  → Snake
-1 → Water
0  → Gun
'''

youDict     = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (s=Snake, w=Water, g=Gun): ")
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw!")
elif (computer - you) == -1 or (computer - you) == 2:
    print("You lose!")
else:
    print("You win!")