from itertools import chain
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import re

def generate_diagonals(word_search):
    size = len(word_search)
    if len(word_search[0].strip())!=size:
        raise RuntimeError(
            "word search not square. ({} high, {} wide).".format(
                size, len(word_search[0].strip())))
    for i in range(size-1,-1,-1):
        line = ""
        for j in range(0,size-i):
            line += word_search[j][j+i]
        yield line
    for j in range(1,size):
        line = ""
        for i in range(0,size-j):
            line += word_search[j+i][i]
        yield line
    for i in range(size-1,-1,-1):
        line = ""
        for j in range(0,size-i):
            line += word_search[size-j-1][j+i]
        yield line
    for j in range(1,size):
        line = ""
        for i in range(0,size-j):
            line += word_search[size-(j+i)-1][i]
        yield line

def generate_verticals(word_search):
    size = len(word_search)
    for i in range(0,size):
        line = ""
        for j in range(0,size):
            line += word_search[j][i]
        yield line

def part1(input_data):
    acc = 0
    patterns = [r'XMAS',r'SAMX']
    for line in chain(input_data, 
                      generate_diagonals(input_data),
                      generate_verticals(input_data)):
        for pattern in patterns:
            acc += len(re.findall(pattern,line))
    return acc

def part2(input_data):
    shape = (3,3)
    view = sliding_window_view(
        np.asarray([[c for c in line.strip()] for line in input_data]), shape)
    acc = 0
    view_list = view.reshape(view.shape[0]*view.shape[1],view.shape[2],view.shape[3])
    for window in view_list:
        if window[1][1]=='A':
            if ((window[0][0]=='M' and window[2][2]=='S') or 
                    (window[0][0]=='S' and window[2][2]=='M')):
                if ((window[2][0]=='M' and window[0][2]=='S') or
                        (window[2][0]=='S' and window[0][2]=='M')):
                    acc += 1
    return acc

if __name__=="__main__":
    with open("input") as fh:
        input_data = []
        for line in fh:
            input_data += [line]
        print(part1(input_data))
        print(part2(input_data))