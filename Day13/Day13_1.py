import sys
import copy

# Function forging


# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]
records = [str(i) for i in records]

points = []
fold_x = None
fold_y = None
max_x = -1
max_y = -1

for line in records:
    split_line = line.split(",")
    if (len(split_line) == 2):
        x_coord = int(split_line[0])
        y_coord = int(split_line[1])
        if x_coord > max_x:
            max_x = x_coord
        if y_coord > max_y:
            max_y = y_coord
        points.append([x_coord, y_coord])
    else:
        if fold_x is None and fold_y is None:
            if line.__contains__("fold along y="):
                fold_y = int(line.replace('fold along y=', ''))
            elif line.__contains__("fold along x="):
                fold_x = int(line.replace('fold along x=', ''))

# Hard worker

# Fold x
if fold_x is not None:
    print("Folding x")
    for point in points:
        if point[0] > fold_x:
            distFromLine = point[0] - fold_x
            point[0] -= distFromLine*2

# Fold y
if fold_y is not None:
    print("Folding y")
    for point in points:
        if point[1] > fold_y:
            distFromLine = point[1] - fold_y
            point[1] -= distFromLine*2

finalSet = set()
for point in points:
    finalSet.add(tuple(point))

print(len(finalSet))