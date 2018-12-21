lettersCount = 0
wordsCount = 0
linesCount = 0
f = open('C:\\Users\\dip\\PycharmProjects\\lab1\\lab16text.txt', 'r')
while True:
    ch = f.read(1)
    if ch == '':
        break
    elif ch == '\n':
        linesCount += 1
        wordsCount += 1
    elif ch == ' ':
        wordsCount += 1
    elif ord('A') <= ord(ch) <= ord('Z') or ord('a') <= ord(ch) <= ord('z'):
        lettersCount += 1

f.close()
print('Input file contains:')
print(lettersCount, 'letters')
print(wordsCount, 'words')
print(linesCount, 'lines')
