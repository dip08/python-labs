def Palindrom(s):
    # делим нацело
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True


print('Введите строку: ')
s = input()
result = 0
if Palindrom(s):
    print(0)
else:
    for i in range(len(s)):
        sSub = s
        for j in reversed(range(i)):
            sSub += sSub[j]
        if Palindrom(sSub):
            result = i
            break
print('До полинома надо добавить:', result, 'симв.')
