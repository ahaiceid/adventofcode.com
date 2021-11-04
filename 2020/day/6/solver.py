#!/usr/bin/python3
import itertools

def read_in_chunks(file_handle):
    ''' Lazy function (generator) to read a file in chunks separated by double-newlines. '''
    data = []
    for line in file_handle:
        line = line.strip()
        if line:
            data.append(line)
        else:
            yield data
            data.clear()
    yield data

if __name__ == "__main__":
    any_counts = []
    all_counts = []
    with open("input") as fh:
        for chunk in read_in_chunks(fh):
            any_counts.append(len(set(''.join(chunk))))
            all_answers = None
            for answer in chunk:
                try:
                    all_answers &= set(answer)
                except TypeError:
                    all_answers = set(answer)
            all_counts.append(len(all_answers))
    print("any: {}".format(sum(any_counts)))
    print("all: {}".format(sum(all_counts)))
