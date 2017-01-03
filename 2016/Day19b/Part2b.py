from math import log

def part2(n):
    p = 3**int(log(n-1,3))
    return n-p+max(n-2*p,0)

print part2(6)