f = open('C:\\Users\\dip\\PycharmProjects\\lab1\\lab17text.txt', 'r')
n = int(f.readline())
mas = [0] * (n - 1)
for line in f.readlines():
    data = line.split(' ')
    st1 = int(data[2])
    st2 = int(data[3])
    for i in range(st1, st2):
        mas[i - 1] += 1
f.close()
max = 0
for i in mas:
    if max < i:
        max = i

for counter, value in enumerate(mas):
    if value == max:
        print(counter + 1, counter + 2, sep='-')
