import sys
import copy
import numpy as np

# Function forging
def renderPoints(pointList):
    max_x = -1
    max_y = -1
    for currentPoint in pointList:
        if currentPoint[0] > max_x:
            max_x = currentPoint[0]
        if currentPoint[1] > max_y:
            max_y = currentPoint[1]
    matrix = np.full((max_x+1, max_y+1), ".")
    for currentPoint in pointList:
        matrix[currentPoint[0], currentPoint[1]] = "#"

    print(matrix)

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]
records = [str(i) for i in records]

points = []
foldList = []

for line in records:
    split_line = line.split(",")
    if (len(split_line) == 2):
        x_coord = int(split_line[0])
        y_coord = int(split_line[1])
        points.append([x_coord, y_coord])
    else:
        if line.__contains__("fold along y="):
            foldList.append(["y", int(line.replace('fold along y=', ''))])
        elif line.__contains__("fold along x="):
            foldList.append(["x", int(line.replace('fold along x=', ''))])

# Hard worker

for currentFold in foldList:
    if currentFold[0] == "x":
        print("Folding x")
        for point in points:
            if point[0] > currentFold[1]:
                distFromLine = point[0] - currentFold[1]
                point[0] -= distFromLine * 2
    elif currentFold[0] == "y":
        print("Folding y")
        for point in points:
            if point[1] > currentFold[1]:
                distFromLine = point[1] - currentFold[1]
                point[1] -= distFromLine * 2
    finalSet = set()
    for point in points:
        finalSet.add(tuple(point))
    points = list(finalSet)
    for i in range(len(points)):
        points[i] = list(points[i])

renderPoints(points)
