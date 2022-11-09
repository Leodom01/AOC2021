from collections import Counter

# Function forging
def pairwise(myList):
    returnList = []
    for i in range(len(myList)-1):
        returnList.append(myList[i]+myList[i+1])
    return returnList

def getLeaderboardFromCounter(counter):
    returnDict = {}
    for couple, val in counter.items():
        if couple[0] in returnDict.keys():
            returnDict[couple[0]] = returnDict[couple[0]]+val
        else:
            returnDict[couple[0]] = val
        if couple[1] in returnDict.keys():
            returnDict[couple[1]] = returnDict[couple[1]]+val
        else:
            returnDict[couple[1]] = val
    return returnDict

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]
records = [str(i) for i in records]

template = records[0]
rules = dict()
for i in range(2, len(records)):
    rules[records[i].split(" -> ")[0]] = records[i].split(" -> ")[1]


# Hard worker
STEPS = 40

bigCounter = Counter(rules.keys())
bigCounter.subtract(rules.keys())

bigCounter.update(pairwise(template))

for i in range(STEPS):
    for couple, iterations in bigCounter.copy().items():
        if iterations == 0:
            continue
        firstItem = couple[0]
        secondItem = couple[1]
        middleItem = rules.get(couple)
        bigCounter[couple] -= iterations
        bigCounter[firstItem + middleItem] += iterations
        bigCounter[middleItem + secondItem] += iterations

#Now count the occurences given the finalPolymer list
finalBoard = getLeaderboardFromCounter(bigCounter)
for item, val in finalBoard.items():
    if item == template[0] or item == template[-1]:
        finalBoard[item] = int((val+1) / 2)
    else:
        finalBoard[item] = int(val / 2)

top = (list(finalBoard.items())[0][0], list(finalBoard.items())[0][1])
flop = (list(finalBoard.items())[0][0], list(finalBoard.items())[0][1])

for item, val in finalBoard.items():
    if val > top[1]:
        top = (item, val)
    elif val < flop[1]:
        flop = (item, val)

print(top[1] - flop[1])
