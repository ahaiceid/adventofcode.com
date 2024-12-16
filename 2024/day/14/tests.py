import io
import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        'p=0,4 v=3,-3',
        'p=6,3 v=-1,-3',
        'p=10,3 v=-1,2',
        'p=2,0 v=2,-1',
        'p=0,0 v=1,3',
        'p=3,0 v=-2,-2',
        'p=7,6 v=-1,-3',
        'p=3,0 v=-1,-2',
        'p=9,3 v=2,3',
        'p=7,3 v=-1,2',
        'p=2,4 v=2,-3',
        'p=9,5 v=-3,-3']

    def test_read_robot(self):
        self.assertEqual(
            solver.read_robot(self.sample_data[0]+'\n'),
            ((0,4),(3,-3)))

    def test_advance_robot(self):
        pos = (2,4)
        vel = (2,-3)
        test_data = [
            #steps: position
            (1, (4,1)),
            (2, (6,5)),
            (3, (8,2)),
            (4, (10,6)),
            (5, (1,3))]
        for steps, expected_position in test_data:
            self.assertEqual(
                solver.advance_robot(pos, vel, 11, 7, steps),
                expected_position)

    def test_part1(self):
        self.assertEqual(
            solver.part1(io.StringIO('\n'.join(self.sample_data)), 11, 7),
            12)