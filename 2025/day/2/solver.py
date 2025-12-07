from itertools import batched
from math import ceil

def values(start, end):
    n = start
    while n <= end:
        yield n
        n += 1

def is_valid_id_part1(id):
    if len(id)%2 != 0:
        return True
    if id[:len(id)//2]==id[len(id)//2:]:
        return False
    return True

def is_valid_id_part2(id):
    id_length = len(id)
    if id_length==1:
        return True
    for v in range(1, id_length//2+1):
        substrs = set([])
        for s in batched(id,v):
            substrs.add(''.join(s))
        if len(substrs) == 1:
            return False
    return True



def find_invalids(data, validity_func):
    invalids = set([])
    for d in data:
        for v in values(*[int(x) for x in d.split('-')]):
            if not validity_func(str(v)):
                invalids.add(v)
    return invalids

def part1(input_data):
    invalids = find_invalids(input_data, is_valid_id_part1)
    return sum(invalids)

def part2(input_data):
    invalids = find_invalids(input_data, is_valid_id_part2)
    return sum(invalids)

if __name__ == "__main__":
    with open('input') as data:
        line = data.readline()
        print(part1([l for l in line.split(',')]))
        print(part2([l for l in line.split(',')]))
