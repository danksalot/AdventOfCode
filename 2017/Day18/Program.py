regs = {'a': 0, 'b': 0, 'i': 0, 'f': 0, 'p': 0 }
current = 0
sound = 0

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

def getValue(x):
	if is_digit(x):
		return int(x)
	else:
		return regs[x]

def snd(x):
	global sound
	sound = getValue(x)

def set(x, y):
	regs[x] = getValue(y)

def add(x, y):
	regs[x] += getValue(y)

def mul(x, y):
	regs[x] *= getValue(y)

def mod(x, y):
	regs[x] %= getValue(y)

def rcv(x):
	if getValue(x) != 0:
		print sound
		exit()

def jgz(x, y):
	global current
	if getValue(x) > 0:
		current += getValue(y) - 1

with open('Input') as inFile:
	lines = map(str.rstrip, inFile.readlines())

while current >= 0 and current < len(lines):
	parts = lines[current].split(' ')
	if parts[0] == 'snd':
		snd(parts[1])
	elif parts[0] == 'set':
		set(parts[1], parts[2])
	elif parts[0] == 'add':
		add(parts[1], parts[2])
	elif parts[0] == 'mul':
		mul(parts[1], parts[2])
	elif parts[0] == 'mod':
		mod(parts[1], parts[2])
	elif parts[0] == 'rcv':
		rcv(parts[1])
	elif parts[0] == 'jgz':
		jgz(parts[1], parts[2])
	current += 1

print 'Ran out of instructions'