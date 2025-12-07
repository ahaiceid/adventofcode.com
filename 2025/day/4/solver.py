


NEIGHBOUR_OFFSETS = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]

def is_within_map_bounds(x,y,map):
    return 0<=min(x,y) and x<len(map[0]) and y<len(map)

def is_available_function(x,y,heat_map):
    return heat_map[y][x]<4

def generate_heat_map(tp_map):
    heat_map = [[0 for _ in range(len(tp_map[0]))] for _ in range(len(tp_map))]
    for y in range(len(tp_map)):
        for x in range(len(tp_map[0])):
            if tp_map[y][x]=='@':
                for offset in NEIGHBOUR_OFFSETS:
                    nx, ny = x+offset[0], y+offset[1]
                    if is_within_map_bounds(nx,ny,tp_map):
                        heat_map[ny][nx] += 1
    return heat_map

def remove_available_positions(tp_map, heat_map):
    new_map = []
    removed_count = 0
    for y in range(len(tp_map)):
        new_row = ''
        for x in range(len(tp_map[0])):
            if tp_map[y][x]=='@' and is_available_function(x,y,heat_map):
                removed_count += 1
                new_row += '.'
            else:
                new_row += tp_map[y][x]
        new_map.append(new_row)
    return new_map, removed_count

def part1(input_data):
    tp_map = [l.strip() for l in input_data]
    heat_map = generate_heat_map(tp_map)
    acc = 0
    for y in range(len(tp_map)):
        for x in range(len(tp_map[0])):
            if tp_map[y][x]=='@' and is_available_function(x,y,heat_map):
                acc += 1
    return acc

def part2(input_data):
    tp_map = [l.strip() for l in input_data]
    heat_map = generate_heat_map(tp_map)
    acc = 0
    tp_map, removed_count = remove_available_positions(tp_map, heat_map)
    while removed_count>0:
        acc += removed_count
        heat_map = generate_heat_map(tp_map)
        tp_map, removed_count = remove_available_positions(tp_map, heat_map)
    return acc


if __name__=="__main__":
    with open('input') as fh:
        print(part1(fh))
    with open('input') as fh:
        print(part2(fh))
