#!/usr/bin/python3
from functools import reduce
from math import prod

MACHINE1 = {
    "init":     (0,0),
    "evaluate":   lambda st: (st[0] * st[1]),
    "forward":  lambda op, st: (st[0] + op, st[1]),
    "down":     lambda op, st: (st[0], st[1] + op),
    "up":       lambda op, st: (st[0], st[1] - op),
}

MACHINE2 = {
    "init":     (0,0,0),
    "evaluate": lambda st: (st[0] * st[1]),
    "forward":  lambda op, st: (st[0] + op, st[1] + st[2] * op, st[2]),
    "down":     lambda op, st: (st[0], st[1], st[2] + op),
    "up":       lambda op, st: (st[0], st[1], st[2] - op),
}

def processor(machine):
    def f(state, input):
        nonlocal machine
        return machine[input[0]](int(input[1]), state)
    return f

if __name__ == "__main__":
    with open("input") as fh:
        print(MACHINE1["evaluate"](reduce(processor(MACHINE1), [ln.strip().split() for ln in fh.readlines()], MACHINE1["init"])))
    with open("input") as fh:
        print(MACHINE2["evaluate"](reduce(processor(MACHINE2), [ln.strip().split() for ln in fh.readlines()], MACHINE2["init"])[:2]))
