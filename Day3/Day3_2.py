import sys
import statistics

# Function forging
def getColumn(colNo, matrix):
    listToRet = []
    for row in matrix:
        listToRet.append(int(row[colNo]))
    return listToRet

def getO2(matrix, colToTest: int):
    if len(matrix) == 1:
        return str(''.join(matrix[0]))
    else:
        column = getColumn(colToTest, matrix)
        bitToKeep = round(statistics.mean(column)+1) - 1
        #Delete rows without bitToKeep at position colToTest
        for row in matrix.copy():
            if int(row[colToTest]) != bitToKeep:
                matrix.remove(row)
        return getO2(matrix, colToTest+1)

def getCO2(matrix, colToTest: int):
    if len(matrix) == 1:
        return str(''.join(matrix[0]))
    else:
        column = getColumn(colToTest, matrix)
        bitToKeep = 1 - (round(statistics.mean(column) + 1) - 1)
        # Delete rows without bitToKeep at position colToTest
        for row in matrix.copy():
            if int(row[colToTest]) != bitToKeep:
                matrix.remove(row)
        return getCO2(matrix, colToTest + 1)

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]
rec_matrix = []

#Move the list of rows in a matrix of characters 1/0
for row in range(len(records)):
    rec_matrix.append([])
    for col in range(len(records[0])):
        rec_matrix[row].append((records[row])[col])

#print(rec_matrix)

#Juicy part
O2  =   int(getO2(rec_matrix.copy(), 0), 2)
CO2 =   int(getCO2(rec_matrix.copy(), 0), 2)

print("O2 and CO2: ", O2, CO2)
print("Your value Sir: ", O2*CO2)