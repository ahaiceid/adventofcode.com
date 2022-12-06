from collections.abc import Iterable


def initialize_stacks(data: Iterable[str]) -> list:
    stack_count = int(data[0].strip().split(' ')[-1])
    stacks = [[] for _ in range(stack_count)]
    for layer in data[1:]:
        for stack_index in range(stack_count):
            crate = layer[(stack_index*4)+1]
            if crate != ' ':
                stacks[stack_index].append(crate)
    return stacks

def input_parser(input_data: Iterable[str]) -> list:
    initialized = False
    buffer = []
    for line in input_data:
        line = line.strip('\n')
        if not initialized:
            if line:
                buffer.insert(0, line)
            else:
                initialized = True
                yield initialize_stacks(buffer)
        else:
            yield line

def part1(input_data: Iterable[str]) -> str:
    commands = input_parser(input_data)
    stacks = next(commands)
    for command in commands:
        command = command.split()
        move_count = int(command[1])
        from_stack = int(command[3]) - 1
        to_stack = int(command[5]) - 1
        for _ in range(move_count):
            stacks[to_stack].append(stacks[from_stack].pop())
    return ''.join([stack[-1] for stack in stacks])

def part2(input_data: Iterable[str]) -> str:
    commands = input_parser(input_data)
    stacks = next(commands)
    for command in commands:
        command = command.split()
        move_count = int(command[1])
        from_stack = int(command[3]) - 1
        to_stack = int(command[5]) - 1
        stacks[to_stack] += stacks[from_stack][-move_count:]
        stacks[from_stack] = stacks[from_stack][:-move_count]
    return ''.join([stack[-1] for stack in stacks if stack])

if __name__ == "__main__":
    with open('input', 'r') as input_data:
        print(part1(input_data))
    with open('input', 'r') as input_data:
        print(part2(input_data))
