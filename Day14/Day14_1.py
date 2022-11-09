import sys
import copy

# Function forging


# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]
records = [str(i) for i in records]

template = records[0]
rules = dict()
for i in range(2, len(records)):
    rules[records[i].split(" -> ")[0]] = records[i].split(" -> ")[1]

# Hard worker
finalPolymer = template
for cycle in range(10):
    print(finalPolymer)
    newPolymer = ""
    for index in range(len(finalPolymer)-1):
        firstItem = finalPolymer[index]
        secondItem = finalPolymer[index+1]
        if (firstItem+secondItem) in rules.keys():
            newPolymer = newPolymer+(firstItem+rules.get(firstItem+secondItem))
        else:
            newPolymer = newPolymer+firstItem
    newPolymer = newPolymer+finalPolymer[len(finalPolymer)-1]
    finalPolymer = newPolymer

#Now count the occurences
occurrences = []
while len(finalPolymer) > 0:
    firstChar = finalPolymer[0]
    occurrences.append([firstChar, finalPolymer.count(firstChar)])
    finalPolymer = finalPolymer.replace(firstChar, '')

higher = ['A', -1]
lower = ['A', None]
for charOcc in occurrences:
    if charOcc[1] > higher[1]:
        higher = charOcc
    elif lower[1] is None or charOcc[1] < lower[1]:
        lower = charOcc

print(higher[1]-lower[1])