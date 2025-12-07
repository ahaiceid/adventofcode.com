import unittest
import solver


class TestSolver(unittest.TestCase):

    sample_input = ['.......S.......',
                     '...............',
                     '.......^.......',
                     '...............',
                     '......^.^......',
                     '...............',
                     '.....^.^.^.....',
                     '...............',
                     '....^.^...^....',
                     '...............',
                     '...^.^...^.^...',
                     '...............',
                     '..^...^.....^..',
                     '...............',
                     '.^.^.^.^.^...^.',
                     '...............']

    def test_get_start_position(self):
        start_pos = solver.get_start_position(self.sample_input)
        self.assertEqual(start_pos, (0, 7))

    def test_get_next_positions(self):
        expected_positions = [{(0, 7)}, {(1, 7)}, {(2, 6), (2, 8)}, {
            (3, 6), (3, 8)}, {(4, 5), (4, 7), (4, 9)}]
        for i in range(len(expected_positions)-1):
            current_positions = expected_positions[i]
            expected_next_position = expected_positions[i+1]
            next_positions, _ = solver.get_next_positions(
                self.sample_input, current_positions)
            self.assertEqual(next_positions, expected_next_position)

    def test_part1(self):
        result = solver.part1(self.sample_input)
        self.assertEqual(result, 21)

    def test_part2(self):
        result = solver.part2(self.sample_input)
        self.assertEqual(result, 40)
