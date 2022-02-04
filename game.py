import os
import random

from graphics import *

dirname = os.path.dirname(__file__)
n = random.randint(0, 2612)

with open(f"{dirname}/words.txt") as f:
    lines = sorted(set(f.readlines()))
    for word in lines:
        i = lines.index(word)
        lines[i] = word.strip()
    word = lines.pop(n)

word = [char for char in word]
window = GraphWin("Wurdle", 500, 600)

for i in range(6):
    guess = [char for char in input("guess: ")]
    
    for j in range(len(word)):
        xPos = 70 + (j * 90)
        yPos = 70 + (i * 90)
        rectA = Point(110+(j*90), ((i+1)*90)-60)
        rectB = Point(30+(j*90), ((i+1)*90)+20)
        rect = Rectangle(rectA, rectB)
        letter = Text(Point(xPos, yPos), guess[j])
        letter.setSize(72)
        
        if guess[j] == word[j]:
            rect.setFill("green")
        elif guess[j] in word:
            rect.setFill("yellow")
        else:
            rect.setFill("grey")
        rect.draw(window)
        letter.draw(window)

print(word)
input("Press any key to exit... ")