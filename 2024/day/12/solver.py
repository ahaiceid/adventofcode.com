

def get_neighbours(pos):
    return [(pos[0]+n[0],pos[1]+n[1])
            for n in [(0,-1), (1,0), (0,1), (-1,0)]]



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


if __name__=="__main__":
    with open('input') as input_data:
        print(part1(input_data))