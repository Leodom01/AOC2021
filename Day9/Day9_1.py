import sys

# Function forging
def findMins(matrix):
    mins = []
    for r_index, row in enumerate(matrix):
        for c_index, val in enumerate(row):
            is_min = True
            if r_index > 0:
                if matrix[r_index-1][c_index] <= val:
                    is_min = False
            if r_index < len(matrix)-1 and is_min:
                if matrix[r_index+1][c_index] <= val:
                    is_min = False
            if c_index > 0 and is_min:
                if matrix[r_index][c_index-1] <= val:
                    is_min = False
            if c_index < len(row)-1 and is_min:
                if matrix[r_index][c_index+1] <= val:
                    is_min = False
            if is_min:
                mins.append(val)
    return mins


# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

heights = [[0 for x in range(len(records[0]))] for y in range(len(records))]
for index, row in enumerate(records):
    for val in range(len(row)):
        heights[index][val] = int(row[val])

# Juicy part
mins = findMins(heights)

print("Here's your value Sir. : ", sum(mins)+len(mins))
