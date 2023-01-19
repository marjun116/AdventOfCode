file = open("../inputs/day10.txt", "r")
x = file.read()
data = [line.strip() for line in x.splitlines()]

line = []

countp = 0
countb = 0
countg = 0
countc = 0

for i in range(len(data)):
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
                countp += 1
                break
        if char == "]":
            if (line[-1] == "["):
                line.pop()
            else:
                countb += 1
                break
        if char == "}":
            if (line[-1] == "{"):
                line.pop()
            else:
                countc += 1
                break
        if char == ">":
            if (line[-1] == "<"):
                line.pop()
            else:
                countg += 1
                break

print(countp*3)
print(countb*57)
print(countg*25137)
print(countc*1197)
