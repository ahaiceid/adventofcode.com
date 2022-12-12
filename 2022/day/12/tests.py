import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = ['Sabqponm', 'abcryxxl', 'accszExk', 'acctuvwj', 'abdefghi']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 31)
        '''height_grid = solver.CoordinateSpace([[h for h in row] for row in self.sample_data])
        graph = solver.Graph()
        graph.nodes = solver.CoordinateSpace([[graph.create_node(height_grid,(x,y)) for x in range(height_grid.width)] for y in range(height_grid.height)])
        self.assertEqual(graph.traverse(), 31)'''

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 29)
