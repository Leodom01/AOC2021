import sys

counter = 0

with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [int(i) for i in records]

for index in range(len(records)-1):
    if records[index + 1] > records[index]:
        counter = counter + 1

print('The number is:', counter)
