#!/usr/bin/python3
import unittest
import solver

class TestSolver(unittest.TestCase):

    square_loop = ['.....', '.S-7.', '.|.|.', '.L-J.', '.....']
    complex_loop = ['..F7.', '.FJ|.', 'SJ.L7', '|F--J', 'LJ...']

    def test_part1(self):
        self.assertEqual(solver.part1(self.square_loop), 4)
        self.assertEqual(solver.part1(self.complex_loop), 8)

    @unittest.skip('not implemented yet')
    def test_part2(self):
        sample1 = [
            '...........',
            '.S-------7.',
            '.|F-----7|.',
            '.||.....||.',
            '.||.....||.',
            '.|L-7.F-J|.',
            '.|..|.|..|.',
            '.L--J.L--J.', 
            '...........']
        self.assertEqual(solver.part2(sample1), 4)
        sample2 = [
            '.F----7F7F7F7F-7....',
            '.|F--7||||||||FJ....',
            '.||.FJ||||||||L7....',
            'FJL7L7LJLJ||LJ.L-7..',
            'L--J.L7...LJS7F-7L7.',
            '....F-J..F7FJ|L7L7L7',
            '....L7.F7||L7|.L7L7|',
            '.....|FJLJ|FJ|F7|.LJ',
            '....FJL-7.||.||||...',
            '....L---J.LJ.LJLJ...']
        self.assertEqual(solver.part2(sample2), 8)
        sample3 = [
            'FF7FSF7F7F7F7F7F---7',
            'L|LJ||||||||||||F--J',
            'FL-7LJLJ||||||LJL-77',
            'F--JF--7||LJLJ7F7FJ-',
            'L---JF-JLJ.||-FJLJJ7',
            '|F|F-JF---7F7-L7L|7|',
            '|FFJF7L7F-JF7|JL---7',
            '7-L-JL7||F7|L7F-7F7|',
            'L.L7LFJ|||||FJL7||LJ',
            'L7JLJL-JLJLJL--JLJ.L']
        self.assertEqual(solver.part2(sample3), 10)
