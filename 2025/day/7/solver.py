

def get_start_position(grid):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 'S':
                return (r, c)
    return None

def get_next_positions(grid, current_positions):
    next_positions = set()
    splits = 0
    for position in current_positions:
        r, c = position
        r += 1
        if grid[r][c] == '^':
            splits += 1
            next_positions.add((r, c - 1))
            next_positions.add((r, c + 1))
        else:
            next_positions.add((r, c))
    return next_positions, splits

def part1(data):
    grid = [l.strip() for l in data]
    start_pos = get_start_position(grid)
    positions = {start_pos}
    acc = 0
    for _ in range(len(grid)-start_pos[0]-1):
        positions, splits = get_next_positions(grid, positions)
        acc += splits
    return acc

def get_quantum_positions(grid, current_positions):
    next_positions = dict()
    for position, count in current_positions:
        r, c = position
        r += 1
        if grid[r][c] == '^':
            try:
                next_positions[(r, c-1)] += count
            except KeyError:
                next_positions[(r, c-1)] = count
            try:
                next_positions[(r, c+1)] += count
            except KeyError:
                next_positions[(r, c+1)] = count
        else:
            try:
                next_positions[(r, c)] += count
            except KeyError:
                next_positions[(r, c)] = count
    return next_positions

def part2(data):
    grid = [l.strip() for l in data]
    start_pos = get_start_position(grid)
    positions = {start_pos: 1}
    for i in range(len(grid)-start_pos[0]-1):
        positions = get_quantum_positions(grid, positions.items())
    return sum(positions.values())

if __name__ == "__main__":
    with open("input") as fh:
        print(part1(fh))
    with open("input") as fh:
        print(part2(fh))
