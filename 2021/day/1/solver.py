#!/usr/bin/python3
from itertools import starmap

if __name__ == "__main__":
    with open('input') as fh:
        inputs = [int(line.strip()) for line in fh.readlines()]
    
    print(sum(starmap(lambda x,y: 1 if x<y else 0, zip(inputs[:-1],inputs[1:]))))

    windows = [sum(x) for x in zip(inputs[:-2], inputs[1:-1], inputs[2:])]
    print(sum(starmap(lambda x,y: 1 if x<y else 0, zip(windows[:-1],windows[1:]))))