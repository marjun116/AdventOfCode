with open("../inputs/day11.txt", 'r') as f:
    data = dict()
    for y, line in enumerate(f):
        for x, val in enumerate(line.strip()):
            data[x, y] = int(val)


def getNeighbours(key):
    x1, y1 = key
    result = []
    xvals = [-1, 0, +1]
    yvals = [-1, 0, +1]
    for x2 in xvals:
        for y2 in yvals:
            x = x1+x2
            y = y1+y2
            if x >= 0 and y >= 0 and x < 10 and y < 10:
                result.append((x, y))
    return result


totalFlashes = 0


def flash(flashed):
    global totalFlashes
    flashing = []
    for key in data:
        if data[key] > 9 and key not in flashed:
            flashing.append(key)
            totalFlashes += 1

    if flashing:
        for key in flashing:
            neighbours = getNeighbours(key)
            for neighbour in neighbours:
                data[neighbour] += 1
        flash(flashed + flashing)


def increaseDay():
    for key in data:
        data[key] += 1
    flash([])
    for key in data:
        if data[key] > 9:
            data[key] = 0


day = 0
while day < 100:
    increaseDay()
    day += 1

print(totalFlashes)
