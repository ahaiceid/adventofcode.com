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
        (-2,-1): (-1,-1),
        (-2,0): (-1,0),
        (-2,1): (-1,1),
        (-1,-2): (-1,-1),
        (-1,2): (-1,1),
        (0,-2): (0,-1),
        (0,2): (0,1),
        (1,-2): (1,-1),
        (1,2): (1,1),
        (2,-1): (1,-1),
        (2,0): (1,0),
        (2,1): (1,1),
        # if a delta isn't here do nothing
    }

    def __init__(self, head_position=(0,0), tail_position=(0,0)):
        self.initialize(head_position, tail_position)

    def initialize(self, head_position, tail_position):
        self.head_position = list(head_position)
        self.tail_position = list(tail_position)

    def move_head(self, direction):
        cartesian = self.direction_to_cartesian[direction]
        self.head_position[0] += cartesian[0]
        self.head_position[1] += cartesian[1]

    def calculate_tail_move(self, displacement):
        return self.displacement_to_tail_move.get(displacement,(0,0))

    def update_tail(self):
        displacement = (
            self.head_position[0] - self.tail_position[0],
            self.head_position[1] - self.tail_position[1])
        update = self.calculate_tail_move(displacement)
        #print('{} -> {},'.format(displacement,update))
        self.tail_position[0] += update[0]
        self.tail_position[1] += update[1]

def part1(input_data):
    rope_bridge = RopeBridge()
    visited = set(tuple(rope_bridge.tail_position))
    for move_descriptor in input_data:
        move_direction, move_count = move_descriptor.split()
        for _ in range(int(move_count)):
            rope_bridge.move_head(move_direction)
            rope_bridge.update_tail()
            visited.add(tuple(rope_bridge.tail_position))
            print(len(visited))
    return len(visited)

def part2(input_data):
    pass

if __name__ == '__main__':
    with open('input', 'r') as data:
        print(part1(data))