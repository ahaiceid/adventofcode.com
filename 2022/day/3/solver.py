
import string

item_priorities = {}
item_priorities.update({k:v for k,v in zip(string.ascii_lowercase,range(1,27))})
item_priorities.update({k:v for k,v in zip(string.ascii_uppercase, range(27,53))})


def part1(input_data):
    priority_sum = 0
    for backpack_contents in input_data:
        item_count = len(backpack_contents)
        priority_sum += item_priorities[
            sorted(set.intersection(
                set(backpack_contents[:item_count//2]),
                set(backpack_contents[item_count//2:])))[0]]
    return priority_sum

def in_threes(lines):
    data = []
    for line in lines:
        line = line.strip()
        data.append(line)
        if len(data) == 3:
            yield data
            data.clear()

def part2(input_data):
    priority_sum = 0
    for group in in_threes(input_data):
        priority_sum += item_priorities[sorted(set.intersection(*[set(bp) for bp in group]))[0]]
    return priority_sum

if __name__ == "__main__":
    with open("input") as input_data:
        print(part1(input_data))
    with open("input") as input_data:
        print(part2(input_data))