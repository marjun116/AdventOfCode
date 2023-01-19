file = open("../inputs/day9.txt", "r")
x = file.read()
data = [[int(num) for num in line] for line in x.splitlines()]

lowPoints = []


def isLow(i, j):
    if i != 0:
        if data[i-1][j] <= data[i][j]:
            return False
    if i != len(data) - 1:
        if data[i+1][j] <= data[i][j]:
            return False
    if j != 0:
        if data[i][j-1] <= data[i][j]:
            return False
    if j != len(data[i]) - 1:
        if data[i][j+1] <= data[i][j]:
            return False
    return True


def getAdj(location):
    toReturn = []
    i, j = location
    if i != 0:
        toReturn.append((i-1, j))
    if i != len(data) - 1:
        toReturn.append((i+1, j))
    if j != 0:
        toReturn.append((i, j - 1))
    if j != len(data) - 1:
        toReturn.append((i, j+1))
    return toReturn


visited = []


def getBasinSize(location):
    currBasin = 1
    adj = getAdj(location)

    for loc in adj:
        if loc not in visited:
            visited.append(loc)
            if data[loc[0]][loc[1]] != 9:
                currBasin += getBasinSize(loc)
    return currBasin


for i in range(len(data)):
    for j in range(len(data[i])):
        if (isLow(i, j)):
            lowPoints.append((i, j))

basinSizes = []

for location in lowPoints:
    visited.append(location)
    basinSizes.append(getBasinSize(location))

basinSizes.sort(reverse=True)
print(basinSizes)
print(basinSizes[0]*basinSizes[1]*basinSizes[2])
