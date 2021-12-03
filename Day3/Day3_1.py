import sys
import statistics

# Function definition
# Get row no rowCol given an array of string all the same length, it considers the colNum-th element of every string and create a list with them
def getIntCol(colNum, stringArray):
    colToRet = []
    for record in stringArray:
        colToRet.append(int(record[colNum]))

    return colToRet


# Global var definition
gamma = ""
epsilon = ""

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

# Juicy part
for colIndex in range(0, len(records[0])):
    newVal = str(int(statistics.median(getIntCol(colIndex, records))))
    gamma = gamma+newVal
    epsilon = epsilon+str(1-int(newVal))

gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)

print("The value is:", gamma * epsilon)
