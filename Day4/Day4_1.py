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
                return True
        for colNum in range(0, len(self.matrices[0])):
            extractedCoutner = 0
            for rowNum in range(0, len(self.matrices)):
                if (self.matrices[rowNum][colNum]).getPicked()==True:
                    extractedCoutner += 1
            if extractedCoutner == 5:
                return True
        return False

    def getUnmarkedValuesList(self):
        unmarked_list = []
        for row in self.matrices:
            for slot in row:
                if slot.getPicked()==False:
                    unmarked_list.append(slot.getNumber())
        return unmarked_list

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
winning_mat = None
won = False
for index, newExtraction in enumerate(extraction):
    if won:
        break
    else:
        for mat in matrices:
            if won:
                break
            else:
                mat.numberExtracted(newExtraction)
                if index > 4 and mat.isWinning():
                    winning_mat = mat
                    last_number = newExtraction
                    won = True



score = sum(winning_mat.getUnmarkedValuesList())
print(last_number)
print(score)
print("Here's your value Sir. : ", score*last_number)

