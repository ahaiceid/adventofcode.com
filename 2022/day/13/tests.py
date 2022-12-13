import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = ['[1,1,3,1,1]', '[1,1,5,1,1]', '', '[[1],[2,3,4]]', '[[1],4]', '', '[9]', '[[8,7,6]]', '', '[[4,4],4,4]', '[[4,4],4,4,4]', '', '[7,7,7,7]', '[7,7,7]', '', '[]', '[3]', '', '[[[]]]', '[[]]', '', '[1,[2,[3,[4,[5,6,7]]]],8,9]', '[1,[2,[3,[4,[5,6,0]]]],8,9]']

    sample_comparisons = [
        ([1,1,3,1,1], [1,1,5,1,1], True),
        ([[1],[2,3,4]], [[1],4], True),
        ([9], [8,7,6], False),
        ([[4,4],4,4], [[4,4],4,4,4], True),
        ([7,7,7,7],[7,7,7], False),
        ([[[]]],[[]], False),
        ([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9], False)
    ]

    def test_comparator(self):
        for sample_comparison in self.sample_comparisons:
            with self.subTest(str(sample_comparison)):
                self.assertEqual(solver.is_less_than(sample_comparison[0],sample_comparison[1]),sample_comparison[2])

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 13)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 140)
