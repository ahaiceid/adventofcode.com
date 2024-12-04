import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        'MMMSXXMASM',
        'MSAMXMSMSA',
        'AMXSXMAAMM',
        'MSAMASMSMX',
        'XMASAMXAMM',
        'XXAMMXXAMA',
        'SMSMSASXSS',
        'SAXAMASAAA',
        'MAMMMXMMMM',
        'MXMXAXMASX']

    def test_diagonal_generation(self):
        sample_data = ['abc','def','ghi']
        expected = [
            # downward diagonals:
            'c',
            'bf',
            'aei',
            'dh',
            'g',
            # upward diagonals:
            'i',
            'hf',
            'gec',
            'db',
            'a']
        result = list(solver.generate_diagonals(sample_data))
        self.assertEqual(result, expected)

    def test_vertical_generation(self):
        sample_data = ['abc','def','ghi']
        expected = ['adg','beh','cfi']
        result = list(solver.generate_verticals(sample_data))
        self.assertEqual(result, expected)

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 18)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 9)