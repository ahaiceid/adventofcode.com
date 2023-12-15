#!/usr/bin/python3

import unittest
import solver

class TestSolver(unittest.TestCase):

    test_data = 'HASH'

    sample_data = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

    def test_part1(self):
        self.assertTrue(solver.part1(self.test_data), 52)
        self.assertTrue(solver.part1(self.sample_data), 1320)

    def test_part2(self):
        self.assertTrue(solver.part2(self.sample_data), 145)