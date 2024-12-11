
def get_neighbouring_positions(map, pos):
    neighbours = []
    for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
        new_pos = pos[0]+x,pos[1]+y
        if 0<=min(new_pos) and new_pos[1]<len(map) and new_pos[0]<len(map[0]):
            neighbours.append(new_pos)
    return neighbours

def get_accessible_positions(map, pos):
    accessible_neighbours = []
    neighbours = get_neighbouring_positions(map, pos)
    for n in neighbours:
        try:
            if int(map[n[1]][n[0]]) - int(map[pos[1]][pos[0]]) == 1:
                accessible_neighbours.append(n)
        except ValueError:
            pass
    return accessible_neighbours

def count_trails(map, pos):
    trail_count = 0
    trail_destinations = set([])
    if map[pos[1]][pos[0]] == '9':
        return 1, set([pos])
    accessible_positions = get_accessible_positions(map,pos)
    for next_pos in accessible_positions:
        child_trail_count, child_destinations = count_trails(map,next_pos)
        trail_count += child_trail_count
        trail_destinations.update(child_destinations)
    return trail_count, trail_destinations

def part1(input_data):
    trails = []
    ratings = 0
    map = [l.strip() for l in input_data]
    for y,l in enumerate(map):
        for x,c in enumerate(l):
            if c=='0':
                rating, destinations = count_trails(map,(x,y))
                trails.append(((x,y),destinations))
                ratings += rating
    return sum([len(d) for _,d in trails]), ratings

if __name__=="__main__":
    with open('input') as fh:
        print(part1(fh))
