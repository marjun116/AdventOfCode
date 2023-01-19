allCalories = []

currentElfCalories = []

lines = open("input/1.txt", "r").readlines()
for line in lines:
    if not line.strip():
        allCalories.append(currentElfCalories.copy())
        currentElfCalories = []
    else:
        currentElfCalories.append(int(line.strip()))

maxCalories = 0

for elfCalories in allCalories:
    if sum(elfCalories) > maxCalories:
        maxCalories = sum(elfCalories)

print(maxCalories)
