crates = []
initialCrates = []
done = False

lines = open("input/5.txt", "r").readlines()

for line in lines:
    if ("1" in line.strip() and not done):
        nums = line.strip().split(" ")
        for i in range(0, int(nums[-1])):
            crates.append([])
        for i in range(0, len(initialCrates)):
            for j in range(0, len(crates)):
                if j*4 < len(initialCrates[i]):
                    if initialCrates[i][4*j] == "[":
                        crates[j].insert(0, initialCrates[i][4*j+1])
        done = True
        continue
    if not done:
        initialCrates.append(line.strip())
    else:
        curr = line.strip().split(" ")
        if len(curr) != 6:
            continue
        count = int(curr[1])
        initial = int(curr[3]) - 1
        final = int(curr[5]) - 1
        temp = []
        for i in range(0, count):
            temp.append(crates[initial].pop())
        for i in range(0, count):
            crates[final].append(temp.pop())
print(crates)
