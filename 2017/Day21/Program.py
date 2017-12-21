import numpy as np
from math import sqrt

rules = []
picture = np.array([['.','#','.'],['.','.','#'],['#','#','#']])

def splitArray(array, numRows, numCols):
	height, width = array.shape
	return (array.reshape(height // numRows, numRows, -1, numCols).swapaxes(1, 2).reshape(-1, numRows, numCols))

def combineArray(array, height, width):
	n, numRows, numCols = array.shape
	return (array.reshape(height // numRows, -1, numRows, numCols).swapaxes(1, 2).reshape(height, width))

with open('Input') as inFile:
	lines = map(str.rstrip, inFile.readlines())

for line in lines:
	parts = line.split(' => ')
	
	before = [list(x) for x in parts[0].split('/')]
	beforeHFlip = before[::-1]
	beforeVFlip = [x[::-1] for x in before]
	beforeR1 = list(list(x) for x in zip(*before[::-1]))
	beforeR1HFlip = beforeR1[::-1]
	beforeR1VFlip = [x[::-1] for x in beforeR1]
	beforeR2 = list(list(x) for x in zip(*beforeR1[::-1]))
	beforeR3 = list(list(x) for x in zip(*beforeR2[::-1]))
	after = [list(x) for x in parts[1].split('/')]

	b1 = '/'.join([''.join(x) for x in before])
	b2 = '/'.join([''.join(x) for x in beforeHFlip])
	b3 = '/'.join([''.join(x) for x in beforeVFlip])
	b4 = '/'.join([''.join(x) for x in beforeR1])
	b5 = '/'.join([''.join(x) for x in beforeR1HFlip])
	b6 = '/'.join([''.join(x) for x in beforeR1VFlip])
	b7 = '/'.join([''.join(x) for x in beforeR2])
	b8 = '/'.join([''.join(x) for x in beforeR3])

	rules.append([b1, b2, b3, b4, b5, b6, b7, b8, after])

#for rule in rules:
	#print(rule)

for i in range(1):
	newArray = np.array([])
	currentWidth = len(picture[0])
	arrayParts = []
	if (currentWidth % 2 == 0):
		arrayParts = splitArray(picture, 2, 2)
	else:
		arrayParts = splitArray(picture, 3, 3)
	newWidth = int(currentWidth + sqrt(len(arrayParts)))
	print(newWidth)
	for i, part in enumerate(arrayParts):

		for rule in rules:
			if '/'.join([''.join(x) for x in part]) in rule[:-1]:
				arrayParts[i] = rule[-1]
			#else:
				#print('Nope')
		#print(part)

	print(arrayParts)
	picture = combineArray(arrayParts, 12, 12)

	print(picture)