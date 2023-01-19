file = open("../inputs/day14.txt", "r")

inputString = file.readline().strip()
template = dict()
countKeys = dict()
countLetters = dict()

for line in file:
    if " -> " in line:
        key, val = line.split(" -> ")
        val = val.strip()
        template[key] = val


def initial(inputString):
    countLetters[inputString[0]] = 1
    for i in range(len(inputString) - 1):
        key = inputString[i:i+2]
        if key in countKeys.keys():
            countKeys[key] += 1
        else:
            countKeys[key] = 1
        if inputString[i+1] in countLetters.keys():
            countLetters[key[1]] += 1
        else:
            countLetters[key[1]] = 1


def step(countKeys):
    currCountKeys = dict()
    for key in countKeys:
        if template[key] in countLetters.keys():
            countLetters[template[key]] += countKeys[key]
        else:
            countLetters[template[key]] = countKeys[key]
        key1 = key[0] + template[key]
        key2 = template[key] + key[1]
        if key1 in currCountKeys.keys():
            currCountKeys[key1] += countKeys[key]
        else:
            currCountKeys[key1] = countKeys[key]
        if key2 in currCountKeys.keys():
            currCountKeys[key2] += countKeys[key]
        else:
            currCountKeys[key2] = countKeys[key]
    return currCountKeys.copy()


initial(inputString)
for i in range(40):
    countKeys = step(countKeys)

max = max(countLetters, key=countLetters.get)
min = min(countLetters, key=countLetters.get)

print("max: ", max, countLetters[max])
print("min: ", min, countLetters[min])

print(countLetters[max] - countLetters[min])
