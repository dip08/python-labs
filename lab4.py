print('Введите почледовательность чисел (0 - завершение последовательности): ')
num = int(input())
prev = num
count = 0
while num != 0:
    num = int(input())
    if num > 0:
        if num > prev:
            count += 1
        prev = num
print('Количество чисел, которые больше предыдущего: ', count)
