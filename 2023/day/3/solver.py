#/usr/bin/python3

from functools import reduce

__digits = ['{}'.format(x) for x in range(10)]
__neighbour_offsets = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def decode_schematic(input_data):
    schematic = {}
    numbers = []
    symbols = []
    for y, line in enumerate(input_data):
        schematic[y] = {}
        number_in_progress = False
        for x, ch in enumerate(line.strip()):
            if ch == '.':
                number_in_progress = False
            elif ch in __digits:
                if number_in_progress:
                    numbers[-1] = numbers[-1] * 10 + int(ch)
                else:
                    number_in_progress = True
                    numbers.append(int(ch))
                schematic[y][x] = (0, len(numbers)-1)
            else:
                number_in_progress = False
                symbols.append((ch,(x,y)))
                schematic[y][x] = (1, len(symbols)-1)
    return schematic, numbers, symbols

def part1(input_data):
    schematic, numbers, symbols = decode_schematic(input_data)
    part_numbers = set()
    for symbol in symbols:
        symbol, pos = symbol
        for neighbour_offset in __neighbour_offsets:
            try:
                location = schematic[pos[1]+neighbour_offset[1]][pos[0]+neighbour_offset[0]]
                if location[0] == 0:
                    part_numbers.add(location[1])
            except KeyError:
                pass
    return sum([numbers[n] for n in part_numbers])

def part2(input_data):
    schematic, numbers, symbols = decode_schematic(input_data)
    gear_products = []
    for symbol in symbols:
        if symbol[0] == '*':
            gears = set()
            pos = symbol[1]
            for offset in __neighbour_offsets:
                try:
                    location = schematic[pos[1]+offset[1]][pos[0]+offset[0]]
                    if location[0] == 0:
                        gears.add(numbers[location[1]])
                except KeyError:
                    pass
            if len(gears) > 1:
                gear_products.append(reduce(lambda x,y:x*y, [gear for gear in gears]))
    return sum(gear_products)

if __name__=="__main__":
    with open('input') as input_data:
        print(part1(input_data))
    with open('input') as input_data:
        print(part2(input_data))