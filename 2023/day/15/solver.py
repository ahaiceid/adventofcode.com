#!/usr/bin/python3
from collections import OrderedDict
import math

def hash(input):
    v = 0
    for ch in input:
        v += ord(ch)
        v *= 17
        v = v % 256
    return v

def part1(init_sequence):
    accumulator = 0
    for step in init_sequence.strip().split(','):
        accumulator += hash(step)
    return accumulator

def part2(init_sequence):
    lens_array = OrderedDict()
    lenses = dict()
    # setup lenses
    for step in init_sequence.strip().split(','):
        if step[-1] == '-':
            label = step[0:-1]
            box = hash(label)
            try:
                del lens_array[box][label]
                del lenses[label][box]
            except KeyError:
                pass
        else:
            label, value = step.split('=')
            box = hash(label)
            try:
                lens_array[box][label] = int(value)
            except KeyError:
                lens_array[box] = OrderedDict({label: int(value)})
            try:
                lenses[label][box] = None
            except KeyError:
                lenses[label] = OrderedDict({label: box})
    # sum focusing powers
    accumulator = 0
    for lens, boxes in lenses.items():
        box = list(boxes.keys())[0]
        box_hash = hash(box)
        box_factor = 1 + box_hash
        slot_factor = 1 + next(
            # find position of lens in box
            (i for i, x in enumerate(lens_array[box_hash].keys()) if x == lens),
            # if it doesn't exist multiply by zero
            # (the entry will get skipped on the next line anyway)
            -1)
        try:
            focal_length = lens_array[box_hash][lens]
        except KeyError:
            continue
        lens_focusing_power = box_factor * slot_factor * focal_length
        accumulator += lens_focusing_power
    #for box in lens_array.values():
    #    accumulator += math.prod(box.values())
    return accumulator


if __name__ == '__main__':
    with open('input') as input_data:
        print(part1(next(input_data)))
    with open('input') as input_data:
        print(part2(next(input_data)))