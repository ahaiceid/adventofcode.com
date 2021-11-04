#!/usr/bin/python3
import string

if __name__ == "__main__":
    valid_count = 0
    required_keys = set(
        ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    digits_set = set(string.digits)
    alphanum_set = set(string.digits + string.ascii_lowercase)
    validation = {
        'byr': lambda s: len(s)==4 and set(s)<=digits_set and 1920<=int(s)<=2002,
        'iyr': lambda s: len(s)==4 and set(s)<=digits_set and 2010<=int(s)<=2020,
        'eyr': lambda s: len(s)==4 and set(s)<=digits_set and 2020<=int(s)<=2030,
        'hgt': lambda s: (s[-2:]=='cm' and 150<=int(s[:-2])<=193) or
                         (s[-2:]=='in' and 59<=int(s[:-2])<=76),
        'hcl': lambda s: len(s)==7 and s[0]=='#' and set(s[1:])<=alphanum_set,
        'ecl': lambda s: s in ['amb','blu','brn','gry','grn','hzl','oth'],
        'pid': lambda s: len(s)==9 and set(s)<=digits_set,
        'cid': lambda s: True,
    }

    with open("input") as input:
        fields = set()
        for line in input:
            line = line.strip()
            if line:
                for pair in line.split(' '):
                    fields.add(pair[:pair.find(':')])
            else:
                valid_count += (required_keys<=fields)
                fields = set()
    print(valid_count)

    valid_count = 0
    with open("input") as input:
        fields = {}
        for line in input:
            line = line.strip()
            if line:
                for pair in line.split(' '):
                    fields[pair[:pair.find(':')]] = pair[pair.find(':')+1:]
            else:
                valid_count += (required_keys<=set(fields.keys())
                                and all([validation[k](v) for k, v in fields.items()]))
                fields = {}
    print(valid_count)
    
