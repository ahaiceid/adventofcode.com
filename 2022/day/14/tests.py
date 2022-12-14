import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_input = ['498,4 -> 498,6 -> 496,6', '503,4 -> 502,4 -> 502,9 -> 494,9']
    vertex_data = (503, 9, [[(498, 4), (498, 6), (496, 6)], [(503, 4), (502, 4), (502, 9), (494, 9)]])
    expected_rock_locations = set([
            (494, 9), (495, 9), (496, 6), (496, 9), (497, 6), (497, 9),
            (498, 4), (498, 5), (498, 6), (498, 9), (499, 9), (500, 9),
            (501, 9), (502, 4), (502, 5), (502, 6), (502, 7), (502, 8),
            (502, 9), (503, 4)])

    def test_yield_pairs(self):
        sample_input_generator = iter(self.sample_input[0].split(' -> '))
        sample_input_pairs = [pair for pair in solver.yield_pairs(sample_input_generator)]
        self.assertEqual([('498,4','498,6'),('498,6','496,6')], sample_input_pairs)

    def test_decode_vertex_lists(self):
        self.assertEqual(solver.decode_vertex_lists(
            self.sample_input),self.vertex_data)
    
    def test_decode_vertex_list_offset(self):
        self.assertEqual(solver.decode_vertex_lists(
            [self.sample_input[0]],1), (499,6,[[(499,4),(499,6),(497,6)]]))

    def test_rasterise_rock(self):
        data = [[' ' for x in range(self.vertex_data[0]+1)]
                for y in range(self.vertex_data[1]+1)]
        space = solver.CoordinateSpace(data)
        solver.rasterise_rock(space, iter(self.vertex_data[2]))

        rock_locations = set()
        for y in range(self.vertex_data[1]+1):
            for x in range(self.vertex_data[0]+1):
                if space[(x,y)] == '#':
                    rock_locations.add((x,y))
        self.assertEqual(rock_locations, self.expected_rock_locations)

    def test_drop_sand(self):
        space = solver.CoordinateSpace(
            ['          ',
            '          ',
            '          ',
            '          ',
            '    #   ##',
            '    #   # ',
            '  ###   # ',
            '        # ',
            '        # ',
            '######### '])
        start_position = (6,0)
        end_positions = [(6,8),(5,8),(7,8),(6,7)]
        for grain_number, end_position in enumerate(end_positions):
            with self.subTest('Drop grain {}'.format(grain_number+1)):
                self.assertEqual(solver.drop_sand(space, start_position), end_positions[grain_number])
                space[end_positions[grain_number]] = 'o'

        space = solver.CoordinateSpace(
            ['          ',
            '          ',
            '      o   ',
            '     ooo  ',
            '    #ooo##',
            '    #ooo# ',
            '  ###ooo# ',
            '    oooo# ',
            '   ooooo# ',
            '######### '])
        with self.subTest('Drop grain 22'):
            self.assertEqual(solver.drop_sand(space, start_position), (3,5))
            space[(3,5)] = 'o'
        with self.subTest('Drop grain 23'):
            self.assertEqual(solver.drop_sand(space, start_position), (1,8))
            space[(1,8)] = 'o'
        with self.subTest('Drop grain 24'):
            self.assertEqual(solver.drop_sand(space, start_position), None)

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_input), 24)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_input), 93)