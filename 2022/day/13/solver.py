
from functools import cmp_to_key
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


def compare(a, b):
    if isinstance(a,int) and isinstance(b,int):
        if a<b: return -1
        if a>b: return 1
        return 0
    if isinstance(a,int):
        a = [a]
    if isinstance(b,int):
        b = [b]
    for first, second in zip_longest(a,b):
        if first is None:
            return -1
        if second is None:
            return 1
        result = compare(first, second)
        if result != 0:
            return result
    return 0


def part1(input_data):
    count = 0
    for i, (a_str, b_str) in enumerate(read_in_chunks(input_data)):
        a = json.loads(a_str)
        b = json.loads(b_str)
        if compare(a,b) < 0:
            count += i+1
    return count

def part2(input_data):
    packets = [json.loads(line) for line in read_ignoring_empty_lines(input_data)]
    packets.extend([[[2]],[[6]]])
    packets.sort(key=cmp_to_key(compare))
    return (packets.index([[2]])+1) * (packets.index([[6]])+1)


if __name__ == '__main__':
    with open('input', 'r') as data:
        print(part1(data))
    with open('input', 'r') as data:
        print(part2(data))