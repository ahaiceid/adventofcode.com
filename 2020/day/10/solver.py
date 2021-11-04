#!/usr/bin/python3

if __name__ == "__main__":
    with open("input") as fh:
        numbers = [int(line) for line in fh]
    sorted_numbers = sorted(numbers)
    one_count = 1
    three_count = 1
    for i in range(len(sorted_numbers)-1):
        difference = sorted_numbers[i+1] - sorted_numbers[i]
        one_count += difference == 1
        three_count += difference == 3
    print("1: {} \n3: {} \n*: {}".format(one_count, three_count, one_count * three_count))

