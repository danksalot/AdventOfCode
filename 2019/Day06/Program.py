objects = {}
com = None
numOrbits = 0

with open('Input') as inFile:
	lines = inFile.read().split('\n')
	objects = [line.split(")") for line in lines]
	orbits = { orbiter:{ 'parent': orbitee} for orbitee, orbiter in objects }

for currentObject in orbits.keys():
	while currentObject != 'COM':
		currentObject = orbits[currentObject]['parent']
		numOrbits += 1

print("Part 1:", numOrbits)

myPath = ['YOU']
while 'COM' not in myPath:
	nextParent = orbits[myPath[-1]]['parent']
	myPath.append(nextParent)

santaPath = ['SAN']
while 'COM' not in santaPath:
	nextParent = orbits[santaPath[-1]]['parent']
	santaPath.append(nextParent)

print("Part 2:", len(set(myPath) ^ set(santaPath)) - 2)