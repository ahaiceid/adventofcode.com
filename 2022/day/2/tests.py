import unittest
import solver

class TestSolver(unittest.TestCase):
    sample_data = ['A Y', 'B X', 'C Z']
    
    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 15)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 12)
