

def get_neighbours(pos):
    return [(pos[0]+n[0],pos[1]+n[1])
            for n in [(0,-1), (1,0), (0,1), (-1,0)]]


def walk_boundary(map, pos):
    directions = {
        (0,-1): [(-1,0),(0,-1),(1,0)],
        (1,0): [(0,-1),(1,0),(0,1)],
        (0,1): [(1,0),(0,1),(-1,0)],
        (-1,0): [(0,1),(-1,0),(0,-1)]}
    
    def __rotate_left(dir):
        return (dir[1],-dir[0])
    
    def __rotate_right(dir):
        return (-dir[1],dir[0])

    def __is_boundary(map, value, pos, dir=None) -> bool:
        def __check_neighbour(n):
            if min(n) <= 0: return True
            if len(map) < n[1]+1: return True
            if len(map[0]) < n[0]+1: return True
            if map[n[1]][n[0]] != value: return True
            return False
        if dir:
            n = (pos[0]+dir[0],pos[1]+dir[1])
            return __check_neighbour(n)
        for n in get_neighbours(pos):
            if __check_neighbour(n):
                return True
        return False

    def __find_boundary(map, value, pos) -> tuple:
        """traverse plots northwards until"""
        if not __is_boundary(map, value, pos, (0,-1)):
            return __find_boundary(map, (pos[0],pos[1]-1))
        return pos, (1,0)
    
    def __walk_boundary(map, value, visited: list, pos: tuple, dir: tuple) -> tuple:
        try:
            if visited[0]==(pos,dir):
                return
        except IndexError:
            pass
        if (__is_boundary(map, value, pos, __rotate_left(dir))):
            # there is a boundary to our left.
            if not __is_boundary(map, value, pos, dir):
                # there isn't a boundary in front of us: walk to next plot
                return __walk_boundary(map, value, visited,
                                       (pos[0]+dir[0],pos[1]+dir[1]), dir)
            else:
                # there is a boundary in front of us: turn to the right
                visited.append((pos,dir))
                return __walk_boundary(map, value, visited, pos, __rotate_right(dir))
        else:
            # there isn't a boundary to our left: turn left and move one plot
            # in that direction.
            visited.append((pos,dir))
            next_dir = __rotate_left(dir)
            return __walk_boundary(map, value, visited,
                                   (pos[0]+next_dir[0],pos[1]+next_dir[1]), next_dir)


    value = map[pos[1]][pos[0]]
    initial_pos, initial_dir = __find_boundary(map, value, pos)
    visited = []
    __walk_boundary(map,value,visited,initial_pos,initial_dir)
    return len(visited)

def flood_area(map, start_position):
    def __flood(map, value, visited: set, pos: tuple) -> tuple:
        """recursively count perimeter, area while populating a visited set"""
        if pos in visited:
            return 0,0
        visited.add(pos)
        neighbour_map = [[n,0,True] for n in get_neighbours(pos)]
        for nm in neighbour_map:
            # accumulate boundary length and mark those neighbours
            if nm[0][0] < 0:
                nm[1] += 1
                nm[2] = False
            if nm[0][1] < 0:
                nm[1] += 1
                nm[2] = False
            if len(map[0]) == nm[0][0]:
                nm[1] += 1
                nm[2] = False
            if len(map) == nm[0][1]:
                nm[1] += 1
                nm[2] = False
            # mark neighbours which have already been visited
            if nm[2] and nm[0] in visited:
                nm[2] = False
            # mark neighbours which don't have the right value
            if nm[2] and map[nm[0][1]][nm[0][0]] != value:
                nm[1] += 1
                nm[2] = False
        boundary_length = sum(nm[1] for nm in neighbour_map)
        area = 1
        for n in [nm[0] for nm in neighbour_map if nm[2]]:
            b, a = __flood(map, value, visited, n)
            boundary_length += b
            area += a
        return boundary_length, area
    visited = set([])
    value = map[start_position[1]][start_position[0]]
    boundary_length, area = __flood(map, value, visited, start_position)
    return visited, boundary_length, area

def generate_map(input_data):
    return [l.strip() for l in input_data]

def part1(input_data):
    map = generate_map(input_data)
    regions = []
    unvisited_plots = set([(a,b) for a in range(len(map[0])) for b in range(len(map))])
    while unvisited_plots:
        plots, boundary_length, area = flood_area(map, unvisited_plots.pop())
        regions.append((boundary_length, area))
        unvisited_plots.difference_update(plots)
    return sum([boundary_length*area for boundary_length, area in regions])


def part2(input_data):
    map = generate_map(input_data)
    regions = []
    unvisited_plots = set([(a,b) for a in range(len(map[0])) for b in range(len(map))])
    while unvisited_plots:
        plots, boundary_length, area = flood_area(map, unvisited_plots.pop())
        regions.append((boundary_length, area, plots))
        unvisited_plots.difference_update(plots)
    price = 0
    for region in regions:
        price += walk_boundary(map, sorted(region[2])[0]) * region[1]
    return price


if __name__=="__main__":
    with open('input') as input_data:
        print(part1(input_data))
    with open('input') as input_data:
        print(part2(input_data))