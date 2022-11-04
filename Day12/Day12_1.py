import sys
import copy

# Function forging

#Check if the path will stay legal even after adding the new item
def staysLegal(path, newItem):
    if not newItem.isupper() and path.count(newItem) >= 1:
        return False
    return True

def nextPaths(caves, currentPath):
    lastItem = currentPath[len(currentPath)-1]
    if lastItem == "end":
        return currentPath
    else:
        nextHops = caves.get(lastItem).split(",")
        newPaths = []
        atLeastOneLegal = False
        for hop in nextHops:
            if staysLegal(currentPath, hop):
                atLeastOneLegal = True
                nextPath = copy.copy(currentPath)
                nextPath.append(hop)
                toAdd = nextPaths(caves, nextPath)
                if toAdd is None:
                    continue
                elif isinstance(toAdd[0], list):
                    for subList in toAdd:
                        newPaths.append(subList)
                else:
                    newPaths.append(toAdd)
        if atLeastOneLegal and len(newPaths) > 0:
            return newPaths
        else:
            return None


# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]
records = [str(i) for i in records]
#Map where key is the cave name and then csv list of connected island
caves = {}
for thisStr in records:
    items = thisStr.split("-")
    if caves.get(items[0]) is None:
        caves[items[0]] = items[1]
    else:
        caves[items[0]] = caves.get(items[0])+","+items[1]
    if caves.get(items[1]) is None:
        caves[items[1]] = items[0]
    else:
        caves[items[1]] = caves.get(items[1])+","+items[0]

# Hard worker
print(len(nextPaths(caves, ["start"])))

