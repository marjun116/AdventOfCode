file = open("../inputs/day8.txt", "r")

before = []
after = []

def find1(signal):
    for i in range(len(signal)):
        if len(signal[i]) == 2:
            return signal[i]

def find7(signal):
    for i in range(len(signal)):
        if len(signal[i]) == 3:
            return signal[i]

def find8(signal):
    for i in range(len(signal)):
        if len(signal[i]) == 7:
            return signal[i]

def find4(signal):
    for i in range(len(signal)):
        if len(signal[i]) == 4:
            return signal[i]


def finda(signal):
    one=find1(signal)
    seven=find7(signal)
    for letter in seven:
        if letter not in one:
            curr_map['a'] = letter
            return

def finddAndg(signal):
    fiveDigits=[]
    for i in signal:
        if len(i) == 5:
            fiveDigits.append(i)
    newFiveDigits = [x.replace(curr_map['a'],'') for x in fiveDigits]
    common = ''.join(set(newFiveDigits[0]).intersection(newFiveDigits[1]).intersection(newFiveDigits[2]))
    four = find4(signal)
    if common[0] not in four:
        curr_map['g'] = common[0]
        curr_map['d'] = common[1]
    else:
        curr_map['g'] = common[1]
        curr_map['d'] = common[0]

def findb(signal):
    four = find4(signal)
    four = four.replace(curr_map['d'],'')
    one = find1(signal)
    for letter in four:
        if letter not in one:
            curr_map['b'] = letter
            return

def findf(signal):
    for i in signal:
        if len(i) == 5:
            i = i.replace(curr_map['a'],'')
            i = i.replace(curr_map['b'],'')
            i = i.replace(curr_map['d'],'')
            i = i.replace(curr_map['g'],'')
            if len(i) == 1:
                curr_map['f'] = i
                return

def finde(signal):
    eight = find8(signal)
    for key in curr_map:
        eight = eight.replace(curr_map[key], '')
    curr_map['e'] = eight

def findc(signal):
    one = find1(signal)
    one = one.replace(curr_map['f'],'')
    curr_map['c'] = one

def getValue(num):
    if len(num) == 2:
        return 1
    if len(num) == 4:
        return 4
    if len(num) == 3:
        return 7
    if len(num) == 7:
        return 8
    if curr_map['a'] in num and curr_map['b'] in num and curr_map['c'] in num and curr_map['e'] in num and curr_map['g'] in num and curr_map['f'] in num:
        return 0
    if curr_map['a'] in num and curr_map['c'] in num and curr_map['d'] in num and curr_map['e'] in num and curr_map['g'] in num:
        return 2
    if curr_map['a'] in num and curr_map['b'] in num and curr_map['d'] in num and curr_map['c'] in num and curr_map['f'] in num and curr_map['g'] in num:
        return 9
    if curr_map['a'] in num and curr_map['c'] in num and curr_map['d'] in num and curr_map['f'] in num and curr_map['g'] in num:
        return 3
    if curr_map['a'] in num and curr_map['b'] in num and curr_map['d'] in num and curr_map['e'] in num and curr_map['f'] in num and curr_map['g'] in num:
        return 6
    if curr_map['a'] in num and curr_map['b'] in num and curr_map['d'] in num and curr_map['f'] in num and curr_map['g'] in num:
        return 5
    

def getRowValue(digits):
    num = 0
    multiplier = 1000
    for i in range(0,4):
        num += multiplier*getValue(digits[i])
        multiplier = multiplier/10
    return num

for line in file:
    parts = line.split(" | ")
    before_curr = parts[0].split(" ")
    after_curr = parts[1].split(" ")
    after_curr[len(after_curr) - 1] = after_curr[len(after_curr) - 1].strip()
    before.append(before_curr)
    after.append(after_curr)

curr_map = {}
totalCount = 0
for i in range(len(before)):
    curr_map = {}
    finda(before[i])
    finddAndg(before[i])
    findb(before[i])
    findf(before[i])
    findc(before[i])
    finde(before[i])
    rowValue = getRowValue(after[i])
    print(after[i], rowValue)
    totalCount += rowValue

print(totalCount)