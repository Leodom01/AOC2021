import sys

# Function forging
from typing import List

def isMin(matrix, r_index, c_index):
    val = matrix[r_index][c_index]
    is_min = True
    if r_index > 0:
        if matrix[r_index - 1][c_index] <= val:
            is_min = False
    if r_index < len(matrix) - 1 and is_min:
        if matrix[r_index + 1][c_index] <= val:
            is_min = False
    if c_index > 0 and is_min:
        if matrix[r_index][c_index - 1] <= val:
            is_min = False
    if c_index < len(row) - 1 and is_min:
        if matrix[r_index][c_index + 1] <= val:
            is_min = False
    return is_min


def findBasinSize(matrix, r_index, c_index):
    cell_in_basin[r_index][c_index] = True
    size = 1
    cell = matrix[r_index][c_index]
    if r_index > 0 and cell < matrix[r_index - 1][c_index] != 9 and not cell_in_basin[r_index - 1][c_index]:
        size += findBasinSize(matrix, r_index-1, c_index)
    if r_index < len(matrix)-1 and cell < matrix[r_index + 1][c_index] != 9 and not cell_in_basin[r_index + 1][c_index]:
        size += findBasinSize(matrix, r_index+1, c_index)
    if c_index > 0 and cell < matrix[r_index][c_index - 1] != 9 and not cell_in_basin[r_index][c_index - 1]:
        size += findBasinSize(matrix, r_index, c_index-1)
    if c_index < len(matrix[0])-1 and cell < matrix[r_index][c_index + 1] != 9 and not cell_in_basin[r_index][c_index + 1]:
        size += findBasinSize(matrix, r_index, c_index+1)
    return size


# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

heights = [[0 for x in range(len(records[0]))] for y in range(len(records))]
cell_in_basin: List[List[bool]] = [[False for x in range(len(records[0]))] for y in range(len(records))]
for index, row in enumerate(records):
    for val in range(len(row)):
        heights[index][val] = int(row[val])

# Juicy part
basins_size = []

for r_index, row in enumerate(records):
    for c_index, val in enumerate(row):
        if isMin(heights, r_index, c_index):
            basins_size.append(findBasinSize(heights, r_index, c_index))

basins_size.sort()

print("Here's your value Sir. : ", basins_size[len(basins_size)-1]*basins_size[len(basins_size)-2]*basins_size[len(basins_size)-3])
