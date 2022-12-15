import re
from reverse_onion_generator import generate_reverse_onion

def decode_sensor_report(report_pattern, sensor_report):
    match = re.match(report_pattern, sensor_report)
    values = [int(x) for x in match.group(1,2,3,4)]
    return (values[0],values[1]),(values[2],values[3])

def decode_sensor_reports(sensor_reports):
    report_pattern = re.compile(r'^Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)$')
    sensor_data = []
    for sensor_report in sensor_reports:
        sensor_pos, beacon_pos = decode_sensor_report(report_pattern, sensor_report.strip())
        sensor_data.append((sensor_pos, beacon_pos))
    return sensor_data

class SensorDetectionChecker:
    def __init__(self, sensor_pos, closest_beacon_pos) -> None:
        self.centre = sensor_pos
        self.distance = self._compute_cardinal_distance(sensor_pos, closest_beacon_pos)

    def is_within_range(self, pos) -> bool:
        return self.distance >= self._compute_cardinal_distance(self.centre, pos)

    def get_bounding_area(self):
        return ((self.centre[0]-self.distance, self.centre[1]-self.distance),
                (self.centre[0]+self.distance, self.centre[1]+self.distance))

    def _compute_cardinal_distance(self, p1, p2) -> int:
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def compute_cardinal_distance(p1, p2):
    return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])

def calculate_bounding_area(sensor_detection_checkers):
    min_x = min([sensor_detection_checker.get_bounding_area()[0][0] for sensor_detection_checker in sensor_detection_checkers])
    min_y = min([sensor_detection_checker.get_bounding_area()[0][1] for sensor_detection_checker in sensor_detection_checkers])
    max_x = max([sensor_detection_checker.get_bounding_area()[1][0] for sensor_detection_checker in sensor_detection_checkers])
    max_y = max([sensor_detection_checker.get_bounding_area()[1][1] for sensor_detection_checker in sensor_detection_checkers])
    return (min_x,min_y),(max_x,max_y)

def check_positions(sensor_detection_checkers, beacon_positions, positions_to_check):
    inside_detection_areas = set()
    positions_to_check = set(positions_to_check)
    positions_to_check -= set(beacon_positions)
    for position in positions_to_check:
        for sensor_detection_checker in sensor_detection_checkers:
            if sensor_detection_checker.is_within_range(position):
                inside_detection_areas.add(position)
                break
    return sorted(inside_detection_areas)

def part1(input_data, row_index=2000000):
    sensor_data = decode_sensor_reports(input_data)
    sensor_detection_checkers = [SensorDetectionChecker(*data) for data in sensor_data]
    beacon_positions = [data[1] for data in sensor_data]
    min_pos, max_pos = calculate_bounding_area(sensor_detection_checkers)
    positions = [(x,row_index) for x in range(min_pos[0],max_pos[0]+1)]
    return len(check_positions(sensor_detection_checkers,beacon_positions,positions))


def detector_perimeter_position_generator(sensor_detector_checker):
    centre = sensor_detector_checker.centre
    distance = sensor_detector_checker.distance + 1
    points = [
        (centre[0] + distance, centre[1]),
        (centre[0], centre[1] + distance),
        (centre[0] - distance, centre[1]),
        (centre[0], centre[1] - distance),
    ]
    position = points[0]
    while position != points[1]:
        position = position[0] - 1, position[1] + 1
        yield position
    while position != points[2]:
        position = position[0] - 1, position[1] - 1
        yield position
    while position != points[3]:
        position = position[0] + 1, position[1] - 1
        yield position
    while position != points[0]:
        position = position[0] + 1, position[1] + 1
        yield position

class PositionNotSuitable(Exception):
    pass

def part2(input_data, max_coord=4000000):
    sensor_data = decode_sensor_reports(input_data)
    sensor_detection_checkers = [SensorDetectionChecker(*data) for data in sensor_data]
    for sensor_detection_checker in sensor_detection_checkers:
        for position in detector_perimeter_position_generator(sensor_detection_checker):
            if min(position[0],position[1]) < 0:
                continue
            if max(position[0],position[1]) > max_coord:
                continue
            try:
                for sensor_detection_checker_ in sensor_detection_checkers:
                    if sensor_detection_checker_.is_within_range(position):
                        raise PositionNotSuitable()
            except PositionNotSuitable:
                continue
            return position[0]*4000000+position[1]

if __name__ == '__main__':
    with open('input', 'r') as data:
        print(part1(data))
    with open('input', 'r') as data:
        print(part2(data))