import unittest
import solver


class TestSolver(unittest.TestCase):

    sample_data = ['..@@.@@@@.', 
                   '@@@.@.@.@@', 
                   '@@@@@.@.@@', 
                   '@.@@@@..@.', 
                   '@@.@@@@.@@',
                   '.@@@@@@@.@', 
                   '.@.@.@.@@@', 
                   '@.@@@.@@@@', 
                   '.@@@@@@@@.', 
                   '@.@.@@@.@.']
    
    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 13)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 43)
