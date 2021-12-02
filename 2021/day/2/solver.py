#!/usr/bin/python3

MACHINE1 = {
    "init":     (0,0),
    "forward":  lambda op, st: (st[0] + op, st[1]),
    "down":     lambda op, st: (st[0], st[1] + op),
    "up":       lambda op, st: (st[0], st[1] - op),
}

MACHINE2 = {
    "init":     (0,0,0),
    "forward":  lambda op, st: (st[0] + op, st[1] + st[2] * op, st[2]),
    "down":     lambda op, st: (st[0], st[1], st[2] + op),
    "up":       lambda op, st: (st[0], st[1], st[2] - op),
}

class LocationMachine:

    def __init__(self, operators):
        self.operators = operators
        self.state = self.operators["init"]

    def process(self, input):
        self.state = self.operators[input[0]](int(input[1]), self.state)

if __name__ == "__main__":
    lm = LocationMachine(MACHINE1)
    lm2 = LocationMachine(MACHINE2)
    with open("input") as fh:
        for line in fh.readlines():
            lm.process(line.strip().split())
            lm2.process(line.strip().split())
    print(lm.state[0] * lm.state[1])
    print(lm2.state[0] * lm2.state[1])

