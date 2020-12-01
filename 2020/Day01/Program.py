from itertools import combinations
from math import prod

with open('Input') as inFile:
	lines = [int(x) for x in inFile.readlines()]

	for x in combinations(lines, 2):
		if sum(x) == 2020: print('Part 1: ' + str(prod(x)))

	for x in combinations(lines, 3):
		if sum(x) == 2020: print('Part 2: ' + str(prod(x)))
