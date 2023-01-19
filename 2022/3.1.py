score = 0

lines = open("input/3.txt", "r").readlines()
for line in lines:
    first, second = line.strip()[:len(
        line.strip())//2], line.strip()[len(line.strip())//2:]
    for char in first:
        if char in second:
            if ord(char) < 97:
                score = score + ord(char) - 38
            else:
                score = score + ord(char) - 96
            break

print(score)
