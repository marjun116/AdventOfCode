lines = open("input/6.txt", "r").readlines()

buffer = lines[0].strip()

curr = [buffer[0], buffer[1], buffer[2], buffer[3], buffer[4], buffer[5],
        buffer[6], buffer[7], buffer[8], buffer[9], buffer[10], buffer[11], buffer[12]]

for i in range(3, len(buffer)):
    curr.append(buffer[i])
    if len(set(curr)) == len(curr):
        print(i+1)
        break
    else:
        curr.pop(0)
