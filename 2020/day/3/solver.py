#!/usr/bin/python3
from math import prod
from collections import Counter

if __name__ == "__main__":
    with open("input") as lines:
        print(prod(Counter([1
            for i, l in enumerate(lines)
            if l[3*i%(len(l)-(l[-1]=='\n'))]=='#'
            ]).values()))

    with open('input') as lines:
        print(prod(Counter([j
            for i, l in enumerate(lines)
            for j, s in enumerate(((1,1),(3,1),(5,1),(7,1),(1,2)))
            if i%s[1]==0 and l[s[0]*i//s[1]%(len(l)-(l[-1]=='\n'))]=='#'
            ]).values()))
