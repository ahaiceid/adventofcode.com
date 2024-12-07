import operator
import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        '190: 10 19',
        '3267: 81 40 27',
        '83: 17 5',
        '156: 15 6',
        '7290: 6 8 6 15',
        '161011: 16 10 13',
        '192: 17 8 14',
        '21037: 9 7 18 13',
        '292: 11 6 16 20']

    def test_validate_equation(self):
        ops = [operator.__mul__, operator.__add__]
        for i in [0,1,8]:
            self.assertTrue(
                solver.validate_equation(self.sample_data[i], ops))
        for i in [2,3,4,5,6,7]:
            self.assertFalse(
                solver.validate_equation(self.sample_data[i], ops))
        ops += [solver.combine_numbers]
        for i in [0,1,3,4,6]:
            self.assertTrue(
                solver.validate_equation(self.sample_data[i], ops))
        for i in [2,5,7]:
            self.assertFalse(
                solver.validate_equation(self.sample_data[i], ops))

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data, len(self.sample_data)), 3749)

    def test_combine_numbers(self):
        self.assertEqual(solver.combine_numbers(15,6),156)
        self.assertEqual(solver.combine_numbers(6,15),615)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data, len(self.sample_data)), 11387)