#!/usr/bin/python3

from functools import reduce
from itertools import starmap


def transpose(lists):
    return list(map(list,zip(*lists)))

def find_lows(lists):
    return [[v for v in starmap(lambda x,y,z: 1 if x>y and y<z else 0, zip([10]+list[:-1],list,list[1:]+[10]))] for list in lists]

def print_map(grid):
    for row in grid:
        print(''.join([str(x) for x in row]))

def combine(func,*grids):
    return [[reduce(func, val) for val in zip(*row)] for row in zip(*grids)]

def get_neighbours(grid, pos):
    neighbours = []
    if 0 < pos[0]:
        neighbours.append((pos[0]-1,pos[1]))
    if 0 < pos[1]:
        neighbours.append((pos[0],pos[1]-1))
    if pos[0]+1 < len(grid[0]):
        neighbours.append((pos[0]+1,pos[1]))
    if pos[1]+1 < len(grid):
        neighbours.append((pos[0],pos[1]+1))
    return neighbours

def get_height(grid, pos):
    return grid[pos[1]][pos[0]]

def recurse_basin(grid, basin, pos):
    basin[pos[1]][pos[0]] = 1
    height = get_height(grid, pos)
    for neighbour in get_neighbours(grid, pos):
        neighbour_height = get_height(grid, neighbour)
        if height < neighbour_height and neighbour_height < 9:
            recurse_basin(grid, basin, neighbour)

def create_map(size):
    new_map = []
    for _ in range(size[1]):
        new_map.append([0]*size[0])
    return new_map

if __name__=="__main__":
    heightmap = []
    with open("input") as fh:
        heightmap = [[int(c) for c in line.strip()] for line in fh.readlines()]
    heightmap_t = transpose(heightmap)

    low_points_x = find_lows(heightmap)
    low_points_y = find_lows(heightmap_t)
    low_points = combine(lambda x,y: x*y, low_points_x, transpose(low_points_y))

    values = combine(lambda x,y: x*y, low_points, heightmap)
    values = combine(lambda x,y: x+y, values, low_points)
    print(sum([sum(v) for v in values]))

    from pprint import PrettyPrinter; pp = PrettyPrinter()

    basin_areas = []
    for y,row in enumerate(low_points):
        for x,height in enumerate(row):
            if height == 1:
                basin_map = create_map((len(low_points[0]),len(low_points)))
                recurse_basin(heightmap, basin_map, (x,y))
                basin_areas.append(sum([sum(r) for r in basin_map]))

    basin_areas = sorted(basin_areas)
    print(basin_areas[-1]*basin_areas[-2]*basin_areas[-3])
