data = "11101000110010100"
diskLength = 272	# Part2 - 35651584

while len(data) < diskLength:
	data += "0" + ''.join("0" if n == "1" else "1" for n in data[::-1])

checksum = data[:diskLength]

while len(checksum) % 2 == 0:
	checksum = ''.join("1" if x == y else "0" for x, y in zip(checksum[0::2], checksum[1::2]))

print checksum