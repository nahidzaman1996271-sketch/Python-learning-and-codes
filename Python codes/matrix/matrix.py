import os
import random
import time

cols = 40
drops = [0] * cols
chars = list("python def class import return while for if in and else 01{}[]()")

def draw():
    os.system('cls')
    screen = [[' '] * cols for _ in range(20)]
    
    for i in range(cols):
        row = drops[i] % 20
        screen[row][i] = random.choice(chars)
    
    for row in screen:
        print('\033[92m' + ''.join(row) + '\033[0m')
    
    for i in range(cols):
        if drops[i] % 20 == 19 and random.random() > 0.7:
            drops[i] = 0
        drops[i] += 1

while True:
    draw()
    time.sleep(0.1)