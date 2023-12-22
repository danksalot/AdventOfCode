from copy import deepcopy

with open('fallen') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

def fillCubesBetween(a, b):
	ax, ay, az = a
	bx, by, bz = b
	cubes = []

	if ax < bx:
		cubes.append(a)
		for x in range(ax+1, bx):
			cubes.append([x, ay, az])
		cubes.append(b)
	elif bx < ax:
		cubes.append(b)
		for x in range(bx+1, ax):
			cubes.append([x, ay, az])
		cubes.append(a)
	elif ay < by:
		cubes.append(a)
		for y in range(ay+1, by):
			cubes.append([ax, y, az])
		cubes.append(b)
	elif by < ay:
		cubes.append(b)
		for y in range(by+1, ay):
			cubes.append([ax, y, az])
		cubes.append(a)
	elif az < bz:
		cubes.append(a)
		for z in range(az+1, bz):
			cubes.append([ax, ay, z])
		cubes.append(b)
	elif bz < az:
		cubes.append(b)
		for z in range(bz+1, az):
			cubes.append([ax, ay, z])
		cubes.append(a)
	else:
		cubes.append(a)
	return cubes

def getSupportingBricks(brick, bricks):	
	supportingBricks = []
	for cube in brick:
		ax, ay, az = cube
		for brick in bricks:
			if cube in brick:
				continue
			if any(ax == bx and ay == by and az - 1 == bz for bx, by, bz in brick):
				if brick not in supportingBricks:
					supportingBricks.append(brick)
	return supportingBricks

def fall(bricks):
	fell = True
	fallen = []
	while fell:
		# print('Falling bricks...')
		fell = False
		for brick in bricks:
			if len(getSupportingBricks(brick, bricks)) == 0 and min(z for x, y, z in brick) > 1:
				# print('Brick falling!', brick)
				for c in brick:
					c[2] -= 1
				fell = True
				if brick not in fallen:
					fallen.append(brick)
	return len(fallen)

bricks = []

for i in range(len(lines)):
	ends = lines[i].split('~')
	end1 = list(map(int, ends[0].split(',')))
	end2 = list(map(int, ends[1].split(',')))
	bricks.append(fillCubesBetween(end1, end2))

# print(bricks)

numFallen = fall(bricks)
# print(numFallen)

# with open('fallen', 'w') as outFile:
# 	for brick in bricks:
# 		outFile.write(str(brick) + '\n')

# print(bricks)

# def canBeRemoved(brick, bricks):
# 	withoutBrickA = deepcopy(bricks)
# 	withoutBrickA.remove(brick)
# 	withoutBrickB = deepcopy(withoutBrickA)
# 	fall(withoutBrickA)
# 	canBeRemoved = True
# 	for i in range(len(withoutBrickA)):
# 		for j in range(len(withoutBrickA[i])):
# 			for k in range(3):
# 				if withoutBrickA[i][j][k] != withoutBrickB[i][j][k]:
# 					canBeRemoved = False
# 					continue
# 	return canBeRemoved

# for i in range(len(bricks)):
# 	print('Checking brick', i)
# 	if canBeRemoved(bricks[i], bricks):
# 		print('Brick can be removed!', bricks[i])

# print('Part 1:', len([b for b in bricks if canBeRemoved(b, bricks)]))

candidatesForRemoval = deepcopy(bricks)
for brick in bricks:
	# print('Checking brick', brick)
	supporting = getSupportingBricks(brick, bricks)
	if len(supporting) == 1:
		remove = supporting.pop()
		if remove in candidatesForRemoval:
			# print('Brick can not be removed!', remove)
			candidatesForRemoval.remove(remove)

print('Part 1:', len(candidatesForRemoval))

sum = 0
for brick in [b for b in bricks if b not in candidatesForRemoval]:
	test = deepcopy(bricks)
	test.remove(brick)
	numFallen = fall(test)
	print('Brick', brick, 'removal results in', numFallen, 'fallen bricks')
	sum += numFallen

print('Part 2:', sum)