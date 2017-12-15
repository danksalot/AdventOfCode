valueA = 699
valueB = 124

def genA(current, mod):
	for i in range(40000000):
		current = (current * 16807) % 2147483647
		if current % mod == 0:
			yield current

def genB(current, mod):
	for i in range(40000000):
		current = (current * 48271) % 2147483647
		if current % mod == 0:
			yield current

def compare(left, right):
	return not ((left & 65535) ^ (right & 65535))

GEN_A = genA(699, 1)
GEN_B = genB(124, 1)

matches = 0

while True:	
	valueA = next(GEN_A, None)
	valueB = next(GEN_B, None)
	if valueA and valueB:
		matches += not ((valueA & 65535) ^ (valueB & 65535))
	else:
		break

print 'Part1:', matches

matches = 0
GEN_A = genA(699, 4)
GEN_B = genB(124, 8)

while True:
	valueA = next(GEN_A, None)
	valueB = next(GEN_B, None)
	if valueA and valueB:
		matches += not ((valueA & 65535) ^ (valueB & 65535))
	else:
		break
	
print 'Part2:', matches

