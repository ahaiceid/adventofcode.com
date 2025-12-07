def part1(inputs):
    dial = 50
    acc = 0
    for input in inputs:
        d = (input[0]=='L') and -1 or 1
        v = int(input[1:])
        dial = (dial + d*v) % 100
        if dial == 0:
            acc += 1
    return acc

def part2(inputs):
    dial = 50
    acc = 0
    for input in inputs:
        d = (input[0]=='L') and -1 or 1
        v = int(input[1:])
        dial1 = dial + d*v
        if 0<dial and dial1<0: acc += 1
        if dial<0 and 0<dial1: acc += 1
        while 100 <= dial1:
            acc += 1
            dial1 -= 100
        while dial1 <= -100:
            acc += 1
            dial1 += 100
        #if dial1 == 0: acc += 1
        dial = dial1
    return acc

if __name__ == "__main__":
    with open('input') as input_data:
        print(part1(input_data))
    with open ('input') as input_data:
        print(part2(input_data))
