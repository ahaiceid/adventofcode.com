#!/usr/bin/python3


class Navigation:
    def __init__(self):
        self.lat = 0
        self.long = 0
        self.heading = 0
        self.actions = {
            'N': lambda v: self._north(v),
            'S': lambda v: self._south(v),
            'E': lambda v: self._east(v),
            'W': lambda v: self._west(v),
            'R': lambda v: self._rotate(v),
            'L': lambda v: self._rotate(-v),
            'F': lambda v: self._east(v)
        }

    def _north(self, distance): self.lat += distance
    def _south(self, distance): self.lat -= distance
    def _east(self, distance): self.long -= distance
    def _west(self, distance): self.long += distance
    def _rotate(self, rotation):
        self.heading = (self.heading + rotation + 360) % 360
        if self.heading == 0:
            self.actions['F'] = self.actions['E']
        elif self.heading == 90:
            self.actions['F'] = self.actions['S']
        elif self.heading == 180:
            self.actions['F'] = self.actions['W']
        elif self.heading == 270:
            self.actions['F'] = self.actions['N']

    def process(self, action, s):
        self.actions[action](s)

    def manhattan_distance(self):
        return abs(self.lat) + abs(self.long)

class WaypointNavigation:
    def __init__(self):
        self.waypoint_lat = 1
        self.waypoint_long = 10
        self.ship_lat = 0
        self.ship_long = 0
        self.actions = {
            'N': lambda v: self._north(v),
            'S': lambda v: self._south(v),
            'E': lambda v: self._east(v),
            'W': lambda v: self._west(v),
            'R': lambda v: self._rotate(v//90),
            'L': lambda v: self._rotate((360-v)//90),
            'F': lambda v: self._forward(v)
        }

    def _north(self, distance): self.waypoint_lat += distance
    def _south(self, distance): self.waypoint_lat -= distance
    def _east(self, distance): self.waypoint_long += distance
    def _west(self, distance): self.waypoint_long -= distance
    def _rotate(self, rotation):
        for _ in range(rotation):
            waypoint_long = self.waypoint_lat
            self.waypoint_lat = - self.waypoint_long
            self.waypoint_long = waypoint_long
    def _forward(self, value):
        self.ship_lat += (self.waypoint_lat * value)
        self.ship_long += (self.waypoint_long * value)

    def process(self, action, s):
        self.actions[action](s)

    def manhattan_distance(self):
        return abs(self.ship_lat) + abs(self.ship_long)

if __name__ == "__main__":
    navigation = Navigation()
    with open("input") as fh:
        for line in fh:
            navigation.process(line[0], int(line[1:]))
    print(navigation.manhattan_distance())
    waypoint_navigation = WaypointNavigation()
    with open("input") as fh:
        for line in fh:
            waypoint_navigation.process(line[0], int(line[1:]))
    print(waypoint_navigation.manhattan_distance())