import sys


# Class and function forging
class Slot:
    def __init__(self, number, picked=False):
        self.number = number
        self.picked = picked

    def __str__(self):
        return self.number+" extracted: "+str(self.picked)

    def __repr__(self):
        return self.__str__()

    def getNumber(self):
        return int(self.number)

    def getPicked(self):
        return bool(self.picked)

    def numberExtracted(self, numExtraction):
        if self.getNumber() == numExtraction:
            self.picked = True

class SlotMatrix:
    def __init__(self, matrices):
        self.matrices = matrices
        self.won = False

    def __str__(self):
        strToRet = "["
        for row in self.matrices:
            strToRet = strToRet+row.__str__()+'\n'
        return strToRet+"]"

    def __repr__(self):
        return self.__str__()

    def numberExtracted(self, number):
        for row in self.matrices:
            for slot in row:
                slot.numberExtracted(number)

    def isWinning(self):
        for row in self.matrices:
            extractedCoutner = 0
            extractedCoutner = [extractedCoutner+1 for slot in row if slot.getPicked()==True]
            if sum(extractedCoutner) == 5:
                self.won = True
                return True
        for colNum in range(0, len(self.matrices[0])):
            extractedCoutner = 0
            for rowNum in range(0, len(self.matrices)):
                if (self.matrices[rowNum][colNum]).getPicked()==True:
                    extractedCoutner += 1
            if extractedCoutner == 5:
                self.won = True
                return True
        return False

    def getUnmarkedValuesList(self):
        unmarked_list = []
        for row in self.matrices:
            for slot in row:
                if slot.getPicked()==False:
                    unmarked_list.append(slot.getNumber())
        return unmarked_list

    def getWonState(self):
        return bool(self.won)

# Defining global variables
# List of all the numbers to be extracted
extraction = []

# List of all the matrix in game
matrices = []

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

extraction = records[0].split(",")
extraction = [int(i) for i in extraction]

support_matrix = []

for rowIndex in range(2, len(records)):
    new_row = list(filter(None, records[rowIndex].strip().split(" ")))
    if len(new_row) == 0:
        matrices.append(SlotMatrix(support_matrix))
        support_matrix = []
        continue
    new_row = [Slot(i) for i in new_row]
    support_matrix.append(new_row)
matrices.append(SlotMatrix(support_matrix))

# Juicy part
while len(matrices) > 1:
    newExtraction = extraction.pop(0)
    for mat in matrices.copy():
        mat.numberExtracted(newExtraction)
        if mat.isWinning():
            matrices.remove(mat)

while not matrices[0].isWinning():
    newExtraction = extraction.pop(0)
    matrices[0].numberExtracted(newExtraction)

losing_mat = matrices[0]
score = sum(losing_mat.getUnmarkedValuesList())

print("Here's your value Sir. : ", score*newExtraction)

