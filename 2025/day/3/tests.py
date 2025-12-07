import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']
    joltages = ['98','89','78','92']
    supplemental_data = [
        ('11','11'),
        ('112','12'),
        ('4663616535611513435323516234335342134544631343565436264451636222565334356426413214515616524251313789','89'),
        ('4329424422246434642322468233366144623347323344285322433231333466434534562417339322622363342535232334','99')]

    def test_joltage(self):
        for bank,joltage in zip(self.sample_data,self.joltages):
            self.assertEqual(solver.joltage(bank),joltage)

    def test_supplemental_joltage(self):
        for d in self.supplemental_data:
            self.assertEqual(solver.joltage(d[0]),d[1])

    def test_joltage_twelve(self):
        self.assertEqual(solver.joltage_twelve('987654321111111'), '987654321111')
        self.assertEqual(solver.joltage_twelve('811111111111119'), '811111111119')
        self.assertEqual(solver.joltage_twelve('234234234234278'), '434234234278')
        self.assertEqual(solver.joltage_twelve('818181911112111'), '888911112111')

    def test_part1(self):
        self.assertEqual(solver.total_joltage(self.sample_data, solver.joltage),357)

    def test_part2(self):
        self.assertEqual(solver.total_joltage(self.sample_data, solver.joltage_twelve), 3121910778619)
