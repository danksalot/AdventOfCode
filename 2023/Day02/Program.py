import re

with open('Input') as inFile:
	lines = inFile.readlines()

maxRed = 12
maxGreen = 13
maxBlue = 14
total = 0
totalPower = 0

for line in lines:
	minRed = 0
	minGreen = 0
	minBlue = 0
	possible = True

	digits = re.findall(r'\d+', line)
	id = int(digits[0])

	reds = [int(r) for r in re.findall(r'(\d+) red', line)]
	if max(reds) > minRed:
		minRed = max(reds)
	if max(reds) > maxRed:
		possible = False

	greens = [int(g) for g in re.findall(r'(\d+) green', line)]
	if max(greens) > minGreen:
		minGreen = max(greens)
	if max(greens) > maxGreen:
		possible = False

	blues = [int(b) for b in re.findall(r'(\d+) blue', line)]
	if max(blues) > minBlue:
		minBlue = max(blues)
	if max(blues) > maxBlue:
		possible = False

	if possible:
		total += id
	totalPower += minRed * minGreen * minBlue
	
print('Part 1: ', total)
print('Part 2: ', totalPower)