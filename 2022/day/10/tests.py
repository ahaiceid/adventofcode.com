import unittest
import solver

class TestMachine(unittest.TestCase):

    def test_short_program(self):
        short_program = ['noop', 'addx 3', 'addx -5']
        x_values = [1, 1, 1, 4, 4, -1]

        cpu = solver.CPU((line.split() for line in short_program))
        for cycle, x in iter(cpu):
            self.assertEqual(x, x_values[cycle-1])
        self.assertEqual(cpu.x, x_values[-1])

    program = [
        'addx 15', 'addx -11', 'addx 6', 'addx -3', 'addx 5', 'addx -1', 'addx -8', 'addx 13',
        'addx 4', 'noop', 'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx 5',
        'addx -1', 'addx 5', 'addx -1', 'addx -35', 'addx 1', 'addx 24', 'addx -19', 'addx 1',
        'addx 16', 'addx -11', 'noop', 'noop', 'addx 21', 'addx -15', 'noop', 'noop',
        'addx -3', 'addx 9', 'addx 1', 'addx -3', 'addx 8', 'addx 1', 'addx 5', 'noop',
        'noop', 'noop', 'noop', 'noop', 'addx -36', 'noop', 'addx 1', 'addx 7', 'noop',
        'noop', 'noop', 'addx 2', 'addx 6', 'noop', 'noop', 'noop', 'noop', 'noop', 'addx 1',
        'noop', 'noop', 'addx 7', 'addx 1', 'noop', 'addx -13', 'addx 13', 'addx 7', 'noop',
        'addx 1', 'addx -33', 'noop', 'noop', 'noop', 'addx 2', 'noop', 'noop', 'noop',
        'addx 8', 'noop', 'addx -1', 'addx 2', 'addx 1', 'noop', 'addx 17', 'addx -9',
        'addx 1', 'addx 1', 'addx -3', 'addx 11', 'noop', 'noop', 'addx 1', 'noop', 'addx 1',
        'noop', 'noop', 'addx -13', 'addx -19', 'addx 1', 'addx 3', 'addx 26', 'addx -30',
        'addx 12', 'addx -1', 'addx 3', 'addx 1', 'noop', 'noop', 'noop', 'addx -9',
        'addx 18', 'addx 1', 'addx 2', 'noop', 'noop', 'addx 9', 'noop', 'noop', 'noop',
        'addx -1', 'addx 2', 'addx -37', 'addx 1', 'addx 3', 'noop', 'addx 15', 'addx -21',
        'addx 22', 'addx -6', 'addx 1', 'noop', 'addx 2', 'addx 1', 'noop', 'addx -10',
        'noop', 'noop', 'addx 20', 'addx 1', 'addx 2', 'addx 2', 'addx -6', 'addx -11',
        'noop', 'noop', 'noop']

    def test_longer_program(self):
        expected_values = {20: 21, 60: 19, 100: 18, 140: 21, 180: 16, 220: 18}
        for cycle, x in iter(solver.CPU((line.split() for line in self.program))):
            if cycle in expected_values:
                self.assertEqual(x, expected_values[cycle])

    def test_part1(self):
        cpu = solver.CPU((line.split() for line in self.program))
        signal_strength_sum = sum([cycle*x for cycle,x in iter(cpu) if cycle in [20,60,100,140,180,220]])

    def test_part2(self):
        expected_scanlines = ['##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ',
                              '###   ###   ###   ###   ###   ###   ### ',
                              '####    ####    ####    ####    ####    ',
                              '#####     #####     #####     #####     ',
                              '######      ######      ######      ### ',
                              '#######       #######       #######     ',
                              '                                        ']
        self.assertEqual(solver.part2(self.program).split('\n'), expected_scanlines)
