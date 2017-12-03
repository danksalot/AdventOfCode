NORTH, SOUTH, WEST, EAST = (0, -1), (0, 1), (-1, 0), (1, 0)
turn_right = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}

def spiral_part1(width, height):
    x = width // 2
    y = height // 2
    dx, dy = NORTH
    matrix = [[0] * width for n in range(height)]
    count = 0
    while True:
        count += 1
        if (count == 265149):
        	print "Part 1:", abs(y) + abs(x)
        matrix[y][x] = count

        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] == 0): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go

def spiral_part2(width, height):
    x = width // 2
    y = height // 2
    dx, dy = NORTH
    matrix = [[0] * width for n in range(height)]
    while True:
        value = max(1, sum([matrix[y-1][x-1],matrix[y-1][x],matrix[y-1][x+1],matrix[y][x-1],matrix[y][x+1],matrix[y+1][x-1],matrix[y+1][x],matrix[y+1][x+1]]))
        matrix[y][x] = value
        if (value > 265149):
        	print "Part 2:",value
        	break

        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] == 0): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go

spiral_part1(515, 515)
spiral_part2(515, 515)