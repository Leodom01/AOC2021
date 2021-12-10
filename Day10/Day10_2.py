import sys

# Function forging

def oppositeChar(list):
    if len(list) == 0:
        return "None"
    last_char = list.pop()
    if last_char == "(":
        return ")"
    elif last_char == "[":
        return "]"
    elif last_char == "{":
        return "}"
    elif last_char == "<":
        return ">"

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

# Throw away the corrupted, keep the incomplete with the chars without closing only
for line_index, line in enumerate(records):
    stack = []
    for index in range(len(line)):
        stack.append(line[index])
        if len(stack) > 1 and line[index] in (")", "]", "}", ">"):
            if ((stack[len(stack) - 2] == "(" and stack[len(stack) - 1] == ")") or
                    (stack[len(stack) - 2] == "[" and stack[len(stack) - 1] == "]") or
                    (stack[len(stack) - 2] == "{" and stack[len(stack) - 1] == "}") or
                    (stack[len(stack) - 2] == "<" and stack[len(stack) - 1] == ">")):
                stack.pop()
                stack.pop()
            else:
                stack = "None"
                break
    records[line_index] = stack

# Delete all th marked as corrupted
records = [line for line in records if line != 'None']
records = [list(line) for line in records]

# Add missing completers for every line
completers = []
for line in records:
    line_completers = []
    while (this_completer := oppositeChar(line)) != "None":
        line_completers.append(this_completer)
    completers.append(line_completers)

# Count every line score
scores = []

for line in completers:
    score = 0
    for val in range(len(line)):
        score = score*5
        if line[val] == ")":
            score += 1
        elif line[val] == "]":
            score += 2
        elif line[val] == "}":
            score += 3
        elif line[val] == ">":
            score += 4
    scores.append(score)

scores.sort()
print("Here's your value Sir. : ", scores[int((len(scores)-1)/2)])
