import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_input = ['30373', '25512', '65332', '33549', '35390']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_input), 21)

    @unittest.skip('Not yet implemented.')
    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_input), 0)