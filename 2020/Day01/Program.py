with open('Input') as inFile:
	lines = [int(x) for x in inFile.readlines()]

	for i in range(len(lines)-1):
		for j in range(1, len(lines)):
			if ((lines[i] + lines[j]) == 2020):
				print('Part 1: ' + str(lines[i] * lines[j]))

	for i in range(len(lines) - 2):
		for j in range(1, len(lines) - 1):
			for k in range(2, len(lines)):
				if ((lines[i] + lines[j] + lines[k]) == 2020):
					print('Part 2: ' + str(lines[i] * lines[j] * lines[k]))
				