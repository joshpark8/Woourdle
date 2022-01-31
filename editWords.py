from os import rmdir


with open('words.txt', 'r') as f:
    lines = sorted(set(f.readlines()))
with open('words.txt', 'w') as f:
    for word in lines:
        word = word.lower()
        if len(word) == 6:
            f.write(word)