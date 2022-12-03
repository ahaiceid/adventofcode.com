import unittest
import solver

class TestSolver(unittest.TestCase):
    sample_data = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 157)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 70)