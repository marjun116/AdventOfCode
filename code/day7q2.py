import math
file = open("../inputs/day7.txt", "r")

def getFinalPosition(positions, num):
    toReturn = 0
    for i in range(len(positions)):
        if num > positions[i]:
            if(len(positions)/2 > i):
                toReturn = math.floor(num)
            else:
                toReturn = math.ceil(num)
            break
    return toReturn

number_line = file.readline()
horizontal_positions = number_line.split(",")
horizontal_positions = [int(i) for i in horizontal_positions]
horizontal_positions.sort()

average = sum(horizontal_positions)/len(horizontal_positions)
finalPosition = getFinalPosition(horizontal_positions, average)
print(finalPosition)
fuel = 0

def getFuel(num):
    return (num*(num+1))/2


for position in horizontal_positions:
    fuel+= getFuel(abs(finalPosition-position))

print(fuel)