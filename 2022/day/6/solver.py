#!/usr/bin/python3

def detect_marker(buffer, marker_length):
    for i in range(marker_length, len(buffer)):
        if len(set(buffer[i-marker_length:i])) == marker_length:
            return i
    return 0

def part1(buffer):
    return detect_marker(buffer, 4)

def part2(buffer):
    return detect_marker(buffer, 14)

if __name__ == '__main__':
    with open('input', 'r') as input_data:
        print(part1(next(input_data)))
    with open('input', 'r') as input_data:
        print(part2(next(input_data)))
