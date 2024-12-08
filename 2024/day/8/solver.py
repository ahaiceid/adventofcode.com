import itertools
from math import gcd
from string import ascii_letters, digits

ANTENNA_TOKENS = ascii_letters + digits

def get_antenna_locations(map):
    antenna_locations = []
    for y,row in enumerate(map):
        for x,cell in enumerate(row):
            if cell in ANTENNA_TOKENS:
                antenna_locations.append((cell,(x,y)))
    return antenna_locations

def get_per_frequency_locations(antenna_locations):
    frequency_dict = {}
    for frequency,position in antenna_locations:
        try:
            frequency_dict[frequency].append(position)
        except KeyError:
            frequency_dict[frequency] = [position]
    return frequency_dict

def get_antinodes_for_pair(antenna_a,antenna_b):
    d = (antenna_b[0]-antenna_a[0],antenna_b[1]-antenna_a[1])
    return set([(antenna_a[0]-d[0],antenna_a[1]-d[1]),
            (antenna_b[0]+d[0],antenna_b[1]+d[1])])

def get_antinodes_locations(antenna_locations, antinode_fn):
    antinode_locations = set()
    for antenna_pair in itertools.combinations(antenna_locations,2):
        antinode_locations.update(antinode_fn(*antenna_pair))
    return antinode_locations

def is_within_map_bounds(x,y,map):
    return 0<=min(x,y) and x<len(map[0]) and y<len(map)

def part1(input_data):
    map = [l.strip() for l in input_data]
    locations = get_antenna_locations(map)
    per_antenna_locations = get_per_frequency_locations(locations)
    antinodes = set()
    for k,v in per_antenna_locations.items():
        antinodes.update(get_antinodes_locations(v, get_antinodes_for_pair))
    antinodes = set(
        [a for a in antinodes 
         if is_within_map_bounds(*a,map)])
    return len(antinodes)

def get_antinode_line_function(map):
    def fn(antenna_a, antenna_b):
        antinode_locations = set()
        d = (antenna_b[0]-antenna_a[0],antenna_b[1]-antenna_a[1])
        d = (d[0]//gcd(*d),d[1]//gcd(*d))
        location = antenna_a
        while is_within_map_bounds(*location,map):
            antinode_locations.add(location)
            location = (location[0]-d[0],location[1]-d[1])
        location = (antenna_a[0]+d[0],antenna_a[1]+d[1])
        while is_within_map_bounds(*location,map):
            antinode_locations.add(location)
            location = (location[0]+d[0],location[1]+d[1])
        return antinode_locations
    return fn

def part2(input_data):
    map = [l.strip() for l in input_data]
    locations = get_antenna_locations(map)
    per_antenna_locations = get_per_frequency_locations(locations)
    antinodes = set()
    for k,v in per_antenna_locations.items():
        antinodes.update(get_antinodes_locations(v, get_antinode_line_function(map)))
    antinodes = set(
        [a for a in antinodes 
         if is_within_map_bounds(*a,map)])
    return len(antinodes)

if __name__=="__main__":
    with open('input') as fh:
        print(part1(fh))
    with open('input') as fh:
        print(part2(fh))