
from functools import reduce
from itertools import zip_longest
import json

def read_in_chunks(file_handle):
    ''' Lazy function (generator) to read a file in chunks separated by double-newlines. '''
    data = []
    for line in file_handle:
        line = line.strip()
        if line:
            data.append(line)
        else:
            yield data
            data.clear()
    yield data

def read_ignoring_empty_lines(file_handle):
    ''' Lazy function to read a file, ignoring empty lines. '''
    for line in file_handle:
        line = line.strip()
        if line:
            yield line


def is_less_than(a, b):
    if isinstance(a,int) and isinstance(b,int):
        if a<b: return True
        if a>b: return False
        return None
    if isinstance(a,int):
        a = [a]
    if isinstance(b,int):
        b = [b]
    for first, second in zip_longest(a,b):
        if first is None:
            return True
        if second is None:
            return False
        result = is_less_than(first, second)
        if result in [True,False]:
            return result
    return None


def part1(input_data):
    count = 0
    for i, (a_str, b_str) in enumerate(read_in_chunks(input_data)):
        a = json.loads(a_str)
        b = json.loads(b_str)
        if is_less_than(a,b):
            count += i+1
    return count

def part2(input_data):
    packets = [json.loads(line) for line in read_ignoring_empty_lines(input_data)]
    packets.append([[2]])
    packets.append([[6]])
    import pdb; pdb.set_trace()
    packets.sort(cmp=is_less_than)


if __name__ == '__main__':
    with open('input', 'r') as data:
        print(part1(data))
    with open('input', 'r') as data:
        print(part2(data))