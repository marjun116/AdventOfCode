lines = open("input/8.txt", "r").readlines()
trees = []

for line in lines:
    trees.append(line.strip())

width, height = len(trees[8]), len(trees)

hidden = [[0]*width for _ in range(height)]

for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            hidden[i][j] = 1
            continue
        ishidden = False
        for smalli in range(i):
            if trees[smalli][j] >= trees[i][j]:
                ishidden = True
                break
        if not ishidden:
            hidden[i][j] = 1
            continue
        ishidden = False
        for largei in range(i+1, height):
            if trees[largei][j] >= trees[i][j]:
                ishidden = True
                break
        if not ishidden:
            hidden[i][j] = 1
            continue

        ishidden = False
        for smallj in range(j):
            if trees[i][smallj] >= trees[i][j]:
                ishidden = True
                break
        if not ishidden:
            hidden[i][j] = 1
            continue
        ishidden = False
        for largej in range(j+1, width):
            if trees[i][largej] >= trees[i][j]:
                ishidden = True
                break
        if not ishidden:
            hidden[i][j] = 1
            continue

total = 0
for i in range(height):
    for j in range(width):
        if hidden[i][j] == 1:
            total = total + 1
print(total)
