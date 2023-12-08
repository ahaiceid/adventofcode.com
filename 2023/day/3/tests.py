#/usr/bin/python3

import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..']


    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 4361)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 467835)