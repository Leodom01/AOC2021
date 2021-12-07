import sys

# Function forging
def aligntToX(crabs, x):
    total = 0
    for c in crabs:
        total += abs(x-c)
    return total

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]
records[0] = records[0].split(",")
records = [int(i) for i in records[0]]

crab_dist = []
[crab_dist.append(c) for c in records if c not in crab_dist]

# Juicy part
best_result = -1

for dist in range(min(crab_dist), max(crab_dist)+1):
    cost = aligntToX(records, dist)
    if cost < best_result or best_result == -1:
        best_result = cost

print("Here's your value Sir. : ", best_result)

