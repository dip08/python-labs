def CaesarCipherChar(c, k):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + k) % 26 + ord('A'))
    else:
        return c


def CaesarCipher(s, k):
    result = ''
    for ch in s:
        result += CaesarCipherChar(ch, k)
    return result


print('Введите строку: ')
text = input()
print('Введите смещение: ')
n = int(input())
print(CaesarCipher(text, n))


