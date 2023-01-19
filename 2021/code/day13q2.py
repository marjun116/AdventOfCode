sheet = dict()
folds = []


def yFold(line):
    for key in list(sheet.keys()):
        if key[1] >= line:
            newY = line - (key[1] - line)
            newKey = (key[0], newY)
            sheet[newKey] = 1
            del sheet[key]


def xFold(line):
    for key in list(sheet.keys()):
        if key[0] >= line:
            newX = line - (key[0] - line)
            newKey = (newX, key[1])
            sheet[newKey] = 1
            del sheet[key]


with open("../inputs/day13.txt", 'r') as f:

    for y, line in enumerate(f):
        if ',' in line:
            x, y = line.strip().split(',')
            x = int(x)
            y = int(y)
            sheet[x, y] = 1
        elif 'fold' in line:
            fold = line.split(' ')
            axis, loc = fold[-1].split('=')
            loc = int(loc.strip())
            folds.append((axis, loc))


for fold in folds:
    if fold[0] == 'x':
        xFold(fold[1])
    else:
        yFold(fold[1])

print(len(sheet))
maxx = -1
maxy = -1
for key in sheet.keys():
    if key[0] > maxx:
        maxx = key[0]
    if key[1] > maxy:
        maxy = key[1]
fin = [[0]*(maxx + 1) for _ in range(maxy+1)]

count = 0
for key in sheet.keys():
    print(key)
    fin[key[1]][key[0]] = 1
    for lin in fin:
        print(lin)
    print()
