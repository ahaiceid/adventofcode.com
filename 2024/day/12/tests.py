import collections
import unittest
import io

import solver

class TestSolver(unittest.TestCase):

    small_sample_data = 'AAAA\nBBCD\nBBCC\nEEEC'
    sample_data = 'RRRRIICCFF\nRRRRIICCCF\nVVRRRCCFFF\nVVRCCCJFFF\nVVVVCJJCFE\nVVIVCCJJEE\nVVIIICJJEE\nMIIIIIJJEE\nMIIISIJEEE\nMMMISSJEEE'

    def test_generate_map(self):
        self.assertEqual(solver.generate_map(io.StringIO(self.small_sample_data)),
                         ['AAAA',
                          'BBCD',
                          'BBCC',
                          'EEEC'])
        self.assertEqual(solver.generate_map(
            io.StringIO(self.sample_data)),
            ['RRRRIICCFF',
             'RRRRIICCCF',
             'VVRRRCCFFF',
             'VVRCCCJFFF',
             'VVVVCJJCFE',
             'VVIVCCJJEE',
             'VVIIICJJEE',
             'MIIIIIJJEE',
             'MIIISIJEEE',
             'MMMISSJEEE'])

    def test_flood_area(self):
        small_sample_map = ['AAAA','BBCD','BBCC','EEEC']
        TestCaseData = collections.namedtuple(
            'TestCaseData',
            ['start_position', 'plots', 'boundary_length', 'area'])
        test_case_data = [
            TestCaseData((0,0), {(1, 0), (2, 0), (3, 0), (0, 0)}, 10, 4),
            TestCaseData((0,1), {(0,1),(1,1),(0,2),(1,2)}, 8, 4),
            TestCaseData((2,1), {(2,1),(2,2),(3,2),(3,3)}, 10, 4),
            TestCaseData((0,3), {(0,3),(1,3),(2,3)}, 8, 3),
            TestCaseData((3,1), {(3,1)}, 4, 1)]
        for tcd in test_case_data:
            plots, boundary_length, area = solver.flood_area(small_sample_map, tcd.start_position)
            self.assertEqual(plots, tcd.plots, tcd)
            self.assertEqual(boundary_length, tcd.boundary_length, tcd)
            self.assertEqual(area, tcd.area, tcd)

    def test_part1_small(self):
        self.assertEqual(solver.part1(io.StringIO(self.small_sample_data)), 140)
        self.assertEqual(solver.part1(io.StringIO('OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO')), 772)

    def test_part1(self):
        self.assertEqual(solver.part1(io.StringIO(self.sample_data)), 1930)