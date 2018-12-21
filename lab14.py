board = [0] * 8
for i in range(8):
    board[i] = [0] * 8
for i in range(8):
    for j in range(8):
        board[i][j] = '-'

print('Введите назавание фигуры(пешка – *, конь – К, слон – S, ладья – L, ферзь – F):')
figure = input()
print('Введите назавние позиции(например e4)')
place = input()

j = ord(place[0]) - ord('a')
i = int(place[1]) - 1
board[i][j] = figure

if figure == '*':
    if i < 8:
        board[i + 1][j] = '+'
        if i == 1:
            board[i + 2][j] = '+'
elif figure == 'K':
    if i - 2 >= 0:
        if j - 1 >= 0:
            board[i - 2][j - 1] = '+'
        if j + 1 < 8:
            board[i - 2][j + 1] = '+'
    if i - 1 >= 0:
        if j - 2 >= 0:
            board[i - 1][j - 2] = '+'
        if j + 2 < 8:
            board[i - 1][j + 2] = '+'
    if i + 2 < 8:
        if j - 1 >= 0:
            board[i + 2][j - 1] = '+'
        if j + 1 < 8:
            board[i + 2][j + 1] = '+'
    if i + 1 < 8:
        if j - 2 >= 0:
            board[i + 1][j - 2] = '+'
        if j + 2 < 8:
            board[i + 1][j + 2] = '+'
elif figure == 'S':
    for q in range(8):
        if q != j:
            if 0 <= i - j + q < 8:
                board[i - j + q][q] = '+'
            if 0 <= i + j - q < 8:
                board[i + j - q][q] = '+'
elif figure == 'L':
    for q in range(8):
        if q != i:
            board[q][j] = '+'
        if q != j:
            board[i][q] = '+'
elif figure == 'F':
    for q in range(8):
        if q != i:
            board[q][j] = '+'
        if q != j:
            board[i][q] = '+'
            if 0 <= i - j + q < 8:
                board[i - j + q][q] = '+'
            if 0 <= i + j - q < 8:
                board[i + j - q][q] = '+'
for i in range(8):
    for j in range(8):
        print(board[7 - i][j], end='')
    print()
