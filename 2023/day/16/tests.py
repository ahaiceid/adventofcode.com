#!/usr/bin/python3
import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        '.|...\\....',
        '|.-.\\.....',
        '.....|-...',
        '........|.',
        '..........',
        '.........\\',
        '..../.\\\\..',
        '.-.-/..|..',
        ".|....-|.\\",
        '..//.|....']

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data), 46)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data), 51)