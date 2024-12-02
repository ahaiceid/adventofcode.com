#!python3
import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        '7 6 4 2 1',
        '1 2 7 8 9',
        '9 7 6 2 1',
        '1 3 2 4 5',
        '8 6 4 4 1',
        '1 3 6 7 9']

    def test_part1(self):
        reports = [[int(n) for n in r.split()] for r in self.sample_data]
        for r in [0,5]:
            self.assertTrue(solver.report_is_safe(reports[r]))
        for r in [1,2,3,4]:
            self.assertFalse(solver.report_is_safe(reports[r]))
        self.assertEqual(solver.part1(self.sample_data), 2)

    def test_part2(self):
        reports = [[int(n) for n in r.split()] for r in self.sample_data]
        for r in [0,3,4,5]:
            self.assertTrue(solver.report_is_safe_with_damping(reports[r]))
        for r in [1,2]:
            self.assertFalse(solver.report_is_safe_with_damping(reports[r]))
        self.assertEqual(solver.part2(self.sample_data), 4)

    def test_part2_additional(self):
        additional_unsafe_reports = [
            '5 9 12 14 11',
            '39 43 46 48 49 52 54 54',
            '14 18 19 21 24 28',
            '11 15 17 18 23']
        reports = [[int(n) for n in r.split()] for r in additional_unsafe_reports]
        for report in reports:
            self.assertFalse(solver.report_is_safe_with_damping2(report))
