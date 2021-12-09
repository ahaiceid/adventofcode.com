#!/usr/bin/python3

from itertools import starmap


if __name__ == "__main__":

    print(sum([
        1
        for line in open("input").readlines()
        for code in line.split()[-4:]
        if len(code) in [2,3,4,7]
        ]))

    with open("input") as fh:
        total = 0
        for line in fh.readlines():
            input_tokens = set([''.join(sorted(x)) for x in line.replace('| ','').split()])
            output_tokens = [''.join(sorted(x)) for x in line.split()[-4:]]

            mapping = {8:"abcdefg"}
            five_segments = set()
            six_segments = set()
            for token in list(input_tokens):
                if len(token) == 2:
                    mapping[1] = token
                elif len(token) == 3:
                    mapping[7] = token
                elif len(token) == 4:
                    mapping[4] = token
                elif len(token) == 5:
                    five_segments.add(token)
                elif len(token) == 6:
                    six_segments.add(token)

            # find 3
            for token in five_segments:
                if len(set(mapping[7]).intersection(set(token))) == 3:
                    mapping[3] = token
                    five_segments.remove(token)
                    break
            
            # find 5
            for token in five_segments:
                if len(set(mapping[4]).intersection(set(token))) == 3:
                    mapping[5] = token
                    five_segments.remove(token)
                    break

            # only 2 remains
            mapping[2] = five_segments.pop()

            # find 9
            for token in six_segments:
                if len(set(mapping[3]).intersection(set(token))) == 5:
                    mapping[9] = token
                    six_segments.remove(token)
                    break
            
            # find 0
            for token in six_segments:
                if len(set(mapping[7]).intersection(set(token))) == 3:
                    mapping[0] = token
                    six_segments.remove(token)
                    break

            # only 6 remains
            mapping[6] = six_segments.pop()

            lookup = {v: k for k, v in mapping.items()}
            total += sum(starmap(lambda x,y: x*y, zip([lookup[output_token] for output_token in output_tokens],[1000,100,10,1])))

        print(total)



'''{
    8: 'abcdefg',
    7: 'dfg',
    4: 'cefg',
    3: 'bcdfg',
    1: 'fg',
    9: 'bcdefg',
    0: 'abdefg',
    6: 'abcdef'}'''