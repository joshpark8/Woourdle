import os
import random

from matplotlib import lines
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
print(word)
window = GraphWin("Wurdle", 500, 600)

guess = [char for char in input("guess ")]

for i in range(len(word)):
    xPos = 70 + (i * 90)
    yPos = 50

    rect = Rectangle(Point(110+(i*90), 90), Point(30+(i*90), 10))
    if guess[i] == word[i]:
        rect.setFill("green")
    elif guess[i] in word:
        rect.setFill("yellow")
    else:
        rect.setFill("grey")
    rect.draw(window)

    letter = Text(Point(xPos, yPos), guess[i])
    letter.setSize(82)
    letter.draw(window)

input("Press any key to exit... ")