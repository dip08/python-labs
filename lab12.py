print('Введите числа через пробел: ')
n = input().split()
result = 0
for i in n:
    result += n[int(i):len(n)].count(i)
result = result // 2
print(result)

