import sys


# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

output_vals = [line.split("|")[1] for line in records]

easy_digits = 0

for line in output_vals:
    for val in line.split(" "):
        length = len(val)
        if length in (2, 3, 4, 7):
            easy_digits += 1

print("Here's your value Sir. : ", easy_digits)