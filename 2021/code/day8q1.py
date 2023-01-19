file = open("../inputs/day8.txt", "r")

before = []
after = []

for line in file:
    parts = line.split(" | ")
    before_curr = parts[0].split(" ")
    after_curr = parts[1].split(" ")
    after_curr[len(after_curr) - 1] = after_curr[len(after_curr) - 1].strip()
    before.append(before_curr)
    after.append(after_curr)

print(after)

unique=0
for i in range(len(after)):
    for j in range(len(after[i])):
        if len(after[i][j]) == 2 or len(after[i][j]) == 4 or len(after[i][j]) == 3 or len(after[i][j]) == 7:
            print(after[i][j])
            unique+=1

print(unique)