from collections.abc import Callable, Iterable
from math import prod


def read_in_chunks(file_handle):
    ''' Lazy function (generator) to read a file in chunks separated by double-newlines. '''
    data = []
    for line in file_handle:
        line = line.strip()
        if line:
            data.append(line)
        else:
            yield data
            data.clear()
    yield data


class MonkeyFactory:

    def construct_monkeys(self, monkey_data_generator: Iterable) -> dict[str:object]:
        monkeys = []
        for monkey_data in monkey_data_generator:
            monkey_index, monkey = self.construct_monkey(monkey_data)
            assert(len(monkeys) == monkey_index)
            monkeys.append(monkey)
        return monkeys

    def construct_monkey(self, monkey_data: Iterable) -> tuple[int,object]:
        monkey_state = dict()
        index = self.decode_index(monkey_data[0])
        monkey_state['items'] = self.decode_items(monkey_data[1])
        monkey_state['operation'] = self.decode_operator(monkey_data[2])
        monkey_state['divisor'] = self.decode_divisor(monkey_data[3])
        monkey_state['target_monkeys'] = (self.decode_target(monkey_data[4]), self.decode_target(monkey_data[5]))
        return index, Monkey(monkey_state)

    def decode_index(self, index_line) -> int:
        return int(index_line.split()[-1].strip(':'))

    def decode_items(self, starting_items_line) -> list[int]:
        return [int(item) for item in starting_items_line.split(': ')[1].split(', ')]

    def decode_operator(self, operation_line) -> Callable:
        *_, operand, value = operation_line.split()
        if value == 'old':
            return lambda x: pow(x,2)
        if operand == '*':
            return lambda x: x * int(value)
        if operand == '+':
            return lambda x: x + int(value)

    def decode_divisor(self, divisor_line) -> int:
        return int(divisor_line.split()[-1])

    def decode_target(self, target_line) -> int:
        return int(target_line.split()[-1])


class Monkey(object):

    def __init__(self, initial_state):
        self.items = list(initial_state['items'])
        self.operation = initial_state['operation']
        self.divisor = initial_state['divisor']
        self.target_monkeys = tuple(initial_state['target_monkeys'])

    def receive_item(self, item: int):
        self.items.append(item)
    
    def take_turn(self, worry_modulation, worry_wrap):
        thrown_items = []
        while True:
            try:
                item = self.items.pop(0)
            except IndexError:
                break
            item = self.operation(item)
            item = item // worry_modulation
            item = item % worry_wrap
            if item % self.divisor == 0:
                thrown_items.append((self.target_monkeys[0], item))
            else:
                thrown_items.append((self.target_monkeys[1], item))
        return thrown_items

def calculate_round(monkeys, inspections, worry_decay, worry_wrap):
    for i, monkey in enumerate(monkeys):
        inspections[i] += len(monkey.items)
        items_to_distribute=monkey.take_turn(worry_decay, worry_wrap)
        for recipient, item in items_to_distribute:
            monkeys[recipient].receive_item(item)


def part1(input_data):
    monkey_factory = MonkeyFactory()
    monkeys = monkey_factory.construct_monkeys(read_in_chunks(input_data))
    divisor_lcm = prod([monkey.divisor for monkey in monkeys])
    inspections = [0 for _ in range(10)]
    for _ in range(20):
        calculate_round(monkeys, inspections, 3, divisor_lcm)
    return prod(sorted(inspections, reverse=True)[0:2])

def part2(input_data):
    monkey_factory = MonkeyFactory()
    monkeys = monkey_factory.construct_monkeys(read_in_chunks(input_data))
    divisor_lcm = prod([monkey.divisor for monkey in monkeys])
    inspections = [0 for _ in range(10)]
    for _ in range(10000):
        calculate_round(monkeys, inspections, 1, divisor_lcm)
    return prod(sorted(inspections, reverse=True)[0:2])

if __name__ == '__main__':
    with open('input', 'r') as data:
        print(part1(data))
    with open('input', 'r') as data:
        print(part2(data))