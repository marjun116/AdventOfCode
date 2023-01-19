currDirectories = []
allDirectories = []

lines = open("input/7.txt", "r").readlines()

for line in lines:
    command = line.strip().split(" ")
    if command[0] == "$":
        if command[1] == "ls":
            continue
        if command[1] == "cd":
            if command[2] == "..":
                allDirectories.append(currDirectories.pop())
            else:
                currDirectories.append([[command[2]], 0])
    if command[0] == "dir":
        continue
    if command[0].isdigit():
        for dir in currDirectories:
            dir[1] = dir[1] + int(command[0])

for dirs in currDirectories:
    allDirectories.append(dirs)

score = 0
for dir in allDirectories:
    if dir[1] <= 100000:
        score = score + dir[1]

print(score)
