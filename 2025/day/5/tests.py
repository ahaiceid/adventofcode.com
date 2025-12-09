import unittest
from unittest.mock import mock_open, patch
import solver

class TestSolver(unittest.TestCase):

    sample_data = ['3-5\n',
                   '10-14\n',
                   '16-20\n',
                   '12-18\n',
                   '\n',
                   '1\n',
                   '5\n',
                   '8\n',
                   '11\n',
                   '17\n',
                   '32\n']
    expected_ranges = {3:6, 10:21}

    def test_construct_ranges(self):
        self.assertEqual(
            solver.construct_ranges(
                self.sample_data[0:4]), self.expected_ranges)

    def test_check_ingredient(self):
        for id in [1,8,32]:
            self.assertFalse(
                solver.check_ingredient(
                    self.expected_ranges, id))
        for id in [5,11,17]:
            self.assertTrue(
                solver.check_ingredient(
                    self.expected_ranges, id), f'{id}')
            
    def test_part1(self):
        with patch('__main__.open', 
                   mock_open(read_data=''.join(self.sample_data))):
            with open('input','r') as mfh:
                result = solver.part1(mfh)
        self.assertEqual(result, 3)

        """
from unittest.mock import patch, mock_open
with patch("builtins.open", mock_open(read_data="data")) as mock_file:
    assert open("path/to/open").read() == "data"
mock_file.assert_called_with("path/to/open")"""