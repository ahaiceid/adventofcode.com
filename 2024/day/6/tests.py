import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = ['....#.....', '.........#', '..........', '..#.......', '.......#..', '..........', '.#..^.....', '........#.', '#.........', '......#...']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), (41,6))

    @unittest.skip("not yet")
    def test_part2(self):
        pass

