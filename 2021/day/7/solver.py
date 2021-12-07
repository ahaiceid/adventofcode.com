#!/usr/bin/python3

if __name__ == "__main__":
    inputs = [int(x) for x in open("input").readline().split(",")]
    print(min([sum([abs(x-pos) for x in inputs]) for pos in range(min(inputs),max(inputs)+1)]))
    print(min([sum([sum(range(1,abs(x-pos)+1)) for x in inputs]) for pos in range(min(inputs),max(inputs)+1)]))
