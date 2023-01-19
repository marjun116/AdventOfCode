allRounds = []

scoreMap = {("A", "X"): 3, ("A", "Y"): 4, ("A", "Z"): 8, ("B", "X"): 1,
            ("B", "Y"): 5, ("B", "Z"): 9, ("C", "X"): 2, ("C", "Y"): 6, ("C", "Z"): 7}

lines = open("input/2.txt", "r").readlines()
for line in lines:
    allRounds.append((line.strip()[0], line.strip()[2]))

score = 0
for round in allRounds:
    score = score + scoreMap.get(round)

print(score)
