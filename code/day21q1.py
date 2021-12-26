file = open("../inputs/day21.txt")

pos1 = int(file.readline().strip()[-1])
pos2 = int(file.readline().strip()[-1])

print(pos1, pos2)

pos = [pos1, pos2]
score = [0, 0]

die = 1
count = 0
currPlayer = 1


def movePlayerAndAddScore(roll):
    pos[currPlayer-1] += roll
    if pos[currPlayer-1] > 10:
        pos[currPlayer-1] %= 10
        if pos[currPlayer-1] == 0:
            pos[currPlayer-1] = 10
    score[currPlayer-1] += pos[currPlayer-1]


def addDie():
    global die, count
    die += 1
    count += 1
    if die > 100:
        die = 1


def rollAndMove():
    currRoll = die
    addDie()
    currRoll += die
    addDie()
    currRoll += die
    addDie()
    movePlayerAndAddScore(currRoll)


while score[0] < 1000 and score[1] < 1000:
    rollAndMove()
    if currPlayer == 2:
        currPlayer = 1
    else:
        currPlayer = 2

print(count * min(score))
