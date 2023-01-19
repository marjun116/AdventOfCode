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
secondMaxCalories = 0
thirdMaxCalories = 0

for elfCalories in allCalories:
    if sum(elfCalories) > maxCalories:
        thirdMaxCalories = secondMaxCalories
        secondMaxCalories = maxCalories
        maxCalories = sum(elfCalories)
    elif sum(elfCalories) > secondMaxCalories:
        thirdMaxCalories = secondMaxCalories
        secondMaxCalories = sum(elfCalories)
    elif sum(elfCalories) > thirdMaxCalories:
        thirdMaxCalories = sum(elfCalories)

print(maxCalories + secondMaxCalories + thirdMaxCalories)
