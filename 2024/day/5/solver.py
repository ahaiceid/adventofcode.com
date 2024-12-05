import functools

def parse_ordering_rules(input_data):
    ordering = {}
    for i,rule in enumerate(input_data):
        if not rule.strip():
            break
        k,v=[int(x) for x in rule.strip().split('|')]
        try:
            ordering[k] += [v]
        except KeyError:
            ordering[k] = [v]
    return ordering, i+1

def parse_updates(input_data):
    updates = []
    for update_line in input_data:
        updates += [[int(x) for x in update_line.strip().split(',')]]
    return updates

def validate_update(update, ordering_rules):
    for i in range(len(update)):
        preceding = update[:i]
        for v in preceding:
            try:
                if v in ordering_rules[update[i]]:
                    return False
            except KeyError:
                pass
    return True

def middle_page_number(update):
    return update[len(update)//2]

def part1(input_data):
    ordering_rules, update_index = parse_ordering_rules(input_data)
    updates = parse_updates(input_data[update_index:])
    acc = 0
    for update in updates:
        if validate_update(update, ordering_rules):
            acc += middle_page_number(update)
    return acc

def correct_ordering(update, ordering_rules):
    def number_cmp(n1,n2):
        try:
            if n1 in ordering_rules[n2]:
                return 1
        except KeyError:
            pass
        try:
            if n2 in ordering_rules[n1]:
                return -1
        except KeyError:
            pass
        return 0
    return sorted(update, key=functools.cmp_to_key(number_cmp))

def part2(input_data):
    ordering_rules, update_index = parse_ordering_rules(input_data)
    updates = parse_updates(input_data[update_index:])
    acc = 0
    for update in updates:
        if not validate_update(update, ordering_rules):
            acc += middle_page_number(correct_ordering(update, ordering_rules))
    return acc


if __name__=="__main__":
    with open("input") as fh:
        input_data = []
        for line in fh:
            input_data += [line]
        print(part1(input_data))
        print(part2(input_data))