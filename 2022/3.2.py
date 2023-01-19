score = 0

lines = open("input/3.txt", "r").readlines()
for i in range(0, int(len(lines)/3)):
    first = lines[i*3].strip()
    second = lines[i*3+1].strip()
    third = lines[i*3+2].strip()

    for char in first:
        if char in second and char in third:
            if ord(char) < 97:
                score = score + ord(char) - 38
            else:
                score = score + ord(char) - 96
            break

print(score)
