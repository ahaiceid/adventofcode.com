#!/usr/bin/python3
from functools import reduce
from itertools import chain

class CoordinateSpace:

    def __init__(self, data):
        self.set_data(data)

    def __getitem__(self, key):
        return self.data[key[1]][key[0]]

    def __setitem__(self, key, value):
        self.data[key[1]][key[0]] = value

    def get_width(self):
        return len(self.data[0])

    def get_height(self):
        return len(self.data)

    def set_data(self, data):
        self.data = [[value for value in row] for row in data]

    def __str__(self):
        return '\n'.join(
            [''.join([str(v) for v in r])
            for r in self.data])

    width = property(get_width)
    height = property(get_height)

def fold_y(data):
    ''' fold in bottom to top '''
    new_data = combine(
        lambda x,y: (x=='#' or y=='#') and '#' or '.',
        data[:len(data)//2],
        reversed(data[len(data)//2+1:]))
    return new_data

def fold_x(data):
    ''' fold right onto left '''
    return transpose(fold_y(transpose(data)))

def combine(func, data1, data2):
    return [[
            reduce(func, val)
            for val in zip(*row)]
        for row in zip(data1,data2)]

def transpose(data):
    return list(map(list,zip(*data)))

def read_coords(file_handle):
    ''' Read coordinates until first double \n '''
    data = []
    while True:
        line = file_handle.readline().strip()
        if line:
            data.append(tuple([int(v) for v in line.split(',')]))
        else:
            break
    return data

def read_folds(file_handle):
    ''' Read folds, from first double \n. '''
    data = []
    while True:
        line = file_handle.readline().strip()
        if line:
            data.append((line.split()[-1].split('=')[0],int(line.split()[-1].split('=')[1])))
        else:
            break
    return data

def main():
    with open("input") as fh:
        coords = read_coords(fh)
        folds = read_folds(fh)
    max_x = max([x[0] for x in coords])+1
    max_y = max([x[1] for x in coords])+1
    space = CoordinateSpace(['.'*max_x]*max_y)
    for coord in coords:
        space[coord] = '#'

    if folds[0][0] == 'x':
        space.set_data(fold_x(space.data))
    else:
        space.set_data(fold_y(space.data))
    print(sum([1 for x in chain(*space.data) if x=='#']))

    for fold in folds[1:]:
        if fold[0] == 'x':
            space.set_data(fold_x(space.data))
        else:
            space.set_data(fold_y(space.data))
    print(space)

if __name__=="__main__":
    main()