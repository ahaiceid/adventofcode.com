import unittest
import solver

class TestSolver(unittest.TestCase):

    def test_count_trails(self):
        samples = [
            # score two
            (['...0...',
              '...1...',
              '...2...',
              '6543456',
              '7.....7',
              '8.....8',
              '9.....9'],
             (3,0),
             2),
            # score four
            (['..90..9',
              '...1.98',
              '...2..7',
              '6543456',
              '765.987',
              '876....',
              '987....'],
             (3,0),
             4),
            # score one
            (['10..9..',
              '2...8..',
              '3...7..',
              '4567654',
              '...8..3',
              '...9..2',
              '.....01'],
             (1,0),
             1),
            # score two
            (['10..9..',
              '2...8..',
              '3...7..',
              '4567654',
              '...8..3',
              '...9..2',
              '.....01'],
             (5,6),
             2)
            ]
        for data, start_position, expected_result in samples:
            trails, destinations = solver.count_trails(data, start_position)
            self.assertEqual(len(destinations), expected_result)
        sample_data = [
            '89010123',
            '78121874',
            '87430965',
            '96549874',
            '45678903',
            '32019012',
            '01329801',
            '10456732']
        for start_position, expected_result in [
                ((2,0),5),
                ((4,0),6),
                ((3,2),5),
                ((6,4),3),
                ((2,5),1),
                ((5,5),3),
                ((0,6),5),
                ((6,6),3),
                ((1,7),5)]:
            trails, destinations = solver.count_trails(sample_data, start_position)
            self.assertEqual(len(destinations), expected_result)

    def test_count_trails_ratings(self):
        samples = [
            # rating 3
            (['.....0.', '..4321.', '..5..2.', '..6543.', '..7..4.', '..8765.', '..9....'],
             (5,0),
             3)]
        for data, start_position, expected_result in samples:
            rating, destinations = solver.count_trails(data, start_position)
            self.assertEqual(rating, expected_result)

    def test_part1(self):
        sample_data = [
            '89010123',
            '78121874',
            '87430965',
            '96549874',
            '45678903',
            '32019012',
            '01329801',
            '10456732']
        self.assertEqual(solver.part1(sample_data)[0],36)

    def test_part2(self):
        sample_data = [
            '89010123',
            '78121874',
            '87430965',
            '96549874',
            '45678903',
            '32019012',
            '01329801',
            '10456732']
        self.assertEqual(solver.part1(sample_data)[1],81)
