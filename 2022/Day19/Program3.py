from collections import deque
import re

with open('Input') as inFile:
	lines = inFile.read().splitlines()

blueprints = []

ID = 0
ORE_ORE = 1
CLAY_ORE = 2
OBS_ORE = 3
OBS_CLAY = 4
GEO_ORE = 5
GEO_OBS = 6
GEODES = 7

for line in lines:
	blueprintId, oreRobot_ore, clayRobot_ore, obsidianRobot_ore, obsidianRobot_clay, geodeRobot_ore, geodeRobot_obsidian = map(int, re.findall(r'\d+', line))
	blueprints.append([blueprintId, oreRobot_ore, clayRobot_ore, obsidianRobot_ore, obsidianRobot_clay, geodeRobot_ore, geodeRobot_obsidian, 0])

# def getPossibleOrders(blueprint, ore, clay, obsidian):
# 	possibleOrders = []
# 	if (ore // blueprint[ORE_ORE]) > 0:
# 		possibleOrders.append([1,0,0,0,blueprint[ORE_ORE],0,0])
# 	if (ore // blueprint[CLAY_ORE]) > 0:
# 		possibleOrders.append([0,1,0,0,blueprint[CLAY_ORE],0,0])
# 	if min(ore // blueprint[OBS_ORE], clay // blueprint[OBS_CLAY]) > 0:
# 		possibleOrders.append([0,0,1,0,blueprint[OBS_ORE],blueprint[OBS_CLAY],0])
# 	if min(ore // blueprint[GEO_ORE], obsidian // blueprint[GEO_OBS]) > 0:
# 		possibleOrders.append([0,0,0,1,blueprint[GEO_ORE],0,blueprint[GEO_OBS]])
# 	return possibleOrders

# def canImprove(geodeRobots, timeRemaining, currentGeodes, maxGeodes):
# 	bestPossible = currentGeodes + sum([geodeRobots + t for t in range(timeRemaining + 1)])
# 	return bestPossible > maxGeodes

# def bfs(blueprint, timelimit):
# 	print('Working on blueprint', blueprint[ID])
	# kyew = set()
	# kyew.add((1,0,0,0,0,0,0,0,timelimit))
# 	maxGeodes = 0
# 	while kyew:
# 		r1, r2, r3, r4, o, c, ob, g, t = kyew.pop()
# 		orders = getPossibleOrders(blueprint, o, c, ob)
# 		o += r1
# 		c += r2
# 		ob += r3
# 		g += r4
# 		if g > maxGeodes:
# 			print('Found new max:', g)
# 			maxGeodes = g
# 		newTime = t-1
# 		if newTime > 0:
# 			noBuyState = (r1, r2, r3, r4, o, c, ob, g, newTime)
# 		if newTime > 1 and canImprove(r4, newTime, g, maxGeodes):
# 			kyew.add(noBuyState)
# 			for newR1, newR2, newR3, newR4, usedO, usedC, usedObs in orders:
# 				newState = (r1+newR1, r2+newR2, r3+newR3, r4+newR4, o-usedO, c-usedC, ob-usedObs, g, newTime)
# 				kyew.add(newState)
# 		# print(len(kyew))
# 	return maxGeodes

def bfs(blueprint, timelimit):
	kyew = deque([(1,0,0,0,0,0,0,0)])
	maxGeodes = 0
	for t in range(timelimit):
		nextIteration = set()
		maxGeodes = 0
		maxPossible = 0
		while kyew:
			r1, r2, r3, r4, o, c, ob, g = kyew.pop()
			newOre = o + r1
			newClay = c + r2			
			newObs = ob + r3
			newGeodes = g + r4
			maxGeodes = max(newGeodes, maxGeodes)
			maxPossible = max(maxPossible, newGeodes + r4 * (timelimit - 1 - t))


			# We can already make a new GeoRobot every turn
			# Set newClay to 0 so we won't make more and it will reduce unique kyew
			if r3 >= blueprint[GEO_OBS]: newClay = 0

			if t < timelimit - 1 and g + r4 * 2 * (timelimit - 1 - t) >= maxPossible:

				kyew.appendleft((r1, r2, r3, r4, newOre, newClay, newObs, newGeodes))
				if o >= blueprint[ORE_ORE] and r1 < max(blueprint[CLAY_ORE], blueprint[OBS_ORE], blueprint[GEO_ORE]):
					kyew.appendleft((r1+1, r2, r3, r4, newOre-blueprint[ORE_ORE], newClay, newObs, newGeodes))
				if o >= blueprint[CLAY_ORE] and r2 < blueprint[OBS_CLAY]:
					kyew.appendleft((r1, r2+1, r3, r4, newOre-blueprint[CLAY_ORE], newClay, newObs, newGeodes))
				if o >= blueprint[OBS_ORE] and c >= blueprint[OBS_CLAY] and r3 < blueprint[GEO_OBS]:
					kyew.appendleft((r1, r2, r3+1, r4, newOre-blueprint[OBS_ORE], newClay-blueprint[OBS_CLAY], newObs, newGeodes))
				if o >= blueprint[GEO_ORE] and ob >= blueprint[GEO_OBS]:
					kyew.appendleft((r1, r2, r3, r4+1, newOre-blueprint[GEO_ORE], newClay, newObs-blueprint[GEO_OBS], newGeodes))
	return maxGeodes


# for i in range(len(blueprints)):
# 	blueprints[i][GEODES] = bfs(blueprints[i], 24)

# print('Part 1:', sum([b[ID] * b[GEODES] for b in blueprints]))

for i in range(3):
	blueprints[i][GEODES] = bfs(blueprints[i], 32)

print('Part 2:', blueprints[0][GEODES] * blueprints[1][GEODES] * blueprints[2][GEODES])