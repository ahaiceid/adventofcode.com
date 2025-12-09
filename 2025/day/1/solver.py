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
        for _ in range(v):
            dial += d
            if dial == 0:
                acc += 1
            elif abs(dial) == 100:
                acc += 1
                dial = 0
    return acc

if __name__ == "__main__":
    with open('input') as input_data:
        print(part1(input_data))
    with open ('input') as input_data:
        print(part2(input_data))
