total = 0
values = []

with open('Input') as inFile:
	print('Part 1', sum(int(line) for line in inFile))

	while True:
		for line in inFile:
			total += int(line)
			if (total in values):
				print('Part 2:', total)
				exit();
			else:
				values.append(total)