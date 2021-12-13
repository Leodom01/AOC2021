import sys
import copy


# Function forging
def split(word):
    return [copy.copy(int(char)) for char in word]


def increaseSurroundings(matrix, matrix_flash, row_index, col_index):
    max_height = len(matrix)
    max_width = len(matrix[0])
    if row_index >= 1:
        if not matrix_flash[row_index - 1][col_index]:
            matrix[row_index - 1][col_index] += 1
    if row_index < max_height - 1:
        if not matrix_flash[row_index + 1][col_index]:
            matrix[row_index + 1][col_index] += 1
    if col_index >= 1:
        if not matrix_flash[row_index][col_index - 1]:
            matrix[row_index][col_index - 1] += 1
    if col_index < max_width - 1:
        if not matrix_flash[row_index][col_index + 1]:
            matrix[row_index][col_index + 1] += 1
    if col_index >= 1 and row_index >= 1:
        if not matrix_flash[row_index - 1][col_index - 1]:
            matrix[row_index - 1][col_index - 1] += 1
    if col_index < max_width - 1 and row_index >= 1:
        if not matrix_flash[row_index - 1][col_index + 1]:
            matrix[row_index - 1][col_index + 1] += 1
    if row_index < max_height - 1 and col_index >= 1:
        if not matrix_flash[row_index + 1][col_index - 1]:
            matrix[row_index + 1][col_index - 1] += 1
    if row_index < max_height - 1 and col_index < max_width - 1:
        if not matrix_flash[row_index + 1][col_index + 1]:
            matrix[row_index + 1][col_index + 1] += 1


def checkGrtrt9(thisMatrix):
    for row in thisMatrix:
        for octopus in row:
            if octopus > 9:
                return True
    return False

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

matrix = [split(row) for row in records]
matrix_flash = [[False for _ in row] for row in matrix]

flash_count = 0
step = 100

# For every step
    # Reset flashed_matrix
    # Update all octo adding 1
    # While I still have sono octo with more than 9
        # Flash all octo with more than 9 and increse flash_count and add them to flashed_matrix
        # add 1 to all neighbours

for step_no in range(step):
    # Reset flashed_matrix
    matrix_flash = [[False for _ in row] for row in matrix]
    # Update all octo adding 1
    for r_index, row in enumerate(matrix):
        for c_index, octo in enumerate(row):
            matrix[r_index][c_index] += 1
    # While I still have some octo with more than 9
    while checkGrtrt9(matrix):
        for r_index, row in enumerate(matrix):
            for c_index, octo in enumerate(row):
                if matrix[r_index][c_index] > 9:
                    flash_count += 1
                    matrix_flash[r_index][c_index] = True
                    matrix[r_index][c_index] = 0
                    increaseSurroundings(matrix, matrix_flash, r_index, c_index)



for row in matrix:
    print(row)

print("Here's your value Sir. : ", flash_count)
