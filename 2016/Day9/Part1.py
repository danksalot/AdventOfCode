import re

def getDecompressedLength(string):
	marker = re.search("\((\d+)x(\d+)\)", string)
	if marker == None:
		return len(string)
	else:
		num, times = map(int, re.search("\((\d+)x(\d+)\)", string).groups())
		length = marker.start() + (num * times)		
		index = marker.end() + num
		return length + getDecompressedLength(string[index:])

with open("Input") as inputFile:
	line = inputFile.read()

print "Length after decompressing:", getDecompressedLength(line)