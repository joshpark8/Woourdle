from os import rmdir


with open('words.txt', 'r') as f:
    lines = f.readlines()
with open('wordsNew.txt', 'w') as f:
    for line in lines:
        line = line.strip(' ').strip('\n')
        print(line)
        if line == "\n" or len(line) != 5:
            pass
        else:
            f.write(line + '\n')