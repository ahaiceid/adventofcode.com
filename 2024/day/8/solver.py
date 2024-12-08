import itertools
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

def get_antinodes_locations(antenna_locations):
    antinode_locations = set()
    for antenna_pair in itertools.combinations(antenna_locations,2):
        antinode_locations.update(get_antinodes_for_pair(*antenna_pair))
    return antinode_locations

def part1(input_data):
    map = [l.strip() for l in input_data]
    locations = get_antenna_locations(map)
    per_antenna_locations = get_per_frequency_locations(locations)
    antinodes = set()
    for k,v in per_antenna_locations.items():
        antinodes.update(get_antinodes_locations(v))
    antinodes = set(
        [a for a in antinodes 
         if 0<=min(a) and a[0]<len(map[0])and a[1]<len(map)])
    return len(antinodes)



if __name__=="__main__":
    with open('input') as fh:
        print(part1(fh))