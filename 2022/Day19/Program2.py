import sys
import json
sys.setrecursionlimit(3000000)

MAXT = 32

ans = 1

with open('Input') as inFile:
	lines = inFile.read().splitlines()

for line in lines:
    line = line.strip()
    if line == "": continue
    words = line.split()
    num = int(words[1][:-1])
    ore_rob = int(words[6])
    
    clay_rob = int(words[12])
    
    ob_ore = int(words[18])
    ob_clay = int(words[21])

    ge_ore = int(words[27])
    ge_ob = int(words[30])

    states = [(0, 0, 0, 0, 1, 0, 0, 0)]
    maxGeodes = 0
    for t in range(MAXT):
        newStates = set()
        maxGeodes = 0
        maxPossible = 0
        for state in states:
            o, c, ob, g, r1, r2, r3, r4 = state
            newOre = o+r1
            newClay = c+r2
            if r3 >= ge_ob:
                newClay = 0
            newObs = ob+r3
            newGeodes = g+r4
            maxGeodes = max(newGeodes, maxGeodes)
            maxPossible = max(newGeodes+r4*(MAXT-1-t), maxPossible)
            newStates.add((newOre, newClay, newObs, newGeodes, r1, r2, r3, r4))
            if o >= ore_rob and r1 < max(clay_rob, ob_ore, ge_ore):
                newStates.add((newOre-ore_rob, newClay, newObs, newGeodes, r1+1, r2, r3, r4))
            if o >= clay_rob and r2 < ob_clay:
                newStates.add((newOre-clay_rob, newClay, newObs, newGeodes, r1, r2+1, r3, r4))
            if o >= ob_ore and c >= ob_clay and r3 < ge_ob:
                newStates.add((newOre-ob_ore, newClay-ob_clay, newObs, newGeodes, r1, r2, r3+1, r4))
            if o >= ge_ore and ob >= ge_ob:
                newStates.add((newOre-ge_ore, newClay, newObs-ge_ob, newGeodes, r1, r2, r3, r4+1))
        states = set()
        if t < MAXT-1:
            for state in newStates:
                o, c, ob, g, r1, r2, r3, r4 = state
                if g+r4*2*(MAXT-1-t) >= maxPossible:
                    states.add(state)
        # print(num, t, len(states), maxGeodes)
        
    ans *= maxGeodes
    if num == 3:
        break
print(ans)