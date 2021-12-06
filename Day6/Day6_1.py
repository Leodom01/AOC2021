import sys

# Function forging
# Fish_list as parameters and move everything one day forward and spawns new babies
def oneDayOver(fishes):
    new_born = fishes[0]
    for i in range(len(fishes)-1):
        fishes[i] = fishes[i+1]
        if i == 6:
            fishes[i] += new_born
    fishes[8] = new_born

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]
records = records[0].split(",")
records = [int(i) for i in records]

fish_list = []

for index in range(9):
    fish_list.append(records.count(index))

# Juicy part
days_to_wait = 256
for _ in range(days_to_wait):
    oneDayOver(fish_list)

print("Here's your value Sir. : ", sum(fish_list))
#for index in range(len(fish_list)):
#    print(index, " Giorni: ", fish_list[index])
