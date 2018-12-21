def Fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)


print('Введите n-ое число Фибоначчи')
num = int(input())
print(Fib(num))
