

def construct_ranges(data):
    tokens = dict()
    for d in data:
        first, last = map(int, d.split('-'))
        try:
            tokens[first] += 1
        except KeyError:
            tokens[first] = 1
        try:
            tokens[last + 1] -= 1
        except KeyError:
            tokens[last + 1] = -1
    sorted_keys = sorted(tokens.keys())
    start = sorted_keys[0]
    current_heat = 0
    output_kv = dict()
    for key in sorted_keys:
        if tokens[key] > 0:
            if current_heat == 0:
                start = key
            current_heat += tokens[key]
        elif tokens[key] < 0:
            current_heat += tokens[key]
            if current_heat == 0:
                output_kv[start] = key
    return output_kv

def check_ingredient(ranges, ingredient_id):
    for start, end in ranges.items():
        if start <= ingredient_id < end:
            return True
    return False

def part1(data):
    range_input = []
    line = data.readline()
    line = line.strip()
    while line != '':
        range_input.append(line)
        line = data.readline()
        line = line.strip()
    ranges = construct_ranges(range_input)
    acc = 0
    for line in data:
        ingredient_id = int(line.strip())
        if check_ingredient(ranges, ingredient_id):
            acc += 1
    fresh_total = 0
    for k,v in ranges.items():
        fresh_total += v - k
    return acc, fresh_total

if __name__=='__main__':
    with open('input') as fh:
        print('{}\n{}'.format(*part1(fh)))