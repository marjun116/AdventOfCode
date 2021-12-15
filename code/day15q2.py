from queue import PriorityQueue

with open('../inputs/day15.txt', 'r') as f:
    matrix = [list(map(int, line)) for line in f.read().splitlines()]


def shortestPathDijkstra():
    height, width = len(matrix), len(matrix[0])
    weightQueue = PriorityQueue()
    weightQueue.put((0, (0, 0)))
    visited = {(0, 0), }
    while weightQueue:
        curr_risk, (i, j) = weightQueue.get()
        # Once we reach the end of the matrix, we can stop and return the risk
        if i == height - 1 and j == width - 1:
            return curr_risk
        for nextX, nextY in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= nextX < height and 0 <= nextY < width and (nextX, nextY) not in visited:
                weight = matrix[nextX][nextY]
                weightQueue.put((curr_risk + weight, (nextX, nextY)))
                visited.add((nextX, nextY))


def createBigMatrixRow(matrix):
    toReturn = []
    for i in range(len(matrix)):
        currLine = []
        for count in range(5):
            for j in range(len(matrix[0])):
                toAppend = matrix[i][j]+count
                if toAppend > 9:
                    toAppend -= 9
                currLine.append(toAppend)
        toReturn.append(currLine)
    return toReturn


def createBigMatrixColumn(matrix):
    toReturn = []
    for count in range(5):
        for i in range(len(matrix)):
            currLine = []
            for j in range(len(matrix[0])):
                toAppend = matrix[i][j]+count
                if toAppend > 9:
                    toAppend -= 9
                currLine.append(toAppend)
            toReturn.append(currLine)
    return toReturn


matrix = createBigMatrixRow(matrix)
print(matrix[-1])
matrix = createBigMatrixColumn(matrix)


print(shortestPathDijkstra())
