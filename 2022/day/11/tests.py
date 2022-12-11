from math import prod
import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        'Monkey 0:',
        '  Starting items: 79, 98',
        '  Operation: new = old * 19',
        '  Test: divisible by 23',
        '    If true: throw to monkey 2',
        '    If false: throw to monkey 3',
        '',
        'Monkey 1:',
        '  Starting items: 54, 65, 75, 74',
        '  Operation: new = old + 6',
        '  Test: divisible by 19',
        '    If true: throw to monkey 2',
        '    If false: throw to monkey 0',
        '',
        'Monkey 2:',
        '  Starting items: 79, 60, 97',
        '  Operation: new = old * old',
        '  Test: divisible by 13',
        '    If true: throw to monkey 1',
        '    If false: throw to monkey 3',
        '',
        'Monkey 3:',
        '  Starting items: 74',
        '  Operation: new = old + 3',
        '  Test: divisible by 17',
        '    If true: throw to monkey 0',
        '    If false: throw to monkey 1',]

    def test_monkey_factory(self):
        monkey_factory = solver.MonkeyFactory()
        monkeys = monkey_factory.construct_monkeys(solver.read_in_chunks(self.sample_data))
        self.assertEqual(monkeys[0].items, [79,98])
        self.assertEqual(monkeys[0].divisor, 23)
        self.assertEqual(monkeys[0].target_monkeys, (2,3))

    #@unittest.skip('defunct because of changed worry modulation')
    def test_round(self):
        monkey_factory = solver.MonkeyFactory()
        monkeys = monkey_factory.construct_monkeys(solver.read_in_chunks(self.sample_data))
        divisor_lcm = prod([monkey.divisor for monkey in monkeys])
        inspections = [0 for _ in monkeys]
        solver.calculate_round(monkeys, inspections, 3, divisor_lcm)
        self.assertEqual(monkeys[0].items, [20, 23, 27, 26])
        self.assertEqual(monkeys[1].items, [2080, 25, 167, 207, 401, 1046])
        self.assertEqual(monkeys[2].items, [])
        self.assertEqual(monkeys[3].items, [])
        for _ in range(1,20):
            solver.calculate_round(monkeys, inspections, 3, divisor_lcm)
        self.assertEqual(inspections, [101, 95, 7, 105])

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 10605)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 2713310158)