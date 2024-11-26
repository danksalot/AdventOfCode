from itertools import permutations
import networkx as nx

G = nx.Graph()
hasFlow = {}
shortestPaths = {}

with open('Input') as inFile:
	lines = inFile.read().splitlines()

for line in lines:
	parts = line.split(';')
	parts0 = parts[0].split(' ')
	name = parts0[1]
	parts1 = parts[0].split('=')
	rate = int(parts1[-1])
	parts2 = parts[1].split("valve ")
	if "valves" in parts[1]:
		parts2 = parts[1].split("valves ")
	paths = parts2[-1].split(', ')

	if rate > 0:
		hasFlow[name] = rate
	for path in paths:
		G.add_edges_from([(name, path)])

for valve in hasFlow:
	shortestPaths[valve] = { other:len(nx.shortest_path(G, valve, other)) for other in hasFlow if other != valve }

shortestPaths['AA'] = { other:len(nx.shortest_path(G, 'AA', other)) for other in hasFlow }

# print(shortestPaths)

def calcFlowForPath(path, timeleft):
	totalFlow = 0
	for i in range(len(path) - 2):
		timeleft -= shortestPaths[path[i][0]][path[i+1][0]]
		if timeleft < 0:
			break
		totalFlow += timeleft * hasFlow[path[i+1][0]]
	return totalFlow

# best = 0
# for perm in permutations(hasFlow.items()):
# 	candidate = [('AA', 0)] + list(perm)#[::-1]
# 	flow = calcFlowForPath(candidate, 30)
# 	if flow > best:
# 		best = flow
# 		print('New best:', best)
# 		print('Found using route:', candidate)

# print('Part 1:', best)


best = 0
for perm in permutations(hasFlow.items()):
	fullperm = [('AA', 0)] + list(perm) + [('AA', 0)]
	me = fullperm
	elephant = fullperm[::-1]
	myFlow = calcFlowForPath(me, 26)
	elFlow = calcFlowForPath(elephant, 26)
	flow = myFlow + elFlow
	if flow > best:
		best = flow
		print('New best:', best)
		print('My route:', me)
		print('Elephant route:', elephant)

print('Part 2:', best)


