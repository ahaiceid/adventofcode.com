#!python3
import re

def part1(input_data):
    acc = 0
    data = "".join(input_data)
    token = ["mul(",")"]
    left = data.find(token[0], 0)
    while (left!=-1):
        right = data.find(token[1], left+len(token[0]))
        try:
            n1,n2 = [int(n) for n in data[left+len(token[0]):right].split(",")]
            acc += n1*n2
        except ValueError:
            pass
        left = data.find(token[0], left+len(token[0]))
    return acc

def part2(input_data):
    acc = 0
    cursor = 0
    enabled = True
    expr = r"(?P<mul>mul\((?P<n1>\d+)\,(?P<n2>\d+)\))|(?P<disable>don\'t\(\))|(?P<enable>do\(\))"
    for m in re.finditer(expr, "".join(input_data)):
        d = m.groupdict()
        if enabled and d['mul']:
            acc += int(d['n1'])*int(d['n2'])
        if d['enable']:
            enabled = True
        if d['disable']:
            enabled = False
    return acc

if __name__=="__main__":
    with open("input") as input_data:
        print(part1(input_data))
    with open("input") as input_data:
        print(part2(input_data))
