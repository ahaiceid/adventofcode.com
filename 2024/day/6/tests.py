import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = ['....#.....', '.........#', '..........', '..#.......', '.......#..', '..........', '.#..^.....', '........#.', '#.........', '......#...']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 41)

