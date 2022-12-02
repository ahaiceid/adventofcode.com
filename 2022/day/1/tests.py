import unittest
import solver

class TestSolver(unittest.TestCase):
    sample_data = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 24000)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 45000)
