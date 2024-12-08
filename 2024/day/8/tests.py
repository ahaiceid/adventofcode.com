import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        '............',
        '........0...',
        '.....0......',
        '.......0....',
        '....0.......',
        '......A.....',
        '............',
        '............',
        '........A...',
        '.........A..',
        '............',
        '............']

    def test_get_antenna_locations(self):
        expected_locations = [
            ('0', (8, 1)), ('0', (5, 2)), ('0', (7, 3)), ('0', (4, 4)),
            ('A', (6, 5)), ('A', (8, 8)), ('A', (9, 9))]
        self.assertEqual(
            expected_locations,
            solver.get_antenna_locations(self.sample_data))

    def test_get_per_frequency_locations(self):
        location_list = [
            ('0', (8, 1)), ('0', (5, 2)), ('0', (7, 3)), ('0', (4, 4)),
            ('A', (6, 5)), ('A', (8, 8)), ('A', (9, 9))]
        expected_locations = {
            '0': [(8,1), (5,2), (7,3), (4,4)],
            'A': [(6,5), (8,8), (9,9)]}
        self.assertEqual(
            expected_locations,
            solver.get_per_frequency_locations(location_list))

    def test_antinodes_for_pair(self):
        antenna_pair = [(4,3),(5,5)]
        expected_antinodes = set([(3,1),(6,7)])
        self.assertEqual(
            expected_antinodes,
            solver.get_antinodes_for_pair(*antenna_pair))

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 14)

    def test_part2(self):
        t_data = ['T....#....', '...T......', '.T....#...', '.........#', '..#.......', '..........', '...#......', '..........', '....#.....', '..........']
        self.assertEqual(solver.part2(t_data), 9)
        self.assertEqual(solver.part2(self.sample_data), 34)