import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = ['3   4', '4   3', '2   5', '1   3', '3   9', '3   3']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 11)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 31)
