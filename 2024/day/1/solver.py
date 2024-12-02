#!python3
import collections

def part1(input_data):
    data = [line.split() for line in input_data]
    list1 = sorted([int(d[0]) for d in data])
    list2 = sorted([int(d[1]) for d in data])
    acc = 0
    for i in range(len(list1)):
        acc += abs(list2[i] - list1[i])
    return acc

def part2(input_data):
    data = [line.split() for line in input_data]
    list1 = [int(d[0]) for d in data]
    counter = collections.Counter([int(d[1]) for d in data])
    acc = 0
    for n in list1:
        acc += n*counter[n]
    return acc

if __name__ == "__main__":
    with open("input") as input_data:
        print(part1(input_data))
    with open("input") as input_data:
        print(part2(input_data))

