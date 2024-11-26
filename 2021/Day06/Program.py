
days = 80

with open('Input') as inFile:
	lanternfish = [int(x) for x in inFile.read().split(',')]

# print(lanternfish)

### TEST ###
#lanternfish = [3,4,3,1,2]
#days = 18
### TEST ###

# print(lanternfish)

for day in range(days):
	numFish = len(lanternfish)
	for l in range(numFish):
		if lanternfish[l] == 0:
			lanternfish.append(8)
			lanternfish[l] = 6
		else:
			lanternfish[l] -= 1

print('Part 1:', len(lanternfish))