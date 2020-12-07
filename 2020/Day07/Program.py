def findContainers(rules, bagDesc):
	canContain = []
	for rule in rules:
		if bagDesc in rules[rule].keys():
			canContain.append(rule)
	return canContain

def findContents(rules, bagDesc):
	return sum([rules[bagDesc][childBagDesc] * findContents(rules, childBagDesc) for childBagDesc in rules[bagDesc]]) + 1

with open('Input') as inFile:
	lines = inFile.read().splitlines()

rules = {}
for line in lines:
	parts = line.split()
	rules[parts[0] + parts[1]] = {}
	if len(parts) >= 8:
		rules[parts[0] + parts[1]][parts[5] + parts[6]] = int(parts[4])
	if len(parts) >= 12:
		rules[parts[0] + parts[1]][parts[9] + parts[10]] = int(parts[8])
	if len(parts) >= 16:
		rules[parts[0] + parts[1]][parts[13] + parts[14]] = int(parts[12])
	if len(parts) >= 20:
		rules[parts[0] + parts[1]][parts[17] + parts[18]] = int(parts[16])

containers = ['shinygold']
previousCount = len(containers)
while True:
	new = []
	for container in containers:
		new.extend(findContainers(rules, container))
	containers = list(set(containers + new))
	if len(containers) == previousCount:
		break
	previousCount = len(containers)

print('Part 1:', len(containers) - 1)
print('Part 2:', findContents(rules, 'shinygold') - 1)