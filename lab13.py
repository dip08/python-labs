print('Введите список через пробел: ')
n = input().split()
maxNow = 0
maximum = 0
most = n[0]
for i in n:
    maxNow = n.count(i)
    if maxNow > maximum:
        maximum = maxNow
        most = i
print(most)
