import sys

forward = 0
depth = 0

with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

for line in records:
    direction = line.split(" ")[0]
    value = int(line.split(" ")[1])
    if direction == "forward":
        forward += value
    elif direction == "down":
        depth += value
    else:
        depth -= value

print("You value is: ", forward*depth)


