from collections.abc import Iterable

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

def transpose(data):
    '''Transpose a matrix'''
    return list(map(list,zip(*data)))

def reverse(data):
    return [list(reversed(row)) for row in data]


def mark_vis(tree_grid, vis_grid):
    '''Mark visible trees in working left-right across each row'''
    for row in range(tree_grid.height):
        vis_grid[(0,row)] = 1
        max_height = tree_grid[[0,row]]
        for col in range(1, tree_grid.width):
            this_coord = (col,row)
            if tree_grid[this_coord] > max_height:
                vis_grid[this_coord] = 1
                max_height = tree_grid[this_coord]

def calculate_scenic_score(tree_grid, coord):
    if (coord[0] == 0) or coord[1] == 0 or tree_grid.width == coord[1] + 1 or tree_grid.height == coord[0] + 1:
        return 0
    tree_height = tree_grid[coord]
    up = coord[1]
    for row in range(coord[1] - 1, -1, -1):
        if tree_grid[(coord[0],row)] >= tree_height:
            up = coord[1] - row
            break
    down = 0
    for row in range(coord[1]+1,tree_grid.height):
        down = row - coord[1]
        if tree_grid[(coord[0],row)] >= tree_height:
            break
    left = coord[0]
    for col in range(coord[0] - 1, -1, -1):
        if tree_grid[(col,coord[1])] >= tree_height:
            left = coord[0] - col
            break
    right = 0
    for col in range(coord[0]+1, tree_grid.width):
        right = col - coord[0]
        if tree_grid[(col,coord[1])] >= tree_height:
            break
    return up * down * left * right

def part1(input_data):
    tree_grid = CoordinateSpace([[int(h) for h in line.strip()] for line in input_data])
    vis_grid = CoordinateSpace([[0 for _c in range(tree_grid.width)] for _r in range(tree_grid.height)])

    mark_vis(tree_grid, vis_grid)
    tree_grid.data = reverse(tree_grid.data)
    vis_grid.data = reverse(vis_grid.data)
    mark_vis(tree_grid, vis_grid)
    tree_grid.data = transpose(tree_grid.data)
    vis_grid.data = transpose(vis_grid.data)
    mark_vis(tree_grid, vis_grid)
    tree_grid.data = reverse(tree_grid.data)
    vis_grid.data = reverse(vis_grid.data)
    mark_vis(tree_grid, vis_grid)

    return sum([sum(row) for row in vis_grid.data])

def part2(input_data):
    tree_grid = CoordinateSpace([[int(h) for h in line.strip()] for line in input_data])
    scenic_score_grid = CoordinateSpace([[0 for _c in range(tree_grid.width)] for _r in range(tree_grid.height)])
    for row in range(tree_grid.height):
        for col in range(tree_grid.width):
            scenic_score_grid[(row,col)] = calculate_scenic_score(tree_grid,(row,col))
    return max([max(row) for row in scenic_score_grid.data])

if __name__ == "__main__":
    with open('input', 'r') as input_data:
        print(part1(input_data))
    with open('input', 'r') as input_data:
        print(part2(input_data))
