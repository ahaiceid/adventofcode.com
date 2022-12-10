import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_input = ['30373', '25512', '65332', '33549', '35390']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_input), 21)

    def test_calculate_scenic_score(self):
        tree_grid = solver.CoordinateSpace([[int(h) for h in line.strip()] for line in self.sample_input])
        self.assertEqual(solver.calculate_scenic_score(tree_grid, (2,1)), 4)
        self.assertEqual(solver.calculate_scenic_score(tree_grid, (2,3)), 8)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_input), 8)