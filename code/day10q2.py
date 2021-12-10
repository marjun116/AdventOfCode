import math
file = open("../inputs/day10.txt", "r")
x = file.read()
data = [line.strip() for line in x.splitlines()]

line = []
scores = []


def getScore(char):
    if char == "(":
        return 1
    if char == "[":
        return 2
    if char == "{":
        return 3
    if char == "<":
        return 4


for i in range(len(data)):
    incomplete = True
    line = []
    for char in data[i]:
        if char == "(":
            line.append("(")
        if char == "[":
            line.append("[")
        if char == "<":
            line.append("<")
        if char == "{":
            line.append("{")
        if char == ")":
            if (line[-1] == "("):
                line.pop()
            else:
                incomplete = False
                break
        if char == "]":
            if (line[-1] == "["):
                line.pop()
            else:
                incomplete = False
                break
        if char == "}":
            if (line[-1] == "{"):
                line.pop()
            else:
                incomplete = False
                break
        if char == ">":
            if (line[-1] == "<"):
                line.pop()
            else:
                incomplete = False
                break
    if incomplete:
        score = 0
        for char in reversed(line):
            score = score * 5
            score += getScore(char)
        scores.append(score)

scores.sort()
print(scores[math.floor(len(scores)/2)])
