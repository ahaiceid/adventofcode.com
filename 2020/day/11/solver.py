#! /usr/bin/python3
import copy

def is_occupied(grid, loc):
    return get_value(grid, loc) == '#'

def get_value(grid, loc):
    if loc[0] < 0 or loc[1] < 0:
        return '.'
    if len(grid) <= loc[1]:
        return '.'
    if len(grid[0]) <= loc[0]:
        return '.'
    return grid[loc[1]][loc[0]]


def offset_loc(loc, offset):
    return (loc[0]+offset[0],loc[1]+offset[1])

def sum_neighbours(input, loc):
    neighbour_offsets = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    neighbour_count = 0
    for offset in neighbour_offsets:
        if is_occupied(input, offset_loc(loc,offset)):
            neighbour_count += 1
    return neighbour_count

def process(input):
    output = []
    for y, row in enumerate(input):
        new_row = ''
        for x, seat in enumerate(row):
            if seat == '.':
                new_row += '.'
                continue
            occupied_neighbour_count = sum_neighbours(input, (x,y))
            if seat == 'L':
                if 0 == occupied_neighbour_count:
                    new_row += '#'
                else:
                    new_row += 'L'
            else:
                if 4 <= occupied_neighbour_count:
                    new_row += 'L'
                else:
                    new_row += '#'
        output += [new_row]
    return output

def sum_visible(input, visible_locs):
    visible_count = 0
    for visible_loc in visible_locs:
        if is_occupied(input, visible_loc):
            visible_count += 1
    return visible_count

def calculate_neighbours(input, loc):
    directions = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    neighbours = []
    x_max = len(input[0])
    y_max = len(input)
    for direction in directions:
        new_loc = loc
        while True:
            new_loc = offset_loc(new_loc, direction)
            if get_value(input, new_loc) != '.':
                neighbours += (new_loc,)
                break
            if (new_loc[0] < 0) or (x_max <= new_loc[0]):
                break
            if (new_loc[1] < 0) or (y_max <= new_loc[1]):
                break
    return neighbours

def calculate_visibility(input):
    output = {}
    for y, row in enumerate(input):
        for x, seat in enumerate(row):
            if seat == '.':
                continue
            output[(x,y)] = calculate_neighbours(input, (x,y))
    return output

def process_vis(input, visibility):
    output = copy.deepcopy(input)
    for loc, visible_locs in visibility.items():
        visible_count = sum_visible(input, visible_locs)
        if is_occupied(input, loc):
            if visible_count >= 5:
                output[loc[1]] = output[loc[1]][:loc[0]] + 'L' + output[loc[1]][loc[0]+1:]
        else:
            if visible_count == 0:
                output[loc[1]] = output[loc[1]][:loc[0]] + '#' + output[loc[1]][loc[0]+1:]
    return output

def load(filename):
    input = []
    with open(filename) as fh:
        for l in fh:
            input += [l.strip()]
    return input

if __name__ == "__main__":
    input = load('input')
    output = process(input)
    while (str(input) != str(output)):
        input = output
        output = process(input)
    print(''.join(output).count('#'))

    input = load('input')
    visibility = calculate_visibility(input)
    output = process_vis(input, visibility)
    while (str(input) != str(output)):
        input = output
        output = process_vis(input, visibility)
    print(''.join(output).count('#'))

    
