#!/usr/bin/python3

def validate_policy_1(data):
    _min, _max, _ch, _str = data
    occ = _str.count(_ch)
    return _min <= occ and occ <= _max

def validate_policy_2(data):
    _first, _second, _ch, _str = data
    return (_str[_first-1] == _ch) != (_str[_second-1] == _ch)

if __name__ == "__main__":
    inputs = []
    with open('input') as fh:
        for l in fh:
            tokens = l.split(' ')
            _min, _max = tokens[0].split('-')
            _ch = tokens[1][0]
            _str = tokens[2]
            inputs.append([int(_min), int(_max), _ch, _str])
    valid_one = 0
    valid_two = 0
    for input in inputs:
        if validate_policy_1(input):
            valid_one += 1
        if validate_policy_2(input):
            valid_two += 1
    print('Policy One Total: ' + str(valid_one))
    print('Policy Two Total: ' + str(valid_two))