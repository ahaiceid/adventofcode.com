#!/usr/bin/python3

from collections import Counter

def advance_func(state):
    next_state = {k-1: v for k, v in state.items() if 0<k}
    next_state[6] = state.get(7,0) + state.get(0,0)
    next_state[8] = state.get(0,0)
    return next_state

MACHINE = {
    "init":     lambda: Counter([int(x) for x in open("input").readline().split(',')]),
    "advance":  advance_func, 
    "evaluate": lambda x: sum(x.values()),
}

DAYS = [80,256]

if __name__ == "__main__":
    for days in DAYS:
        state = MACHINE["init"]()
        for i in range(days):
            state = MACHINE["advance"](state)
        print(MACHINE["evaluate"](state))
