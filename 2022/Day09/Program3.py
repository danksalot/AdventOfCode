def main():
    with open('Input') as inFile:
    	input_text = [line.strip() for line in inFile.readlines()]
    
    dirs = { 'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1) }
    head_position = (0,0)
    tail_position = (0,0)
    tail_positions = set()
    tail_positions.add(tail_position)
    positions = [(0,0)]*10
    long_tail_positions = set()
    long_tail_positions.add(positions[-1])
    for instruction in input_text:
        data = instruction.split()
        direction = data[0]
        for idx in range(int(data[1])):
            head_position = tuple([sum(tup) for tup in zip(head_position, dirs[direction])])
            tail_position = followKnot(head_position, tail_position)
            tail_positions.add(tail_position)

            positions[0] = tuple([sum(tup) for tup in zip(positions[0], dirs[direction])])
            for idx_p in range(1, len(positions)):
                positions[idx_p] = followKnot(positions[idx_p-1], positions[idx_p])
            long_tail_positions.add(positions[-1])
        #print(positions)
    print(f"Pt1: {len(tail_positions)}")
    print(f"Pt2: {len(long_tail_positions)}")

def update_trailing(leader, follower):
    delta = leader - follower
    #print(f"{leader}-{follower} = {delta}")
    if delta in [2, -2, 2j, -2j]:
        #In line
        follower += (delta/2)
    elif delta.real in [1, -1] and delta.imag in [1, -1]:
        #Diagonally next to each other
        return follower
    elif (delta.real == 0 and delta.imag in [1, -1]):
        return follower
    elif (delta.real in [1, -1] and delta.imag == 0):
        return follower
    elif delta == 0j:
        return follower
    else:
        #Step one diagonally
        delta = int((delta.imag/abs(delta.imag)))*1j + int((delta.real/abs(delta.real)))
        follower += delta
    return follower

def followKnot(a, b):
	if a[0] - b[0] == 2: return (b[0] + 1, a[1])
	elif a[0] - b[0] == -2: return (b[0] - 1, a[1])
	elif a[1] - b[1] == 2: return (a[0], b[1] + 1)
	elif a[1] - b[1] == -2: return (a[0], b[1] - 1)
	else: return b

if __name__ == "__main__":
    main()