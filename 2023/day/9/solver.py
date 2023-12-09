#!/usr/bin/python3

def _generate_next_sequence(sequence):
    next_seq = []
    seq_it = iter(sequence)
    try:
        v0 = next(seq_it)
        while True:
            v1 = next(seq_it)
            next_seq.append(v1-v0)
            v0 = v1
    except StopIteration:
        pass
    return next_seq

def _sequencer(input_data, input_generator):
    accumulator = 0
    for history in input_data:
        values = []
        # get first sequence
        values.append(input_generator(history))
        # generate subsequent sequences
        while True:
            values.append(_generate_next_sequence(values[-1]))
            if all(v == 0 for v in values[-1]):
                break
        # extend sequences
        values[-1].append(0)
        for n in range(len(values)-2,-1,-1):
            values[n].append(values[n][-1] + values[n+1][-1])
        # accumulate last value in first sequence
        accumulator += values[0][-1]
    return accumulator

def part1(input_data):
    return _sequencer(
        input_data,
        lambda history: [int(x) for x in history.strip().split()])

def part2(input_data):
    return _sequencer(
        input_data,
        lambda history: [int(x) for x in history.strip().split()][::-1])

if __name__ == "__main__":
    with open('input') as data:
        print(part1(data))
    with open('input') as data:
        print(part2(data))