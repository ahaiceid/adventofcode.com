import unittest
import solver


class TestSolver(unittest.TestCase):

    sample_data = ['123 328  51 64 ', ' 45 64  387 23 ',
                   '  6 98  215 314', '*   +   *   +  ']
    column_data = [
        [[123, 45, 6], '*'],
        [[328, 64, 98], '+'],
        [[51, 387, 215], '*'],
        [[64, 23, 314], '+']
    ]
    expected_column_values = [33210, 490, 4243455, 401]

    def test_input_parsing(self):
        parsed = solver.parse_input(self.sample_data)
        expected = self.column_data
        self.assertEqual(parsed, expected)

    def test_column_calculations(self):
        for col, value in zip(self.column_data, self.expected_column_values):
            self.assertEqual(solver.calculate_column(col), value)

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 4277556)

    resampled_column_data = [
        ['1', ' ', ' ', '*'],
        ['2', '4', ' ', ' '],
        ['3', '5', '6', ' '],
        [' ', ' ', ' ', ' '],
        ['3', '6', '9', '+'],
        ['2', '4', '8', ' '],
        ['8', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', '3', '2', '*'],
        ['5', '8', '1', ' '],
        ['1', '7', '5', ' '],
        [' ', ' ', ' ', ' '],
        ['6', '2', '3', '+'],
        ['4', '3', '1', ' '],
        [' ', ' ', '4', ' ']]

    column_data_2 = [
        [[4, 431, 623], '+'],
        [[175, 581, 32], '*'],
        [[8, 248, 369], '+'],
        [[356, 24, 1], '*']
    ]

    def test_input_parsing_2(self):
        parsed = solver.parse_input_2(self.sample_data)
        expected = self.resampled_column_data
        self.assertEqual(parsed, expected)

    def test_column_data_2(self):
        columnised = solver.columnise_data(self.resampled_column_data)
        expected = self.column_data_2
        self.assertEqual(columnised,expected)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data),  3263827)
