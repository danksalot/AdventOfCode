def neighbors8(point): 
    "The eight neighbors (with diagonals)."
    x, y = point 
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1))


spiral = [[0] * 101 for x in range(101)]
spiral[50][50] = 1
point = (50,50)
num = 1

def drul(point, x):
    """Down, right, up, left"""
    if x == 0:
        return (point[0] + 1, point[1])
    if x == 1:
        return (point[0], point[1] + 1)
    if x == 2:
        return (point[0] - 1, point[1])
    if x == 3:
        return (point[0], point[1] - 1)

x = 0

while num < 265149:
    v = drul(point, (x+1) % 4)
    if spiral[v[0]][v[1]] == 0:
        x = (x+1) % 4
        point = drul(point,x)
    else:
        point = drul(point,x)
    num = sum([spiral[j][k] for j, k in neighbors8(point)])
    spiral[point[0]][point[1]] = num

print(num)