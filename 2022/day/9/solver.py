#!/bin/python3


class RopeBridge:

    direction_to_cartesian = {
        # map of directions to cartesian coordinates
        'U': (0,1),
        'L': (-1,0),
        'D': (0,-1),
        'R': (1,0)
    }

    displacement_to_tail_move = {
        # map of head displacement to tail move
        (-2,-2): (-1,-1),
        (-2,-1): (-1,-1),
        (-2,0): (-1,0),
        (-2,1): (-1,1),
        (-2,2): (-1,1),
        (-1,-2): (-1,-1),
        (-1,2): (-1,1),
        (0,-2): (0,-1),
        (0,2): (0,1),
        (1,-2): (1,-1),
        (1,2): (1,1),
        (2,-2): (1,-1),
        (2,-1): (1,-1),
        (2,0): (1,0),
        (2,1): (1,1),
        (2,2): (1,1),
        # if a delta isn't here do nothing
    }

    def __init__(self, positions=[(0,0),(0,0)]):
        self.initialize(positions)

    def initialize(self, positions):
        self.positions = [[x,y] for x,y in positions]

    def move_head(self, direction):
        cartesian = self.direction_to_cartesian[direction]
        self.positions[0][0] += cartesian[0]
        self.positions[0][1] += cartesian[1]

    def calculate_tail_move(self, displacement):
        return self.displacement_to_tail_move.get(displacement,(0,0))

    def update_tail(self, tail_index):
        displacement = (
            self.positions[tail_index-1][0] - self.positions[tail_index][0],
            self.positions[tail_index-1][1] - self.positions[tail_index][1])
        update = self.calculate_tail_move(displacement)
        self.positions[tail_index][0] += update[0]
        self.positions[tail_index][1] += update[1]

    def update_tails(self):
        for tail_index in range(1,len(self.positions)):
            self.update_tail(tail_index)

def part1(input_data):
    rope_bridge = RopeBridge()
    visited = set()
    for move_descriptor in input_data:
        move_direction, move_count = move_descriptor.split()
        for _ in range(int(move_count)):
            rope_bridge.move_head(move_direction)
            rope_bridge.update_tails()
            visited.add(tuple(rope_bridge.positions[1]))
    return len(visited)

def part2(input_data):
    rope_bridge = RopeBridge(((0,0),)*10)
    visited = set()
    for move_descriptor in input_data:
        move_direction, move_count =move_descriptor.split()
        for _ in range(int(move_count)):
            rope_bridge.move_head(move_direction)
            rope_bridge.update_tails()
            visited.add(tuple(rope_bridge.positions[9]))
    return len(visited)

if __name__ == '__main__':
    with open('input', 'r') as data:
        print(part1(data))
    with open('input', 'r') as data:
        print(part2(data))
