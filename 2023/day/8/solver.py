#!/usr/bin/python3

import itertools

__tr = str.maketrans({
    'L':'0',
    'R':'1',
})

def gcd(n):
    assert(type(n)==list)
    if len(n) == 2:
        a = max(n)
        b = min(n)
        while b != 0:
            t = b
            b = a % b
            a = t
        return a
    else:
        return gcd(n[:-2]+[gcn(n[-2:])])

def lcm(n):
    assert(type(n)==list)
    if len(n) == 2:
        assert(n[0]*n[1]/gcd(n) - n[0]*n[1]//gcd(n) < 0.01)
        return n[0]*n[1]//gcd(n)
    else:
        return lcm(n[:-2]+[lcm(n[-2:])])

def read_directions(input_iter):
    directions = [
        int(x) for x in next(input_iter).strip().translate(__tr)]
    next(input_iter)
    return directions

def read_network(input_iter):
    network = {}
    for node in input_iter:
        node, left_right = node.strip().split(' = ')
        left, right = left_right.strip('()').split(', ')
        network[node] = (left, right)
    return network

def part1(input_data):
    directions = read_directions(input_data)
    network = read_network(input_data)
    current_node = 'AAA'
    steps = 0
    for direction in itertools.cycle(directions):
        current_node = network[current_node][direction]
        steps += 1
        if current_node == 'ZZZ':
            return steps

def part2(input_data):
    directions = read_directions(input_data)
    network = read_network(input_data)
    starting_nodes = [key for key in network.keys() if key[-1]=='A']
    step_counts = []
    for node in starting_nodes:
        steps = 0
        for direction in itertools.cycle(directions):
            node = network[node][direction]
            steps += 1
            if node[-1] == 'Z':
                break
        step_counts.append(steps)
    return lcm(step_counts)


if __name__=="__main__":
    with open('input') as input_data:
        print(part1(input_data))
    with open('input') as input_data:
        print(part2(input_data))