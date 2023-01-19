data = open("../inputs/day17.txt").read().strip()
x, y = data.split(": ")[1].split(", ")
x = x.split("=")[1].split("..")
y = y.split("=")[1].split("..")
x_low, x_high = int(x[0]), int(x[1])
y_low, y_high = int(y[0]), int(y[1])


def doSteps(x_velo, y_velo, area):
    step = 0
    x, y = (0, 0)
    max_y = 0
    while True:
        if step > 0:
            if x_velo > 0:
                x_velo -= 1
            elif x_velo < 0:
                x_velo += 1
            else:
                x_velo = 0
            y_velo -= 1
        x += x_velo
        y += y_velo
        max_y = y if y > max_y else max_y

        if x < -area or x > x_high:
            break
        if y < y_low or y > area:
            break
        if x_low <= x <= x_high and y_low <= y <= y_high:
            return max_y

        step += 1


minX = 0
pos = 0
while pos < x_low:
    minX += 1
    pos += minX

velocities = dict()
for x_velocity in range(minX, x_high + 1):
    for y_velocity in range(0, 75000):
        hit = doSteps(x_velocity, y_velocity, 75000)
        if hit != None:
            velocities[(x_velocity, y_velocity)] = hit

maxVel = max(velocities, key=velocities.get)
print(velocities[maxVel], maxVel)
