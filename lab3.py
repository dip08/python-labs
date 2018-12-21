print('Введите число A:')
a = int(input())
print('Введите число B:')
b = int(input())
for i in range(a, b):
    s = str(i)
    for j in s:
        if s.count(j) == 3:
            print(s)
            break
