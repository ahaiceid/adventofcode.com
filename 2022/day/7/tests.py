import unittest
import solver

class TestSolver(unittest.TestCase):

    terminal_output = ['$ cd /', '$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']

    def test_part1(self):
        self.assertEqual(solver.part1(self.terminal_output), 95437)

    def test_part2(self):
        self.assertEqual(solver.part2(self.terminal_output), 24933642)