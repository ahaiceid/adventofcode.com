#!/usr/bin/python

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

if __name__=="__main__":
    heightmap = []
    with open("input") as fh:
        heightmap = [[int(c) for c in line.strip()] for line in fh.readlines()]
    heightmap_t = transpose(heightmap)

    low_points = find_lows(heightmap)
    low_points_t = find_lows(heightmap_t)
    low_points = combine(lambda x,y: x*y, low_points, transpose(low_points_t))

    values = combine(lambda x,y: x*y, low_points, heightmap)
    values = combine(lambda x,y: x+y, values, low_points)

    print(sum([sum(v) for v in values]))