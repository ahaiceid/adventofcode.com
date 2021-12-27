#!/usr/bin/python3

from pprint import PrettyPrinter
pp = PrettyPrinter()

def generate_next_state(state, insertion_rules):
    next_state = {}
    for k,v in state.items():
        for output in insertion_rules[k]:
            next_state[output] = next_state.get(output,0) + v
    return next_state

def get_sorted_counts(state, last_character):
    counts = {}
    for k,v in state.items():
        for i in [0]:
            counts[k[i]] = counts.get(k[i],0) + v
    counts[last_character] = counts.get(last_character,0) + 1
    return sorted(counts.items(), key=lambda item:item[1])

def main():
    with open("input") as fh:
        state = {}
        initial_state = fh.readline().strip()
        for i in range(len(initial_state)-1):
            polymer_pair = initial_state[i]+initial_state[i+1]
            state[polymer_pair] = state.get(polymer_pair,0) + 1
        last_character = initial_state[-1]
        fh.readline()
        insertion_rules = {}
        for line in fh.readlines():
            line = line.strip().split(' -> ')
            input = line[0]
            outputs = (input[0]+line[1], line[1]+input[1])
            insertion_rules[input] = outputs

    for _ in range(10):
        state = generate_next_state(state, insertion_rules)

    sorted_counts = get_sorted_counts(state, last_character)
    print(sorted_counts[-1][1] - sorted_counts[0][1])

    for _ in range(30):
        state = generate_next_state(state, insertion_rules)

    sorted_counts = get_sorted_counts(state, last_character)
    print(sorted_counts[-1][1] - sorted_counts[0][1])




if __name__=="__main__":
    main()