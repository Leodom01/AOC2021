import sys

forward = 0
depth = 0
aim = 0


# Functions definition
def aimChange(delta):
    global aim
    aim += delta


def forwardChange(delta):
    global forward
    global aim
    global depth
    forward += delta
    depth += delta*aim


# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

# Juicy part
for line in records:
    direction = line.split(" ")[0]
    value = int(line.split(" ")[1])
    if direction == "forward":
        forwardChange(value)
    elif direction == "down":
        aimChange(value)
    else:
        aimChange(-value)

print("You value is: ", forward*depth)