total = 0
values = []
firstTime = True

while True:
	with open('Input') as inFile:
		for line in inFile.read().splitlines():
			num = line.replace('+', '')
			total += int(num)
			if (total in values):
				print('Part 2:', total)
				exit();
			else:
				values.append(total)

	if (firstTime):
		print('Part 1:', total)
		firstTime = False