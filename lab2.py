print('Введите количество чисел, которые надо вывести: ')
n = int(input())
counter = 1
count = 0
for i in range(n):
    if counter == count:
        counter = counter + 1
        count = 0
    count = count + 1
    print(counter)
