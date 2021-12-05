#!/usr/bin/python3

import itertools

def get_inputs():
    inputs = []
    max_x = 0
    max_y = 0
    with open("input") as fh:
        for line in fh.readlines():
            coords = line.strip().split(" -> ")
            x1,y1 = [int(s) for s in coords[0].split(',')]
            x2,y2 = [int(s) for s in coords[1].split(',')]
            max_x = max(max_x,max(x1,x2))
            max_y = max(max_y,max(y1,y2))
            inputs.append(((x1,y1),(x2,y2)))
    return inputs, (max_x+1,max_y+1)

def create_map(bounds):
    vent_map = []
    for y in range(bounds[1]):
        vent_map.append(['.' for x in range(bounds[0])])
    return vent_map

def rasterize(input, horizontals):
    x1,y1 = input[0]
    x2,y2 = input[1]
    if x1==x2:
        return [p for p in zip(itertools.repeat(x1),range(min(y1,y2),max(y1,y2)+1))]
    elif y1==y2:
        return [p for p in zip(range(min(x1,x2),max(x1,x2)+1),itertools.repeat(y1))]
    elif horizontals:
        # diagonal...
        x_inc = x1<x2 and 1 or -1
        y_inc = y1<y2 and 1 or -1
        return [p for p in zip(range(x1,x2+x_inc,x_inc),range(y1,y2+y_inc,y_inc))]
    return []

def rasterize_all(inputs, horizontals):
    points = []
    for input in inputs:
        points += rasterize(input, horizontals)
    return points

def plot(vent_map, point):
    try:
        vent_map[point[1]][point[0]] += 1
    except TypeError:
        vent_map[point[1]][point[0]] = 1

def part1():
    inputs, bounds = get_inputs()
    vent_map = create_map(bounds)
    points = rasterize_all(inputs,False)
    for point in points:
        plot(vent_map, point)
    print(len([1 for pos in itertools.chain(*vent_map) if type(pos)==int and 2<=pos]))

def part2():
    inputs, bounds = get_inputs()
    vent_map = create_map(bounds)
    points = rasterize_all(inputs,True)
    for point in points:
        plot(vent_map, point)
    print(len([1 for pos in itertools.chain(*vent_map) if type(pos)==int and 2<=pos]))

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()