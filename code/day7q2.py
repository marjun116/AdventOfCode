import math
file = open("../inputs/day7.txt", "r")

number_line = file.readline()
horizontal_positions = number_line.split(",")
horizontal_positions = [int(i) for i in horizontal_positions]
horizontal_positions.sort()
average = math.floor(sum(horizontal_positions)/len(horizontal_positions))
print(average)
fuel = 0

def getFuel(num):
    return (num*(num+1))/2


for position in horizontal_positions:
    fuel+= getFuel(abs(average-position))

print(fuel)