lines = open("input/8.txt", "r").readlines()
trees = []

for line in lines:
    trees.append(line.strip())

width, height = len(trees[8]), len(trees)

score = 0

for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            continue
        topScore = i
        for smalli in range(i):
            if trees[smalli][j] >= trees[i][j]:
                topScore = i - smalli
        bottomScore = height - i - 1
        for largei in range(i+1, height):
            if trees[largei][j] >= trees[i][j]:
                bottomScore = largei - i
                break

        leftScore = j
        for smallj in range(j):
            if trees[i][smallj] >= trees[i][j]:
                leftScore = j - smallj
        rightScore = width - j - 1
        for largej in range(j+1, width):
            if trees[i][largej] >= trees[i][j]:
                rightScore = largej - j
                break
        if leftScore * rightScore * topScore * bottomScore > score:
            score = leftScore * rightScore * topScore * bottomScore

print(score)
