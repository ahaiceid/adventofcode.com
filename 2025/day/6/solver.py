import functools
import operator


def parse_input(input_data):
    output = []
    for line in input_data:
        tokens = [t for t in line.split()]
        for i, t in enumerate(tokens):
            #import pdb; pdb.set_trace()
            try:
                v = int(t)
                try:
                    output[i][0].append(v)
                except IndexError:
                    output.append([[], None])
                    output[i][0].append(v)
            except ValueError:
                output[i][1] = t
    return output

def calculate_column(column):
    values, op = column
    if op == '*':
        return functools.reduce(operator.mul, values, 1)
    elif op == '+':
        return sum(values)

def part1(input_data):
    column_data = parse_input(input_data)
    total = 0
    for column in column_data:
        total += calculate_column(column)
    return total

def parse_input_2(input_data):
    data = []
    for line in input_data:
        data.append(line.rstrip('\n'))
    return [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]

""" resampled_column_data = [
        ['1', ' ', ' ', '*'],
        ['2', '4', ' ', ' '],
        ['3', '5', '6', ' '],
        [' ', ' ', ' ', ' '],
        ['3', '6', '9', '+'],
        ['2', '4', '8', ' '],
        ['8', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', '3', '2', '*'],
        ['5', '8', '1', ' '],
        ['1', '7', '5', ' '],
        [' ', ' ', ' ', ' '],
        ['6', '2', '3', '+'],
        ['4', '3', '1', ' '],
        [' ', ' ', '4', ' ']]"""
def columnise_data(resampled_data):
    output = [[[], None]]
    for row in reversed(resampled_data):
        if all(x==' ' for x in row):
            output.append([[], None])
        else:
            if row[-1] in ('*', '+'):
                output[-1][1] = row[-1]
            output[-1][0].append(int(''.join(row[:-1])))
    return output

def part2(input_data):
    resampled_data = parse_input_2(input_data)
    column_data = columnise_data(resampled_data)
    total = 0
    for column in column_data:
        total += calculate_column(column)
    return total

if __name__ == "__main__":
    with open('input') as data:
        print(part1(data))
    with open('input') as data:
        print(part2(data))
