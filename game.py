import os
import random

dirname = os.path.dirname(__file__)
n = random.randint(0, 3020)

with open(f"{dirname}/words.txt") as f:
    lines = set(f.readlines())
    lines = sorted(lines)
    word = lines.pop(n).lower()
    print(word)

