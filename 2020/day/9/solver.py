#!/usr/bin/python3

import itertools
import sys

if __name__ == "__main__":
    period = 25
    with open("input") as file_handle:
        numbers = [int(line) for line in file_handle]
    number_mapping = {}
    invalid_number = None
    for i in range(period, len(numbers)):
        possible = set([x+y for x, y in itertools.combinations(numbers[i-period:i],2)])
        if numbers[i] not in possible:
            invalid_number = numbers[i]
            break
    print("invalid number: {}".format(invalid_number))
    for i in range(len(numbers)):
        j = i + 2
        while j < len(numbers) and sum(numbers[i:j]) <= invalid_number:
            if sum(numbers[i:j]) == invalid_number:
                print("encryption weakness: {}".format(min(numbers[i:j])+max(numbers[i:j])))
                sys.exit(0)
            j += 1
