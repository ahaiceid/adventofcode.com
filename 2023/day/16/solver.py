#!/usr/bin/python3
#from collections.abc import Iterable

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

class Cursor:

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    position = (0,0)
    direction = (1,0)

# Directions
__R = (1,0)
__D = (0,1)
__L = (-1,0)
__U = (0,-1)

__DIRECTIONS = {
    __R: 0,
    __D: 1,
    __L: 2,
    __U: 3}

def energise(contraption, cursor):

    visited = CoordinateSpace((
        list(
            list([0,0,0,0])
            for _ in range(contraption.width))
        for _ in range(contraption.height)))
    cursors = [cursor]

    while cursors:

        for c in cursors:
            # update visited map
            visited[c.position][__DIRECTIONS[c.direction]] = 1

        # update directions
        new_cursors = []
        for c in cursors:
            if contraption[c.position] == '/':
                if c.direction == __R:
                    c.direction = __U
                elif c.direction == __D:
                    c.direction = __L
                elif c.direction == __L:
                    c.direction = __D
                elif c.direction == __U:
                    c.direction = __R
            elif contraption[c.position] == '\\':
                if c.direction == __R:
                    c.direction = __D
                elif c.direction == __D:
                    c.direction = __R
                elif c.direction == __L:
                    c.direction = __U
                elif c.direction == __U:
                    c.direction = __L
            elif contraption[c.position] == '|':
                if c.direction in (__L,__R):
                    c.direction = __U
                    new_cursors.append(Cursor(c.position, __D))
            elif contraption[c.position] == '-':
                if c.direction in (__D,__U):
                    c.direction = __L
                    new_cursors.append(Cursor(c.position, __R))
        cursors = cursors + new_cursors
        
        # update positions
        for c in cursors:
            c.position = (
                c.position[0] + c.direction[0],
                c.position[1] + c.direction[1])

        # cull unnecessary cursors (off the edge or overlayed on an
        # identical previous beam)
        cursors = [
            c
            for c in cursors
            if (
                (-1 < c.position[0])
                and (c.position[0] < contraption.height)
                and (-1 < c.position[1])
                and (c.position[1] < contraption.width)
                and (visited[c.position][__DIRECTIONS[c.direction]]==0)
            )]

    visit_count = len([
        1
        for row in visited.data
        for cell in row
        if any(cell)])
    return visit_count


def part1(input_data):
    contraption = CoordinateSpace(
        ((v for v in line.strip()) for line in input_data))
    return energise(contraption, Cursor((0,0),__R))

def part2(input_data):
    contraption = CoordinateSpace(
        ((v for v in line.strip()) for line in input_data))
    
    # generate all initial cursors
    initial_cursors = []
    initial_cursors += [Cursor((x,0),__D) for x in range(contraption.width)]
    initial_cursors += [Cursor((x,contraption.height-1),__U) for x in range(contraption.width)]
    initial_cursors += [Cursor((0,y),__R) for y in range(contraption.height)]
    initial_cursors += [Cursor((contraption.width-1,y),__L) for y in range(contraption.height)]

    maximum_visits = 0
    for cursor in initial_cursors:
        maximum_visits = max(maximum_visits, energise(contraption,cursor))
    
    return maximum_visits

if __name__ == "__main__":
    with open('input') as input_data:
        print(part1(input_data))
    with open('input') as input_data:
        print(part2(input_data))
