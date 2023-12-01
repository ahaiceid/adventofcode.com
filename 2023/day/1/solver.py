#!/usr/bin/python3
import re

def part1(input_data):
    accumulator = 0
    for input_line in input_data:
        for token in input_line:
            try:
                accumulator += 10 * int(token)
                break
            except ValueError:
                pass
        for token in reversed(input_line):
            try:
                accumulator += int(token)
                break
            except ValueError:
                pass
    return accumulator

def part2(input_data):
    accumulator = 0
    digits = {'0': 0, '2': 2, '8': 8, '6': 6, '3': 3, '4': 4, '9': 9, '5': 5, '1': 1, '7': 7, 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    digit_string = [digit[0] for digit in digits.items()]
    digit_pattern = re.compile(r'|'.join(digit_string))
    reverse_pattern = re.compile(r'|'.join(digit_string)[::-1])
    for input_line in input_data:
        accumulator += 10 * digits[digit_pattern.search(input_line).group()]
        accumulator += digits[reverse_pattern.search(input_line[::-1]).group()[::-1]]
    return accumulator

if __name__ == "__main__":
    with open("input") as input_data:
        print(part1(input_data))
    with open("input") as input_data:
        print(part2(input_data))