#!/usr/bin/python3


class CoordinateSpace:
    '''A rudimentary 2d coordinate space class'''

    def __init__(self, data):
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

    def set_data(self, data):
        self.data = [list(row) for row in data]

    def __str__(self):
        return '\n'.join(
            [''.join([str(v) for v in r])
            for r in self.data])

    width = property(get_width)
    height = property(get_height)


# Some useful definitions
__E = (1,0)
__S = (0,1)
__W = (-1,0)
__N = (0,-1)

__CONNS = {
    '|': (__N,__S),
    '-': (__E,__W),
    'L': (__N,__E),
    'J': (__N,__W),
    '7': (__S,__W),
    'F': (__S,__E),
    '.': None,
    'S': None}

def get_start_location(pipe_layout):
    for y in range(pipe_layout.height):
        for x in range(pipe_layout.width):
            if pipe_layout[(x,y)] == 'S':
                return (x,y)
    raise RuntimeError('start location not found')

def get_connections(start_location):
    # hard-coded for my data, in the spirit of,
    # "You've Come a Long Way Baby"
    connections = __S, __E
    return (
        (start_location[0]+connections[0][0],
        start_location[1]+connections[0][1]),
        (start_location[0]+connections[1][0],
        start_location[1]+connections[1][1]))

def update_cursor(pipe_layout, cursor):
    last_location = cursor[0]
    current_location = cursor[1]
    current_pipe = pipe_layout[current_location]
    connections = __CONNS[current_pipe]
    next_location = (
        current_location[0] + connections[0][0],
        current_location[1] + connections[0][1])
    if next_location == last_location:
        next_location = (
            current_location[0] + connections[1][0],
            current_location[1] + connections[1][1])
    return (current_location,next_location)


def part1(input_data):
    pipe_layout = CoordinateSpace(
        ((v for v in line.strip()) for line in input_data))

    start_location = get_start_location(pipe_layout)
    start_connections = get_connections(start_location)

    cursors = [
        ((start_location),(start_connections[0])),
        ((start_location),(start_connections[1]))]
    steps = 1

    while cursors[0][1] != cursors[1][1]:
        cursors[0] = update_cursor(pipe_layout,cursors[0])
        cursors[1] = update_cursor(pipe_layout,cursors[1])
        steps += 1

    return steps


if __name__ == "__main__":
    with open('input') as input_data:
        print(part1(input_data))