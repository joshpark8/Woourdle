from multiprocessing.connection import answer_challenge
import os
import random

from graphics import *

green_square = "\N{large green square}"
black_square = "\N{black large square}"
yellowsquare = "\N{large yellow square}"
print(green_square + black_square + yellowsquare)
def game(window):
    dirname = os.path.dirname(__file__)
    n = random.randint(0, 2314)

    with open(f"{dirname}/words.txt") as f:
        lines = sorted(set(f.readlines()))
        for word in lines:
            i = lines.index(word)
            lines[i] = word.strip()
        rawWord = lines.pop(n)

    word = [char for char in rawWord]
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
        correctLetters = 0
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
                correctLetters += 1
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
        if correctLetters == 5:
            print("Congratulations!")
            break
    print(f"The word was {rawWord}.")

if __name__ == "__main__":
    again = True
    
    while again:
        window = GraphWin("Woourdle", 500, 600)
        game(window)
        answer = input("Play again? Y/N ")
        again = ("y" in answer) or ("Y" in answer)
        window.close()