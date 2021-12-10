import sys

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

corruptors = []

for line in records:
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
                corruptors.append(stack.pop())
                break


score = 0

print(corruptors)

for val in corruptors:
    if val == ")":
        score += 3
    elif val == "]":
        score += 57
    elif val == "}":
        score += 1197
    elif val == ">":
        score += 25137

print("Here's your value Sir. : ", score)
