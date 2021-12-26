import re
import math


def split(data):
    matchObject = re.search("\d\d", data)
    if matchObject:
        left = data[: matchObject.start()]
        right = data[matchObject.end():]
        left_digit = int(math.floor(int(matchObject.group()) / 2))
        right_digit = int(math.ceil(int(matchObject.group()) / 2))
        data = f"{left}[{left_digit},{right_digit}]{right}"
    return data


def explode(data):
    return data


def doMath(data):
    explodedData = explode(data)
    if explodedData != data:
        return doMath(explodedData)
    else:
        splitData = split(data)
        if splitData != data:
            return doMath(splitData)
        else:
            return splitData


snailMath = False

for line in open("../inputs/day18.txt").readlines():
    if not snailMath:
        snailMath = line.strip()
    else:
        data = "[" + snailMath + "," + line.strip() + "]"
        snailMath = doMath(data)

print(split("[[11,7],7]"))
