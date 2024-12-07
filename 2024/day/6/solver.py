

def turn_right(fwd):
    return (-fwd[1],fwd[0])

def get_next_pos(pos, fwd):
    return (pos[0]+fwd[0],pos[1]+fwd[1])

def test_map_bounds(map, pos):
    if min(pos)<0: raise StopIteration("")
    if pos[0] == len(map): raise StopIteration("")
    if pos[1] == len(map[0]): raise StopIteration("")

def advance(map, pos, fwd):
    map[pos[1]][pos[0]] = 'X'
    while True:
        next_pos = get_next_pos(pos, fwd)
        test_map_bounds(map,next_pos)
        if map[next_pos[1]][next_pos[0]] != "#":
            pos = next_pos
            break
        fwd = turn_right(fwd)

    return map, pos, fwd

def part1(input_data):
    map = [[c for c in s.strip()] for s in input_data]
    pos = None
    fwd = (0,-1)
    for y,r in enumerate(map):
        for x,c in enumerate(r):
            if c=='^':
                pos = (x,y)
                break
    try:
        while True:
            #print('\n'.join([''.join(r) for r in map]),end="\n\n")
            map, pos, fwd = advance(map, pos, fwd)
    except StopIteration:
        pass
    return sum((True for r in map for cell in r if cell=='X'))


if __name__=="__main__":
    with open("input") as input_data:
        print(part1(input_data))