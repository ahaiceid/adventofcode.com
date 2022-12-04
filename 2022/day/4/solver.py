from collections.abc import Iterable

def part1(input_data: Iterable[str]) -> int:
    count = 0
    for pair in input_data:
        a, b = [[int(num) for num in elf.split('-')] for elf in pair.split(',')]
        if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
            count += 1
    return count

def part2(input_data: Iterable[str]) -> int:
    count = 0
    for pair in input_data:
        a, b = [[int(num) for num in elf.split('-')] for elf in pair.split(',')]
        range_a = range(a[0],a[1]+1)
        range_b = range(b[0],b[1]+1)
        if a[0] in range_b or a[1] in range_b or b[0] in range_a or b[1] in range_a:
            count += 1
    return count

if __name__ == "__main__":
    with open("input") as input_data:
        print(part1(input_data))

    with open("input") as input_data:
        print(part2(input_data))