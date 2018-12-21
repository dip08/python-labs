f = open('C:\\Users\\dip\\PycharmProjects\\lab1\\lab18text.txt', 'r')
n = int(f.readline())

d = {}

for line in f.readlines():
    data = line.split(' ')
    data[1] = data[1].strip("\n")
    if data[1] not in d.keys():
        d[data[1]] = 0
    if data[0] not in d.keys():
        d[data[0]] = d[data[1]] + 1
f.close()

for i in sorted(d.items()):
    print(i[0], i[1], sep=' ')
