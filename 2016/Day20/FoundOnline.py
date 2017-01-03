import sys

rules = []
with open("Input") as inputFile:
    lines = inputFile.readlines()
    
for line in lines:
    lower, upper = map(int, line.split('-'))
    rules.append([lower, upper])

rules.sort()

allowed = 0
ip = 0
ruleIndex = 0

while ip < 2**32:
    lower, upper = rules[ruleIndex]
    if ip >= lower:
        if ip <= upper:
            ip = upper + 1
            continue
        ruleIndex += 1
    else:
        allowed += 1
        ip += 1

print(allowed)