allRounds = []

scoreMap = {"X": 1, "Y": 2, "Z": 3, ("A", "X"): 3, ("A", "Y"): 6, ("A", "Z"): 0, (
    "B", "X"): 0, ("B", "Y"): 3, ("B", "Z"): 6, ("C", "X"): 6, ("C", "Y"): 0, ("C", "Z"): 3}

lines = open("input/2.txt", "r").readlines()
for line in lines:
    allRounds.append((line.strip()[0], line.strip()[2]))

score = 0
for round in allRounds:
    score = score + scoreMap.get(round) + scoreMap.get(round[1])

print(score)
