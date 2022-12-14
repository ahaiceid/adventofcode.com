from collections.abc import Iterable
from functools import reduce


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


def yield_pairs(data):
    first = next(data)
    for second in data:
        yield first, second
        first = second

def rasterise_rock(coordinate_space, vertex_lists):
    for vertex_list in vertex_lists:
        for u,v in yield_pairs(iter(vertex_list)):
            if u[0]==v[0]:
                # points are in same column
                rock_pixels = [(u[0],p) for p in range(u[1],v[1], (v[1]-u[1])//abs(v[1]-u[1]))] + [v]
            else:
                rock_pixels = [(p,u[1]) for p in range(u[0],v[0], (v[0]-u[0])//abs(v[0]-u[0]))] + [v]
            for rock_pixel in rock_pixels:
                coordinate_space[rock_pixel] = '#'

def decode_vertex_lists(input_data, offset=0):
    x_max = 0
    y_max = 0
    vertex_lists = []
    for line in input_data:
        line_vertices = list(map(
            lambda x:(x[0]+offset,x[1]),
            [[int(v) for v in word.split(',')] for word in line.split(' -> ')]))
        line_x_max, line_y_max = reduce(lambda x,y: (max(x[0],y[0]),max(x[1],y[1])), line_vertices)
        vertex_lists.append(line_vertices)
        x_max = max(x_max,line_x_max)
        y_max = max(y_max,line_y_max)
    return x_max, y_max, vertex_lists

def drop_sand(space, position=(500,0)):
    down = (position[0],position[1]+1)
    if down[1] == space.height:
        return None
    if space[down] == ' ':
        return drop_sand(space, down)
    down_left = (down[0]-1,down[1])
    if down_left[0] < 0:
        return None
    if space[down_left] == ' ':
        return drop_sand(space, down_left)
    down_right = (down[0]+1,down[1])
    if down_right[0] == space.width:
        return None
    if space[down_right] == ' ':
        return drop_sand(space, down_right)
    return position
    

def part1(input_data):
    x_max, y_max, vertex_lists = decode_vertex_lists(input_data)
    space = CoordinateSpace([[' ' for x in range(x_max + 1)] for y in range(y_max + 1)])
    rasterise_rock(space, vertex_lists)
    count = 0
    while True:
        try:
            space[drop_sand(space)] = 'o'
        except TypeError:
            break
        count += 1
    return count
    

def part2(input_data, offset=5):
    x_max, y_max, vertex_lists = decode_vertex_lists(input_data, offset)
    space = CoordinateSpace([[' ' for _ in range(x_max + offset + y_max)] for _ in range(y_max + 2)] + [['#' for _ in range(x_max + offset + y_max)]])
    rasterise_rock(space, vertex_lists)
    count = 0
    while True:
        start_position = (500+offset,0)
        end_position = drop_sand(space,start_position)
        space[end_position] = 'o'
        count += 1
        if start_position == end_position:
            return count
    return count

if __name__ == '__main__':
    with open('input', 'r') as data:
        print(part1(data))
    with open('input', 'r') as data:
        print(part2(data))