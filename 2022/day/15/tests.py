import unittest
import re
import solver

class TestSolver(unittest.TestCase):

    sample_data = [
        'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
        'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
        'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
        'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
        'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
        'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
        'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
        'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
        'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
        'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
        'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
        'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
        'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
        'Sensor at x=20, y=1: closest beacon is at x=15, y=3']

    sample_sensor_reports = [
        ((2, 18), (-2, 15)),
        ((9, 16), (10, 16)),
        ((13, 2), (15, 3)),
        ((12, 14), (10, 16)),
        ((10, 20), (10, 16)),
        ((14, 17), (10, 16)),
        ((8, 7), (2, 10)),
        ((2, 0), (2, 10)),
        ((0, 11), (2, 10)),
        ((20, 14), (25, 17)),
        ((17, 20), (21, 22)),
        ((16, 7), (15, 3)),
        ((14, 3), (15, 3)),
        ((20, 1), (15, 3))]

    def test_decode_sensor_report(self):
        pattern = re.compile(r'^Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)$')
        self.assertEqual(solver.decode_sensor_report(pattern,self.sample_data[0]),self.sample_sensor_reports[0])

    def test_decode_sensor_reports(self):
        report_data = solver.decode_sensor_reports(self.sample_data)
        self.assertEqual(solver.decode_sensor_reports(self.sample_data), self.sample_sensor_reports)

    def test_sensor_distance(self):
        sensor_detection = solver.SensorDetectionChecker(*self.sample_sensor_reports[6])
        self.assertEqual(sensor_detection.is_within_range(self.sample_sensor_reports[6][1]), True)
        positions = set([sensor_report[1] for sensor_report in self.sample_sensor_reports])
        positions.remove(self.sample_sensor_reports[6][1])
        for position in positions:
            with self.subTest('Sensor Detection: {}'.format(position)):
                self.assertEqual(sensor_detection.is_within_range(position), False)

    def test_calculate_bounding_area(self):
        sensor_detection_checkers = [solver.SensorDetectionChecker(*report) for report in self.sample_sensor_reports[:2]]
        self.assertEqual(solver.calculate_bounding_area(sensor_detection_checkers), ((-5, 11), (10, 25)))
    
    def test_check_positions(self):
        sensor_detection_checkers = [solver.SensorDetectionChecker(*sensor_report) for sensor_report in self.sample_sensor_reports]
        beacon_positions = [sensor_report[1] for sensor_report in self.sample_sensor_reports]
        min_pos, max_pos = solver.calculate_bounding_area(sensor_detection_checkers)
        positions = [(x,10) for x in range(min_pos[0], max_pos[0]+1)]
        expected_positions = [(-2, 10), (-1, 10), (0, 10), (1, 10), (3, 10), (4, 10),
                              (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10),
                              (12, 10), (13, 10), (14, 10), (15, 10), (16, 10), (17, 10),
                              (18, 10), (19, 10), (20, 10), (21, 10), (22, 10), (23, 10), (24, 10)]
        self.assertEqual(solver.check_positions(sensor_detection_checkers,beacon_positions,positions),expected_positions)

    def test_part1(self):
        self.assertEqual(solver.part1(self.sample_data, 10), 26)

    def test_part2(self):
        self.assertEqual(solver.part2(self.sample_data, 20), 56000011)