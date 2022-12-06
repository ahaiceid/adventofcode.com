import unittest

import solver

class TestSolver(unittest.TestCase):

    input_data = [
        '    [D]    ',
        '[N] [C]    ',
        '[Z] [M] [P]',
        ' 1   2   3 ',
        '',
        'move 1 from 2 to 1',
        'move 3 from 1 to 3',
        'move 2 from 2 to 1',
        'move 1 from 1 to 2'
        ]

    def test_part1(self):
        self.assertEqual(solver.part1(self.input_data), 'CMZ')

    def test_part2(self):
        self.assertEqual(solver.part2(self.input_data), 'MCD')
