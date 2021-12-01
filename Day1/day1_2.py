import sys

counter = 0
windows_sum = []

with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [int(i) for i in records]

for val in range(len(records)-2):
    windows_sum.append(records[val] + records[val+1] + records[val+2])

for index in range(len(windows_sum)-1):
    if windows_sum[index + 1] > windows_sum[index]:
        counter = counter + 1

print('The value is:', counter)