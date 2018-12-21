print('Введите строку с цифрами: ')
s = input()
n = len(s) - 1
while n >= 0:
    if s[n] == '1':
        s = s[:n] + 'one' + s[n + 1:]
    if s[n] == '2':
        s = s[:n] + 'two' + s[n + 1:]
    if s[n] == '3':
        s = s[:n] + 'three' + s[n + 1:]
    if s[n] == '4':
        s = s[:n] + 'four' + s[n + 1:]
    if s[n] == '5':
        s = s[:n] + 'five' + s[n + 1:]
    if s[n] == '6':
        s = s[:n] + 'six' + s[n + 1:]
    if s[n] == '7':
        s = s[:n] + 'seven' + s[n + 1:]
    if s[n] == '8':
        s = s[:n] + 'eight' + s[n + 1:]
    if s[n] == '9':
        s = s[:n] + 'nine' + s[n + 1:]
    if s[n] == '0':
        s = s[:n] + 'zero' + s[n + 1:]
    n = n - 1
print(s)
