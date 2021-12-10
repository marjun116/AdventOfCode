file = open("../inputs/day9.txt", "r")
x = file.read()
data = [[int(num) for num in line] for line in x.splitlines()]

totalRisk = 0
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


for i in range(len(data)):
    for j in range(len(data[i])):
        if (isLow(i, j)):
            lowPoints.append([i, j])
            toAdd = data[i][j] + 1
            totalRisk += toAdd

print(totalRisk)
print(lowPoints)
