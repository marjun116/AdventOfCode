file = open("inputs/day6.txt", "r")

number_line = file.readline()
lanternfishes = number_line.split(",")
lanternfishes = [int(i) for i in lanternfishes]

fish_map = {}

for fish in lanternfishes:
    if fish in fish_map:
        fish_map[fish] = fish_map[fish] + 1
    else:
        fish_map[fish] = 1


for i in range(80):
    new_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fishAge, numFish in fish_map.items():
        if fishAge == 0:
            new_fish[6] = numFish
            new_fish[8] = numFish
        else:
            new_fish[fishAge - 1] += numFish
    fish_map = new_fish

print(sum(fish_map.values()))

