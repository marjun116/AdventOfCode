sheet = dict()
folds = []


def yFold(line):
    for key in list(sheet.keys()):
        if key[1] >= line:
            newY = line - (key[1] - line) - 1
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


currFold = folds[0]
if currFold[0] == 'x':
    xFold(currFold[1])
else:
    yFold(currFold[1])

print(len(sheet))
