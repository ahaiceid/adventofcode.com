#!/usr/bin/python3

from copy import deepcopy

def run(program):
    re = 0
    ic = 0
    executed = set()
    executor = {
        "acc": lambda ic, re, v: (ic + 1, re + v),
        "jmp": lambda ic, re, v: (ic + v, re),
        "nop": lambda ic, re, v: (ic + 1, re),
    }
    while ic < len(program):
        if ic in executed:
            return False, re
        executed.add(ic)
        operation = program[ic][0]
        value = program[ic][1]
        ic, re = executor[operation](ic, re, value)
    return True, re

if __name__ == "__main__":
    program = []
    with open("input") as fh:
        program = [(line.split()[0], int(line.split()[1])) for line in fh]
    # run the program, relying on loop detection to return accumulator value
    _, re = run(program)
    print("accumulator value at loop start: {}".format(re))
    # now attempt to repair the program by substituting jmp->nop and nop->jmp
    for i, inst in enumerate(program):
        if inst[0] in ["jmp","nop"]:
            _program = deepcopy(program)
            _program[i] = ("nop" if inst[0]=="jmp" else "jmp", inst[1]) 
            success, re = run(_program)
            if success:
                break
    print("accumulator value after fixing: {}".format(re))