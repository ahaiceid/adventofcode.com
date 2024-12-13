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
        TestFloodAreaData = collections.namedtuple(
            'TestCaseData',
            ['start_position', 'plots', 'boundary_length', 'area'])
        test_flood_area_data = [
            TestFloodAreaData((0,0), {(1, 0), (2, 0), (3, 0), (0, 0)}, 10, 4),
            TestFloodAreaData((0,1), {(0,1),(1,1),(0,2),(1,2)}, 8, 4),
            TestFloodAreaData((2,1), {(2,1),(2,2),(3,2),(3,3)}, 10, 4),
            TestFloodAreaData((0,3), {(0,3),(1,3),(2,3)}, 8, 3),
            TestFloodAreaData((3,1), {(3,1)}, 4, 1)]
        for tfad in test_flood_area_data:
            plots, boundary_length, area = solver.flood_area(small_sample_map, tfad.start_position)
            self.assertEqual(plots, tfad.plots, tfad)
            self.assertEqual(boundary_length, tfad.boundary_length, tfad)
            self.assertEqual(area, tfad.area, tfad)

    def test_walk_boundary(self):
        small_sample_map = ['AAAA','BBCD','BBCC','EEEC']
        TestWalkBoundaryData = collections.namedtuple(
            'TestWalkBoundaryData',
            ['start_position', 'boundary_sides'])
        test_walk_boundary_data = [
            TestWalkBoundaryData((0,0), 4),
            TestWalkBoundaryData((0,1), 4),
            TestWalkBoundaryData((2,1), 8),
            TestWalkBoundaryData((0,3), 4),
            TestWalkBoundaryData((3,1), 4)]
        for twbd in test_walk_boundary_data:
            self.assertEqual(solver.walk_boundary(small_sample_map, twbd.start_position),twbd.boundary_sides, twbd)


    def test_part1_small(self):
        self.assertEqual(solver.part1(io.StringIO(self.small_sample_data)), 140)
        self.assertEqual(solver.part1(io.StringIO('OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO')), 772)

    def test_part1(self):
        self.assertEqual(solver.part1(io.StringIO(self.sample_data)), 1930)

    def test_part2(self):
        self.assertEqual(solver.part2(io.StringIO(self.small_sample_data)), 80)
        self.assertEqual(solver.part2(io.StringIO('OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO')), 436)
        self.assertEqual(solver.part2(io.StringIO('EEEEE\nEXXXX\nEEEEE\nEXXXX\nEEEEE')), 236)
        self.assertEqual(solver.part2(io.StringIO('AAAAAA\nAAABBA\nAAABBA\nABBAAA\nABBAAA\nAAAAAA')), 368)
        self.assertEqual(solver.part2(io.StringIO(self.sample_data)), 1206)
