from functools import reduce
from itertools import accumulate, zip_longest as zipl
from operator import mul, xor

def reverse_sublist(l, a, b):
    if a <= b: l[a:b] = l[a:b][::-1]
    else: r = (l[a:]+l[:b])[::-1]; l[a:], l[:b] = r[:len(l)-a], r[-b or len(r):]

def hash_round(lens, elems, pos=0, skip=0, accumulator=lambda x, y: (y[0], reduce(sum, x))):
    for (skip, s), pos in accumulate(zipl(enumerate(lens, skip), [pos]), accumulator):
        reverse_sublist(elems, pos % len(elems), (pos+s) % len(elems))
    return elems, skip+s+pos, skip+1

def solve1(input, n=256):
    return mul(*hash_round([int(l) for l in input.split(',')], list(range(n)))[0][:2])

def solve2(input, n=256, g=16, rounds=64, suffix=[17, 31, 73, 47, 23], pos=0, skip=0):
    elems, lengths = [*range(n)], [ord(c) for c in input.strip()] + suffix
    for _ in range(rounds): elems, pos, skip = hash_round(lengths, elems, pos, skip)
    return bytes(reduce(xor, elems[g*k:g*(k+1)]) for k in range(n//g)).hex()

def inputStrip():
    return 'jxqlasbh'

#matrix = ''.join(''.join('{:04b}'.format(int(x, 16)) for x in solve2('jxqlasbh-' + str(i))) for i in range(128))
#part1 = matrix.count('1')
#print(part1)
#
#part2 = 0
#seen = set()
#matrix = [list(map(int, l.strip())) for l in matrix.strip().split('\n')]
#rng = range(128)
#for i, row in enumerate(matrix):
#    for j, bit in enumerate(row):
#        if bit and (i,j) not in seen:
#            part2 += 1
#            q = [(i,j)]
#            while q:
#                x, y = q.pop()
#                seen.add((x, y))
#                for x2, y2 in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
#                    if x2 in rng and y2 in rng and matrix[x2][y2] and (x2, y2) not in seen:
#                        q.append((x2, y2))
#print(part2)

data = 'jxqlasbh'
rows = []

n = 0
for i in range(128):
    v = solve2('%s-%d' % (data, i))
    v = '{:0128b}'.format(int(v, 16))
    n += sum(map(int, v))
    rows.append(list(map(int, v)))

print(n)

seen = set()
n = 0
def dfs(i, j):
    if ((i, j)) in seen:
        return
    if not rows[i][j]:
        return
    seen.add((i, j))
    if i > 0:
        dfs(i-1, j)
    if j > 0:
        dfs(i, j-1)
    if i < 127:
        dfs(i+1, j)
    if j < 127:
        dfs(i, j+1)

for i in range(128):
    for j in range(128):
        if (i,j) in seen:
            continue
        if not rows[i][j]:
            continue
        n += 1
        dfs(i, j)

print(n)