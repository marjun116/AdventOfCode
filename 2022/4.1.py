allSections = []
count = 0

lines = open("input/4.txt", "r").readlines()

for line in lines:
    first, second = line.strip().split(",")
    firstStart, firstEnd = first.split("-")
    secondStart, secondEnd = second.split("-")
    allSections.append(((int(firstStart), int(firstEnd)),
                       (int(secondStart), int(secondEnd))))

for sections in allSections:

    if sections[0][0] <= sections[1][0] and sections[0][1] >= sections[1][1]:
        count = count + 1
        continue
    if sections[1][0] <= sections[0][0] and sections[1][1] >= sections[0][1]:
        count = count + 1
print(count)
