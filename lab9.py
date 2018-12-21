def NextNum(s):
    result = ''
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result += str(count) + s[i]
        i += 1
    return result


s = '1'
print('Введите какой элемент последовательности "Посмотри-и-скажи" надо вывести:')
n = int(input())
for i in range(n - 1):
    s = NextNum(s)
print(s)
