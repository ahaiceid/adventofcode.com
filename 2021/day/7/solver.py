#!/usr/bin/python3

def linear_fuel_cost(inputs,pos):
    return sum([abs(x-pos) for x in inputs])

def exp_fuel_cost(inputs,pos):
    return sum([sum(range(1,abs(x-pos)+1)) for x in inputs])

if __name__ == "__main__":
    inputs = [int(x) for x in open("input").readline().split(",")]
    positions = range(min(inputs),max(inputs)+1)
    min_fuel = None
    for position in positions:
        cost = linear_fuel_cost(inputs,position)
        min_fuel = min_fuel and min(min_fuel,cost) or cost
    print(min_fuel)

    min_exp_fuel = None
    for position in positions:
        cost = exp_fuel_cost(inputs,position)
        min_exp_fuel = min_exp_fuel and min(min_exp_fuel,cost) or cost
    print(min_exp_fuel)