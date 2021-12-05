import sys
from sympy import Point, Segment


# Functions forging
def straightLineContains(segment, point):
    if ((segment.p1.x <= point.x <= segment.p2.x or segment.p2.x <= point.x <= segment.p1.x) and
            (segment.p1.y <= point.y <= segment.p2.y or segment.p2.y <= point.y <= segment.p1.y)):
        return True
    else:
        return False

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]
segments = [Segment(Point(i.split(" -> ")[0].split(",")), Point(i.split(" -> ")[1].split(","))) for i in records]

# Clean segments and keep only those with x1 = x2 or y1 = y2
segments = [valid for valid in segments if (valid.p1.x == valid.p2.x or valid.p1.y == valid.p2.y)]

# Get density matrix sizes
matrix_w = 0
matrix_h = 0
for i in segments:
    if max(i.p1.x, i.p2.x) > matrix_w:
        matrix_w = max(i.p1.x, i.p2.x)
    if max(i.p1.y, i.p2.y) > matrix_h:
        matrix_h = max(i.p1.y, i.p2.y)

density_matrix = [[0] * (matrix_w + 1) for _ in range(matrix_h + 1)]

# Fine only if I have only vertical or horizontal lines
for seg in segments:
    # If line is horizontal
    if seg.p1.x == seg.p2.x:
        for y_val in range(min(seg.p1.y, seg.p2.y), max(seg.p1.y, seg.p2.y) + 1):
            density_matrix[y_val][seg.p1.x] += 1
    # If line is vertical
    elif seg.p1.y == seg.p2.y:
        for x_val in range(min(seg.p1.x, seg.p2.x), max(seg.p1.x, seg.p2.x) + 1):
            density_matrix[seg.p1.y][x_val] += 1

counter = 0
for row in density_matrix:
    for val in row:
        if val >= 2:
            counter += 1

print("Here's your value Sir. : ", counter)
