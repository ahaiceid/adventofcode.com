#!/usr/bin/python3

OPERATORS = {
    "forward":  lambda op, st: (st[0] + op, st[1]),
    "down":     lambda op, st: (st[0], st[1] + op),
    "up":       lambda op, st: (st[0], st[1] - op),
}
INITIAL_STATE = (0,0)

OPERATORS2 = {
    "forward":  lambda op, st: (st[0] + op, st[1] + st[2] * op, st[2]),
    "down":     lambda op, st: (st[0], st[1], st[2] + op),
    "up":       lambda op, st: (st[0], st[1], st[2] - op),
}
INITIAL_STATE2 = (0,0,0)

class LocationMachine:

    def __init__(self, operators, state):
        self.operators = operators
        self.state = state

    def process(self, input):
        self.state = self.operators[input[0]](int(input[1]), self.state)

if __name__ == "__main__":
    lm = LocationMachine(OPERATORS, INITIAL_STATE)
    lm2 = LocationMachine(OPERATORS2, INITIAL_STATE2)
    with open("input") as fh:
        for line in fh.readlines():
            lm.process(line.strip().split())
            lm2.process(line.strip().split())
    print(lm.state[0] * lm.state[1])
    print(lm2.state[0] * lm2.state[1])

