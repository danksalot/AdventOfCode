from itertools import combinations

with open('Input') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

galaxies = []

def manhattan(a,b):
	return abs(a[0]-b[0]) + abs(a[1]-b[1])

def printGrid():
	for line in lines:
		print(line)
	print('\n')

# Insert empty rows
y = 0
while y < len(lines):
	if lines[y].count('#') == 0:
		lines.insert(y + 1, '.'*len(lines[0]))
		y += 1
	y += 1

# Insert empty columns
x = 0
while x < len(lines[0]):
	if [lines[y][x] for y in range(len(lines))].count('#') == 0:
		for y in range(len(lines)):
			lines[y] = lines[y][:x] + '.' + lines[y][x:]
		x += 1
	x += 1

# printGrid()

for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] == '#':
			galaxies.append((y,x))

total = 0
for pair in combinations(galaxies, 2):
	total += manhattan(pair[0], pair[1])

print('Part 1:', total)