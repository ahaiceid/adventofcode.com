#!/usr/bin/python3
import unittest
import solver

class TestSolver(unittest.TestCase):

    test_data = (
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26),
    )

    def test_part1(self):
        for input_data, result, _ in self.test_data:
            self.assertEqual(solver.part1(input_data), result)

    def test_part2(self):
        for input_data, _, result in self.test_data:
            self.assertEqual(solver.part2(input_data), result)
