import unittest
import solver

class TestSolver(unittest.TestCase):

    sample_data = ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224', '1698522-1698528', '446443-446449', '38593856-38593862', '565653-565659', '824824821-824824827', '2121212118-2121212124']

    def test_is_valid_id1(self):
        for id in ['55','6464','123123']:
            self.assertFalse(solver.is_valid_id_part1(id))
        for id in ['101']:
            self.assertTrue(solver.is_valid_id_part1(id))

    def test_is_valid_id2(self):
        for id in ['12341234','123123123','1212121212','1111111','1188511885','38593859']:
            self.assertFalse(solver.is_valid_id_part2(id), id)
        for id in ['12341234','123123123','1212121212','1188511885','38593859']:
            self.assertTrue(solver.is_valid_id_part2(id[1:]), id[1:])

    def test_values(self):
        self.assertEqual([x for x in solver.values(11,22)],[x for x in range(11,23)])

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data),1227775554)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data),4174379265)
