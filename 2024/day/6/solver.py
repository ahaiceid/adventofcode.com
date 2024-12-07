

def turn_right(fwd):
    return (-fwd[1],fwd[0])

def get_next_pos(pos, fwd):
    return (pos[0]+fwd[0],pos[1]+fwd[1])

def test_map_bounds(map, pos):
    if min(pos)<0: raise StopIteration("")
    if pos[0] == len(map): raise StopIteration("")
    if pos[1] == len(map[0]): raise StopIteration("")

def advance(map, pos, fwd, obstruction_count, history):
    map[pos[1]][pos[0]] = 'X'
    while True:
        next_pos = get_next_pos(pos, fwd)
        test_map_bounds(map,next_pos)
        if map[next_pos[1]][next_pos[0]] != "#":
            pos = next_pos
            if history:
                try:
                    if history[0]==history[2] and history[1]<=history[3]:
                        obstruction_count += 1
                except IndexError:
                    pass
                history[0]+=1
            break
        fwd = turn_right(fwd)
        if history:
            history=[0]+history[:3]

    return map, pos, fwd, obstruction_count, history

def part1(input_data):
    map = [[c for c in s.strip()] for s in input_data]
    pos = None
    fwd = (0,-1)
    obstruction_count = 0
    history = [0]
    for y,r in enumerate(map):
        for x,c in enumerate(r):
            if c=='^':
                pos = (x,y)
                break
    import pdb; pdb.set_trace()
    try:
        while True:
            #print('\n'.join([''.join(r) for r in map]),end="\n\n")
            map, pos, fwd, obstruction_count, history = advance(map, pos, fwd, obstruction_count, history)
    except StopIteration:
        pass
    return sum((True for r in map for cell in r if cell=='X')), obstruction_count
    return -1


if __name__=="__main__":
    with open("input") as input_data:
        print(part1(input_data))