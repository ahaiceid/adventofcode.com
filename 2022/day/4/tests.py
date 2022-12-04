import unittest
import solver

class TestSolver(unittest.TestCase):
    sample_input = ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_input), 2)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_input), 4)