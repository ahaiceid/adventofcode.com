import unittest
import solver

class TestSolver(unittest.TestCase):

    def test_part1(self):
        sample_data = ['xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))']
        self.assertEqual(solver.part1(sample_data),161)
        self.assertEqual(solver.part1(["mul(1,2,3)"]),0)

    def test_part2(self):
        sample_data = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
        self.assertEqual(solver.part2(sample_data),48)
