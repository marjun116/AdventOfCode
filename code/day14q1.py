import collections

file = open("../inputs/day14.txt", "r")

inputString = file.readline().strip()
template = dict()

for line in file:
    if " -> " in line:
        key, val = line.split(" -> ")
        val = val.strip()
        template[key] = val


def step(inputString):
    currString = inputString[0]
    for i in range(len(inputString) - 1):
        key = inputString[i:i+2]
        currString += template[key]
        currString += key[1]
    return currString


for i in range(10):
    inputString = step(inputString)

print(collections.Counter(inputString).most_common()[0])
print(collections.Counter(inputString).most_common()[-1])
