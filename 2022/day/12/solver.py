from collections.abc import Iterable
import itertools
import string

HEIGHT_ENCODING = {k:v for k,v in zip(string.ascii_lowercase, itertools.count(1))}
HEIGHT_ENCODING.update({'S':1,'E':26})

class CoordinateSpace:
    '''A rudimentary 2d coordinate space class'''

    def __init__(self, data: Iterable[Iterable]):
        '''Initialise data member from an iterator of iterators'''
        self.set_data(data)

    def __getitem__(self, key):
        return self.data[key[1]][key[0]]

    def __setitem__(self, key, value):
        self.data[key[1]][key[0]] = value

    def get_width(self) -> int:
        return len(self.data[0])

    def get_height(self) -> int:
        return len(self.data)

    def set_data(self, data: Iterable[Iterable]):
        self.data = [list(row) for row in data]

    def __str__(self):
        return '\n'.join(
            [''.join([str(v) for v in r])
            for r in self.data])

    width = property(get_width)
    height = property(get_height)


class Graph():
    class Node():
        def __init__(self, coordinates, height, destinations):
            self.coordinates = tuple(coordinates)
            self.height = height
            self.neighbours = list(destinations)

    def __init__(self):
        self.nodes = None
        self.start_node = None
        self.end_node = None

    def create_node(self, height_grid, node_coord):
        # define some directions:
        up = (0,-1)     #(flipped)
        down = (0,1)
        left = (-1,0)
        right = (1,0)
        position_value = height_grid[node_coord]
        node_height = HEIGHT_ENCODING[position_value]
        destinations = []
        for direction in [up,left,down,right]:
            adjacent_coord = (node_coord[0]+direction[0],node_coord[1]+direction[1])
            if adjacent_coord[0] < 0 or height_grid.width <= adjacent_coord[0]:
                continue
            if adjacent_coord[1] < 0 or height_grid.height <= adjacent_coord[1]:
                continue
            adjacent_height = HEIGHT_ENCODING[height_grid[adjacent_coord]]
            if 1 < adjacent_height - node_height:
                continue
            destinations.append(adjacent_coord)
        if position_value == 'S':
            assert(self.start_node == None)
            self.start_node = node_coord
        if position_value == 'E':
            assert(self.end_node == None)
            self.end_node = node_coord
        return self.Node(node_coord, node_height, destinations)

    def traverse(self, start_node=None):
        visited_nodes = set()
        frontier = {start_node or self.start_node}
        steps = 0
        while True:
            next_frontier = set()
            for selected_node in frontier:
                if not selected_node in visited_nodes:
                    visited_nodes.add(selected_node)
                else:
                    continue
                if selected_node == self.end_node:
                    return steps
                next_frontier.update(self.nodes[selected_node].neighbours)
            if not next_frontier:
                raise RuntimeError('Failed to find path to end node.')
            steps += 1
            frontier = next_frontier

def part1(input_data):
    height_grid = CoordinateSpace([[h for h in line.strip()] for line in input_data])
    graph = Graph()
    graph.nodes = CoordinateSpace([[graph.create_node(height_grid,(x,y)) for x in range(height_grid.width)] for y in range(height_grid.height)])
    return graph.traverse()

def part2(input_data):
    height_grid = CoordinateSpace([[h for h in line.strip()] for line in input_data])
    graph = Graph()
    graph.nodes = CoordinateSpace([[graph.create_node(height_grid,(x,y)) for x in range(height_grid.width)] for y in range(height_grid.height)])
    starting_positions = []
    for x in range(height_grid.width):
        for y in range(height_grid.height):
            if height_grid[(x,y)] in ['a','S']:
                starting_positions.append((x,y))
    path_lengths = []
    for starting_position in starting_positions:
        try:
            path_lengths.append(graph.traverse(starting_position))
        except RuntimeError:
            pass
    return min(path_lengths)


if __name__ == "__main__":
    with open('input', 'r') as data:
        print(part1(data))
    with open('input', 'r') as data:
        print(part2(data))
