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
                currDirectories.append([command[2], 0])
    if command[0] == "dir":
        continue
    if command[0].isdigit():
        for dir in currDirectories:
            dir[1] = dir[1] + int(command[0])

for dir in currDirectories:
    allDirectories.append(dir)

score = 0
for dir in allDirectories:
    if dir[0] == "/":
        score = 70000000 - dir[1]

spacetofree = 30000000 - score

currmin = 70000000

for dir in allDirectories:
    if dir[1] < currmin and dir[1] >= spacetofree:
        currmin = dir[1]

print(currmin)
