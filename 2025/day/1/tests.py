import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 3)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 6)
