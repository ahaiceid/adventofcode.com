#!/usr/bin/python3


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


def part1(input_data):
    return max([sum([int(val) for val in chunk]) for chunk in read_in_chunks(input_data)])

def part2(input_data):
    return sum(sorted([sum([int(val) for val in chunk]) for chunk in read_in_chunks(input_data)], reverse=True)[:3])

if __name__ == "__main__":
    with open("input") as input_data:
        print(part1(input_data))
    with open("input") as input_data:
        print(part2(input_data))