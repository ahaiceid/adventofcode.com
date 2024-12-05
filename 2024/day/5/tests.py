import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        '47|53', '97|13', '97|61', '97|47', '75|29', '61|13', '75|53',
        '29|13', '97|29', '53|29', '61|53', '97|53', '61|29', '47|13',
        '75|47', '97|75', '47|61', '75|61', '47|29', '75|13', '53|13',
        '',
        '75,47,61,53,29',
        '97,61,53,29,13',
        '75,29,13',
        '75,97,47,61,53',
        '61,13,29',
        '97,13,75,29,47']

    def test_parse_rule_ordering(self):
        self.assertEqual(solver.parse_ordering_rules(self.sample_data), (
            {47: [53, 13, 61, 29],
             97: [13, 61, 47, 29, 53, 75],
             75: [29, 53, 47, 61, 13],
             61: [13, 53, 29],
             29: [13],
             53: [29, 13]
             },
            22))

    def test_parse_updates(self):
        self.assertEqual(
            solver.parse_updates(self.sample_data[22:]),
            [[75, 47, 61, 53, 29],
             [97, 61, 53, 29, 13],
             [75, 29, 13],
             [75, 97, 47, 61, 53],
             [61, 13, 29],
             [97, 13, 75, 29, 47]])

    def test_update_validation(self):
        ordering_rules = {
            47: [53, 13, 61, 29],
            97: [13, 61, 47, 29, 53, 75],
            75: [29, 53, 47, 61, 13],
            61: [13, 53, 29],
            29: [13],
            53: [29, 13]}
        self.assertTrue(solver.validate_update([75, 47, 61, 53, 29], ordering_rules))
        self.assertTrue(solver.validate_update([97, 61, 53, 29, 13], ordering_rules))
        self.assertTrue(solver.validate_update([75, 29, 13], ordering_rules))
        self.assertFalse(solver.validate_update([75, 97, 47, 61, 53], ordering_rules))
        self.assertFalse(solver.validate_update([61, 13, 29], ordering_rules))
        self.assertFalse(solver.validate_update([97, 13, 75, 29, 47], ordering_rules))

    def test_middle_page_number(self):
        self.assertEqual(solver.middle_page_number([75, 47, 61, 53, 29]), 61)
        self.assertEqual(solver.middle_page_number([97, 61, 53, 29, 13]), 53)
        self.assertEqual(solver.middle_page_number([75, 29, 13]), 29)

    def test_correct_ordering(self):
        ordering_rules = {
            47: [53, 13, 61, 29],
            97: [13, 61, 47, 29, 53, 75],
            75: [29, 53, 47, 61, 13],
            61: [13, 53, 29],
            29: [13],
            53: [29, 13]}
        self.assertEqual(solver.correct_ordering([75,97,47,61,53], ordering_rules), [97,75,47,61,53])
        self.assertEqual(solver.correct_ordering([61,13,29], ordering_rules), [61,29,13])
        self.assertEqual(solver.correct_ordering([97,13,75,29,47], ordering_rules),[97,75,47,29,13])

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 143)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 123)