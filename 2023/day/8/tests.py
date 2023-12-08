#!/usr/bin/python3
import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data_1 = [
        'RL',
        '', 
        'AAA = (BBB, CCC)',
        'BBB = (DDD, EEE)',
        'CCC = (ZZZ, GGG)',
        'DDD = (DDD, DDD)',
        'EEE = (EEE, EEE)',
        'GGG = (GGG, GGG)',
        'ZZZ = (ZZZ, ZZZ)']

    sample_data_2 = [
        'LLR',
        '',
        'AAA = (BBB, BBB)',
        'BBB = (AAA, ZZZ)',
        'ZZZ = (ZZZ, ZZZ)']

    sample_data_3 = [
        'LR',
        '',
        '11A = (11B, XXX)',
        '11B = (XXX, 11Z)',
        '11Z = (11B, XXX)',
        '22A = (22B, XXX)',
        '22B = (22C, 22C)',
        '22C = (22Z, 22Z)',
        '22Z = (22B, 22B)',
        'XXX = (XXX, XXX)']

    def test_read_directions(self):
        self.assertEqual(solver.read_directions(iter(self.sample_data_1)), [1,0])

    def test_read_network(self):
        self.assertEqual(
            solver.read_network(iter(self.sample_data_2[2:])),
            {
                'AAA': ('BBB','BBB'),
                'BBB': ('AAA','ZZZ'),
                'ZZZ': ('ZZZ','ZZZ')
            })

    def test_part1_1(self):
        self.assertEqual(solver.part1(iter(self.sample_data_1)), 2) 
        self.assertEqual(solver.part1(iter(self.sample_data_2)), 6)

    def test_part2(self):
        self.assertEqual(solver.part2(iter(self.sample_data_3)), 6)