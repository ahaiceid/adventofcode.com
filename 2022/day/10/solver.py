



class CPU:

    def __init__(self, instruction_source):
        self.x = 1
        self.cycle_count = 0
        self.instruction_source = instruction_source
        self.current_instruction = None

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.is_instruction_complete():
                self.fetch_instruction()
            self.cycle_count += 1
            self.current_instruction[0] += 1
            last_x = self.x
            if self.is_instruction_complete():
                self.apply_instruction()
            return self.cycle_count, last_x

    def fetch_instruction(self):
        self.current_instruction = [0, *next(self.instruction_source)]
        
    def is_instruction_complete(self):
        return (self.current_instruction == None or
                (self.current_instruction[1] == 'noop' and 1 <= self.current_instruction[0]) or
                (self.current_instruction[1] == 'addx' and 2 <= self.current_instruction[0]))

    def apply_instruction(self):
        if self.current_instruction == None:
            return
        if self.current_instruction[1] == 'noop':
            return
        if self.current_instruction[1] == 'addx':
            self.x += int(self.current_instruction[2])


def part1(data):
    cpu = CPU((line.split() for line in data))
    return sum([cycle*x for cycle,x in iter(cpu) if cycle in [20,60,100,140,180,220]])

def part2(data):
    print('')
    cpu = CPU((line.split() for line in data))
    scanlines = [[' '] * 40]
    for cycle, x in iter(cpu):
        if cycle % 40 == 0:
            #print(''.join(scanlines))
            scanlines.append([' '] * 40)
        if cycle%40 in range(x,x+3):
            scanlines[cycle//40][(cycle%40)-1] = '#'
    return '\n'.join([''.join(scanline) for scanline in scanlines])


if __name__ == '__main__':
    with open('input', 'r') as input_data:
        print(part1(input_data))
    with open('input', 'r') as input_data:
        print(part2(input_data))
