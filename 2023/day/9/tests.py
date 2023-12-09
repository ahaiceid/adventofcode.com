#!python3
import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        '0 3 6 9 12 15',
        '1 3 6 10 15 21',
        '10 13 16 21 30 45']

    def test_generate_next_sequence(self):
        self.assertEqual(
            solver._generate_next_sequence([0,3,6,9,12,15]),
            [3,3,3,3,3])
        self.assertEqual(
            solver._generate_next_sequence([3,3,3,3,3]),
            [0,0,0,0])

    def test_part1(self):
        self.assertTrue(solver.part1(self.sample_data),114)

    def test_part2(self):
        self.assertTrue(solver.part2(self.sample_data),2)