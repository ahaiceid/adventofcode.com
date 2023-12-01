import unittest
import solver

class TestSolver(unittest.TestCase):

    def test_part1(self):
        sample_data = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
        self.assertEqual(solver.part1(sample_data), 142)

    def test_part2(self):
        sample_data = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']
        self.assertEqual(solver.part2(sample_data), 281)