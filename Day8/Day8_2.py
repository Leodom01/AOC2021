import sys

def nCharsString(strings, n):
    toRet = []
    for str in strings:
        if len(str) == n:
            toRet.append(str)
    return toRet

def stringDiff(stringA, stringB):
    string_support = stringB
    for index, char in enumerate(stringA):
        string_support = string_support.replace(char, "")
    return string_support

def decodeLine(line):
    line = line.strip().split(" ")
    decoded = []
    # At index n there's the correct codification of  number n
    decoded = [decoded.append([]) for _ in range(10)]

    # Fill in the easy values
    for val in line:

        if len(val) == 2:
            decoded[1] = val
        elif len(val) == 4:
            decoded[4] = val
        elif len(val) == 3:
            decoded[7] = val
        elif len(val) == 7:
            decoded[8] = val

    # Find out 6, 9 and 0
    for testing in nCharsString(line, 6):
        if len(stringDiff(decoded[1], testing)) == 5:
            decoded[6] = testing
        elif len(stringDiff(decoded[4], testing)) == 2:
            decoded[9] = testing
        else:
            decoded[0] = testing

    # Find out 2, 3,and 5
    for testing in nCharsString(line, 5):
        if len(stringDiff(decoded[1], testing)) == 3:
            decoded[3] = testing
        elif len(stringDiff(decoded[9], testing)) == 1:
            decoded[2] = testing
        else:
            decoded[5] = testing

    return decoded

def decode_with_dictionary(dictionary, to_decode):
    to_decode = to_decode.strip()
    for index in range(len(dictionary)):
        if sorted(dictionary[index]) == sorted(to_decode):
            return index

# Input reading
with open('input.txt') as f:
    records = [line.rstrip() for line in f]

records = [str(i) for i in records]

encoded_stream = [line.split("|")[0] for line in records]
to_decode_output = [line.split("|")[1] for line in records]

total_sum = 0

for index, line in enumerate(encoded_stream):
    dictionary = decodeLine(line)
    decoded = []
    for encoded in to_decode_output[index].strip().split(" "):
        decoded.append(decode_with_dictionary(dictionary, encoded))

    total_sum += 1000 * decoded[0] + 100 * decoded[1] + 10 * decoded[2] + decoded[3]

print("Here's your value Sir. : ", total_sum)