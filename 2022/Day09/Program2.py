ds = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}

def simulate_head(moves):
    positions = [(0, 0)]
    for move in moves:
        di, n = move.split()
        dx, dy = ds[di]
        for _ in range(int(n)):
            positions.append((positions[-1][0] + dx, positions[-1][1] + dy))
    
    return positions

def follow_head(positions):
    followed_positions = [(0, 0)]
    kx, ky = 0, 0
    for px, py in positions:
        if abs(px - kx) > 1 or abs(py - ky) > 1:
            kx = kx + ((px > kx) - (kx > px))
            ky = ky + ((py > ky) - (ky > py))
        followed_positions.append((kx, ky))
        
    return followed_positions

with open('Input') as inFile:
	h0 = simulate_head(inFile.read().splitlines())
for _ in range(9):
    # print(h0)
    h0 = follow_head(h0)
    
print(set(h0))
print(len(set(h0)))