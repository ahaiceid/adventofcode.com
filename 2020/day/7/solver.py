#!/usr/bin/python3

def recurse_reverse(reverse_bag_mapping, bag):
    bag_set = set()
    try:
        for _bag in reverse_bag_mapping[bag]:
            bag_set |= set([_bag])
            bag_set |= recurse_reverse(reverse_bag_mapping, _bag)
    except KeyError:
        pass
    return bag_set

def recurse_forward(bag_mapping, bag):
    total = 1
    for _bag, count in bag_mapping[bag]:
        total += recurse_forward(bag_mapping, _bag) * count
    return total

def process_bags(line):
    _, _, _, _, *data = line.split()
    try:
        while data:
            n, a, b, _, *data = data
            yield int(n), a+' '+b
    except ValueError:
        pass

if __name__ == "__main__":
    bag_mapping = {}
    with open("input") as fh:
        for line in fh:
            tokens = line.split()
            bag = ' '.join(tokens[:2])
            bag_mapping[bag] = []
            for count, _bag in process_bags(line):
                bag_mapping[bag] += [(_bag, count),]
    reverse_bag_mapping = {}
    for k, v_list in bag_mapping.items():
        for v, _ in v_list:
            if not v in reverse_bag_mapping:
                reverse_bag_mapping[v] = [k]
            else:
                reverse_bag_mapping[v] += [k]
    possible_bags = recurse_reverse(reverse_bag_mapping, 'shiny gold')
    print("possible bags: {}".format(len(possible_bags)))
    total_bags = recurse_forward(bag_mapping, 'shiny gold') - 1
    print("total bags: {}".format(total_bags))
