#!/usr/bin/python3

from itertools import starmap

if __name__ == "__main__":

    '''print(sum([
        1
        for line in open("input").readlines()
        for code in line.split()[-4:]
        if len(code) in [2,3,4,7]
        ]))'''

    '''
    digits = {
        0: [0,1,2,3,4,5],
        1: [1,2],
        2: [0,1,3,4,6],
        3: [0,1,2,3,6],
        4: [1,2,5,6],
        5: [0,2,3,5,6],
        6: [2,3,4,5,6],
        7: [0,1,2],
        8: [0,1,2,3,4,5,6],
        9: [0,1,2,5,6]
    }
    '''

    total = 0
    with open("sampleinput") as fh:
        for line in fh.readlines():
            input_tokens = set([''.join(sorted(x)) for x in line.replace('| ','').split()])
            output_tokens = [''.join(sorted(x)) for x in line.split()[-4:]]
            token_map = {8: 'abcdefg'}
            while not set(output_tokens).issubset(set(token_map.values())):

                if 4 in token_map and 1 in token_map and 9 not in token_map:
                    token_map[9] = ''.join(sorted(set(token_map[1]).union(set(token_map[4]))))
                elif 4 in token_map and 7 in token_map and 9 not in token_map:
                    token_map[9] = ''.join(sorted(set(token_map[1]).union(set(token_map[4]))))
                else:
                    for token in input_tokens:
                        if token in token_map.values():
                            continue
                        token_set = set(token)
                        if len(token) == 2:
                            token_map[1] = token
                        elif len(token) == 3:
                            token_map[7] = token
                        elif len(token) == 4:
                            token_map[4] = token
                        elif len(token) == 5:
                            if 2 in token_map and 3 in token_map:
                                token_map[5] = token
                                continue
                            elif 3 in token_map and 5 in token_map:
                                token_map[2] = token
                                continue
                            elif 5 in token_map and 2 in token_map:
                                token_map[3] = token
                                continue
                            if 1 in token_map:
                                if token_set.issuperset(set(token_map[1])):
                                    token_map[3] = token
                                    continue
                            if 7 in token_map:
                                if token_set.issuperset(set(token_map[7])):
                                    token_map[3] = token
                                    continue
                            if 6 in token_map:
                                if token_set.issubset(set(token_map[6])):
                                    token_map[5] = token
                                    continue
                            if 9 in token_map:
                                if token_set.issubset(set(token_map[9])):
                                    token_map[5] = token
                                    continue
                        elif len(token) == 6:
                            if 0 in token_map and 6 in token_map:
                                token_map[9] = token
                                continue
                            elif 6 in token_map and 9 in token_map:
                                token_map[0] = token
                                continue
                            elif 9 in token_map and 0 in token_map:
                                token_map[6] = token
                                continue
                            if 3 in token_map:
                                if token_set.issuperset(set(token_map[3])):
                                    token_map[9] = token
                                    continue
                            if 1 in token_map:
                                if not token_set.issuperset(set(token_map[1])):
                                    token_map[6] = token
                                    continue
                                elif 5 in token_map:
                                    if token_set.issuperset(set(token_map[5])):
                                        token_map[9] = token
                                        continue
                    #else:
                    #    print(token)
                    #    print(token_map)
            lookup = {v: k for k, v in token_map.items()}
            subtotal = sum(starmap(lambda x,y: x*y, zip([lookup[output_token] for output_token in output_tokens],[1000,100,10,1])))
            #if subtotal == 9361:
            #    import pdb; pdb.set_trace()
            if subtotal < 1000:
                print(output_tokens)
                print(lookup)
            print(subtotal)
            total += subtotal
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