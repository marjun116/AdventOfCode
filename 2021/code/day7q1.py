file = open("../inputs/day7.txt", "r")

number_line = file.readline()
horizontal_positions = number_line.split(",")
horizontal_positions = [int(i) for i in horizontal_positions]
horizontal_positions.sort()
median = horizontal_positions[round(len(horizontal_positions)/2)]
fuel = 0

for position in horizontal_positions:
    fuel+= abs(median-position)

print(fuel)