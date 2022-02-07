import os
import random

from graphics import *

dirname = os.path.dirname(__file__)
n = random.randint(0, 2314)

with open(f"{dirname}/words.txt") as f:
    lines = sorted(set(f.readlines()))
    for word in lines:
        i = lines.index(word)
        lines[i] = word.strip()
    word = lines.pop(n)

word = [char for char in word]
window = GraphWin("Woourdle", 500, 600)
for i in range(6):
    guess = ""
    guess = [char for char in input("guess: ")]
    while len(guess) != 5:
        guess = [char for char in input("Your guess must be 5 letters!: ")]
    green = ["","","","",""]
    yellow = []
    for k in range(len(word)):
        if guess[k] == word[k]:
            green[k] = word[k]
            # print(green)
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
            # print("GREEN " + word[j])
        elif guess[j] in word and guess[j] not in green and guess[j] not in yellow:
            rect.setFill("yellow")
            yellow.append(guess[j])
            # print("YELLOW " + word[j])
        else:
            rect.setFill("grey")
            # print("GREY " + word[j])
        rect.draw(window)
        letter.draw(window)

print(word)
input("Press any key to exit... ")