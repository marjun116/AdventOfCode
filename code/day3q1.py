from collections import defaultdict

file = open("../inputs/day3.txt", "r")

lines = file.readlines()

lines = [line.strip() for line in lines]

counts = defaultdict(int)

for line in lines:
    for index in range(len(line)):
        counts[index] += int(line[index])

ratios = []
for index in counts.keys():
    ratios.append(counts[index] / len(lines))

print(ratios)

epsilon = 0b000110001010
lambda1 = 0b111001110101

print(epsilon * lambda1)