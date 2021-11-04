#!/usr/bin/python3
import math
import itertools

def find_product(inputs, n):
    return [math.prod(x)
        for x in itertools.product(inputs, repeat=n)
        if sum(x)==2020][0]

if __name__ == "__main__":
    with open('input') as fh:
        content = fh.readlines()
    inputs = [int(x.strip()) for x in content]
    print(find_product(inputs, 2))
    print(find_product(inputs, 3))
