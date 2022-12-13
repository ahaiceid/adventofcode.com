from functools import cmp_to_key
from json import loads
import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = ['[1,1,3,1,1]', '[1,1,5,1,1]', '', '[[1],[2,3,4]]', '[[1],4]', '', '[9]', '[[8,7,6]]', '', '[[4,4],4,4]', '[[4,4],4,4,4]', '', '[7,7,7,7]', '[7,7,7]', '', '[]', '[3]', '', '[[[]]]', '[[]]', '', '[1,[2,[3,[4,[5,6,7]]]],8,9]', '[1,[2,[3,[4,[5,6,0]]]],8,9]']

    sample_comparisons = [
        ([1,1,3,1,1], [1,1,5,1,1], -1),
        ([[1],[2,3,4]], [[1],4], -1),
        ([9], [8,7,6], 1),
        ([[4,4],4,4], [[4,4],4,4,4], -1),
        ([7,7,7,7],[7,7,7], 1),
        ([[[]]],[[]], 1),
        ([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9], 1)
    ]

    def test_compare(self):
        for sample_comparison in self.sample_comparisons:
            with self.subTest(str(sample_comparison)):
                self.assertEqual(solver.compare(sample_comparison[0],sample_comparison[1]),sample_comparison[2])

    def test_sorting(self):
        packet_list = [loads(packet) for packet in solver.read_ignoring_empty_lines(self.sample_data)] + [[[2]],[[6]]]
        packet_list.sort(key=cmp_to_key(solver.compare))
        expected = [[], [[]], [[[]]], [1, 1, 3, 1, 1], [1, 1, 5, 1, 1], [[1], [2, 3, 4]], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9], [1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [[1], 4], [[2]], [3], [[4, 4], 4, 4], [[4, 4], 4, 4, 4], [[6]], [7, 7, 7], [7, 7, 7, 7], [[8, 7, 6]], [9]]
        self.assertEqual(packet_list, expected)

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 13)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 140)
